from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from .models import Cat, Mission
from .serializers import MissionSerializer, TargetSerializer
from rest_framework.decorators import action


class MissionViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    permission_classes = []  # Allow unrestricted access

    def create(self, request, *args, **kwargs):
        """Create a new Mission."""
        targets_data = request.data.pop('targets')
        
        mission_serializer = self.get_serializer(data=request.data)
        mission_serializer.is_valid(raise_exception=True)
        mission_instance = mission_serializer.save()

        target_serializer = TargetSerializer(data=targets_data, many=True)
        target_serializer.is_valid(raise_exception=True)
        target_serializer.save(mission=mission_instance)

        return Response(self.get_serializer(mission_instance).data, status=status.HTTP_201_CREATED)
    
    def delete(self, request, *args, **kwargs):
        """Delete a Mission and its associated Targets."""
        mission = self.get_object()
        if not mission.cat:
            mission.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"detail": "Cannot delete a mission assigned to a cat."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    def update(self, request, *args, **kwargs):
        """Disable PUT method but allow PATCH method."""
        if request.method == "PUT":
            return Response(
                {"detail": "PUT method is not allowed."},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        return super().update(request, *args, **kwargs)


    @action(detail=True, methods=['post'])
    def mark_completed(self, request, pk=None):
        """Mark the mission and its target as completed."""
        mission = self.get_object()
        mission.is_completed = True
        mission.save()
        serializer = self.get_serializer(mission)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def assign_cat(self, request, pk=None):
        """Assign a cat to the mission."""
        mission = self.get_object()
        cat_id = request.data.get('cat_id')
        try:
            cat = Cat.objects.get(id=cat_id)
        except Cat.DoesNotExist:
            return Response(
                {"detail": "Cat not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        mission.cat = cat
        mission.save()
        serializer = self.get_serializer(mission)
        return Response(serializer.data)