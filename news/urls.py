from django.urls import path
from . import views

urlpatterns = [
    path('service/', views.services_all, name='service'),
    path('service/<int:id>', views.services_more, name='more'),
    path('contacts/', views.data, name='contacts'),
    path('news', views.novelty, name='news'),
]
