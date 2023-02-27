from django.urls import path
from . import views

urlpatterns = [
    path('', views.start),
    path('item/<int:id>', views.one_item, name='items-detail'),
]