from django.urls import path
from .views import theme_detail_update_delete
from .views import theme_list_create


urlpatterns = [
    path('', theme_list_create, name='article_list_create'),
    path('<int:theme_pk>/', theme_detail_update_delete, name='article_detail_update_delete'),
]