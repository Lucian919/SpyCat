from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from .models import Target
from .serializers import TargetSerializer
from rest_framework.decorators import action


class TargetViewSet(viewsets.GenericViewSet,
                    mixins.UpdateModelMixin):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
    permission_classes = []  # Allow unrestricted access

    def update(self, request, *args, **kwargs):
        """Disable PUT method but allow PATCH method."""
        if request.method == "PUT":
            return Response(
                {"detail": "PUT method is not allowed."},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Allow PATCH to update only the `notes` field.

        If the request contains any keys other than `notes`, return 400.
        """
        allowed = {"notes"}
        incoming_keys = set(request.data.keys())
        if not incoming_keys.issubset(allowed):
            return Response(
                {"detail": "Only 'notes' may be updated via PATCH."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        target_instance = self.get_object()
        if target_instance.is_completed or target_instance.mission.is_completed:
            return Response(
                {"detail": "Cannot update notes of a completed target/mission."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().partial_update(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def mark_completed(self, request, pk=None):
        """Mark the target as completed."""
        target = self.get_object()
        target.is_completed = True
        target.save()
        if target.mission.targets.filter(is_completed=False).count() == 0:
            target.mission.is_completed = True
            target.mission.save()
        serializer = self.get_serializer(target)
        return Response(serializer.data)