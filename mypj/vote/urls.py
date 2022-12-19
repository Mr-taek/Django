from django.urls import path

from .views import detail

app_name="votes"

urlpatterns=[
    path('',detail)
]