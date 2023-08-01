from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *


urlpatterns = [
    path('', PostView.as_view(), name='allpost'),
    path('<int:pk>', DetailPost.as_view(), name='fullpost'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('<int:pk>/createresp/', NewResponse.as_view(), name='createresp'),
    path('<int:pk>/respdelete/', responsedelete, name='resp_delete'),
    path('<int:pk>/accept/', accept, name='accept'),
    path('<int:pk>/denied/', denied, name='denied'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)