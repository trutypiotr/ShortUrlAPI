import json
import uuid

from django.test import TestCase
from rest_framework.reverse import reverse

from .models import Url


class GenerateShortUrlTest(TestCase):
    def setUp(self):
        self.url = reverse('generate_short_url')

    def test_valid_url(self):
        response = self.client.post(self.url, {"original_url": "http://example.com"})
        self.assertEqual(response.status_code, 201)

    def test_invalid_url(self):
        response = self.client.post(self.url, {"original_url": "example.com"})
        self.assertEqual(response.status_code, 400)


class GetOriginalUrlTest(TestCase):
    def setUp(self):
        key = str(uuid.uuid4())[:6]
        self.original_url = "http://example.com"
        Url.objects.create(key=key, original_url=self.original_url)
        self.url = reverse('get_original_url', kwargs={"key": key})

    def test_valid_key(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(self.original_url, response_data.get('original_url'))
