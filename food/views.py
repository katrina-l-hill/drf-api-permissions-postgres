from rest_framework import generics
from .models import Food
from .serializers import FoodSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.


class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
