from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('wine/', views.wine_list, name='wine_list'),
    path('review/<int:pk>/', views.review_detail, name='review_detail'),
    path('wine/<int:pk>', views.wine_detail, name='wine_detail'), 
]