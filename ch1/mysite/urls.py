from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers
# from theme.views import ThemeViewSet
from accounts.views import ProfileViewSet
from django.conf import settings
from django.conf.urls.static import static
from .authToken import CustomAuthToken

router = routers.DefaultRouter()
# router.register('theme', ThemeViewSet)
router.register('profile', ProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('theme/', include(('hint.urls', 'hint'), namespace='hint')),
    re_path(r'^', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    re_path('api-token-auth/', CustomAuthToken.as_view()),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
