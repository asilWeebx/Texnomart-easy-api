# views.py
from rest_framework import generics
from rest_framework.parsers import MultiPartParser

from .models import Card, Category
from .serializers import CardSerializer, CategorySerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CardListCreateView(generics.ListCreateAPIView):
    serializer_class = CardSerializer
    parser_classes = [MultiPartParser, ]
    def get_queryset(self):
        category_id = self.kwargs.get('category_id', None)
        if category_id:
            return Card.objects.filter(category_id=category_id)
        return Card.objects.all()

class CardRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    parser_classes = [MultiPartParser, ]
