from rest_framework import viewsets, mixins
from .models import Book
from .serializers import BookSerializer

class BookViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



# Create your views here. --- IGNORE ---


