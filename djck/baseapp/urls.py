from django.urls import path
from .views import home, create, PostDetailView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home.as_view(), name='home'),
    path('create/', create.as_view(), name='create-post'),
    path('<int:pk>/', PostDetailView.as_view(), name='details'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
