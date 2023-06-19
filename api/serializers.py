from rest_framework import serializers
from .models import Url


class UrlSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = Url
        fields = ["original_url", "short_url"]
        read_only_fields = ["short_url", ]

    def get_short_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/{obj.key}/')
