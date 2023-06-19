import uuid

from rest_framework import generics

from .models import Url
from .serializers import UrlSerializer


class GenerateShortUrl(generics.CreateAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer

    def perform_create(self, serializer):
        serializer.save(key=str(uuid.uuid4())[:6])


class GetOriginalUrl(generics.RetrieveAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    lookup_field = 'key'
