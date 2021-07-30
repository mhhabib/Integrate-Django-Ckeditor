from django.urls import path
from .views import create

urlpatterns = {
    path('', create.as_view(), name='create-post'),
}
