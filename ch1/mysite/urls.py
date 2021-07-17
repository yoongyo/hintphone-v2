from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers
# from theme.views import ThemeViewSet
from accounts.views import ProfileViewSet
from django.conf import settings
from django.conf.urls.static import static
from .authToken import CustomAuthToken
from . import views

router = routers.DefaultRouter()
# router.register('theme', ThemeViewSet)
router.register('profile', ProfileViewSet)

urlpatterns = [
    re_path(r'^$', views.signin, name="login"),
    path('admin/', admin.site.urls),
    path('api/theme/', include(('hint.urls', 'hint'), namespace='hint')),
    re_path(r'^api/', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    re_path('api-token-auth/', CustomAuthToken.as_view()),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^logout/$', views.logout, name='logout'),
    re_path(r'^(?P<user_id>\w+)/$', views.theme_list, name='theme_list'),
    re_path(r'^(?P<user_id>\w+)/(?P<theme>[\w|\W]+)/edit/$', views.theme_edit, name='theme_edit'),
    re_path(r'^(?P<user_id>\w+)/(?P<theme>[\w|\W]+)/ajax/$', views.ajax, name='ajax'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
