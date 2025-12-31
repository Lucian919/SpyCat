from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from .models import Cat
from .serializers import CatSerializer

class CatViewSet(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
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
        """Allow PATCH to update only the `salary` field.

        If the request contains any keys other than `salary`, return 400.
        """
        allowed = {"salary"}
        incoming_keys = set(request.data.keys())
        if not incoming_keys.issubset(allowed):
            return Response(
                {"detail": "Only 'salary' may be updated via PATCH."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().partial_update(request, *args, **kwargs)