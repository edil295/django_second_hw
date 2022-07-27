from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_item, name='item'),
    path('<int:item_id>/', views.detail_item, name='detail'),
    path('greetings/', views.greetings),
]