from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    path('book-list/', views.book_list, name='book-list'),
    path('book-create/', views.book_create, name='book-create'),
    path('book-<str:pk>/', views.book_single, name='book-single_id'),
]