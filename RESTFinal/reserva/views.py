from rest_framework import generics
from .models import Reserva
from .serializers import ReservaSerializer


class ReservaListCreate(generics.ListCreateAPIView):
    queryset = Reserva.objects.all().order_by('-id')[:10]
    serializer_class = ReservaSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new post."""
        serializer.save()

class ReservaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
