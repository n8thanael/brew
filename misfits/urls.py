from django.urls import path
from misfits.views import home, test

urlpatterns = [
    path('', home, name="home"),
    path('test', test, name="test"),
]