from django.urls import path
from . import views

urlpatterns = [
    path('url/', views.GenerateShortUrl.as_view(), name="generate_short_url"),
    path('<str:key>/', views.GetOriginalUrl.as_view(), name="get_original_url"),
]
