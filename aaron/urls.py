from django.urls import path
from aaron.views import aaron

urlpatterns = [
    path('aaron', aaron, name="aaron"),
]