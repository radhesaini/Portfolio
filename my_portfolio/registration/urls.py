from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.registration, name='registration'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create_home_page/', views.create_home_page, name='create_home_page'),
    path('update_home_page/<int:pk>/', views.update_home_page, name='update_home_page'),
    path('delete_home_page/<int:pk>/', views.delete_home_page, name='delete_home_page'),
    path('create_carousel_image/', views.create_carouseImage, name='create_carousel_image'),
    path('update_carousel_image/<int:pk>/', views.update_carouseImage, name='update_carousel_image'),
    path('delete_carousel_image/<int:pk>/', views.delete_carouseImage, name='delete_carousel_image'),
    path('create_journey_highlight/', views.create_journeyHighlight, name='create_journey_highlight'),
    path('update_journey_highlight/<int:pk>/', views.update_journeyHighlight, name='update_journey_highlight'),
    path('delete_journey_highlight/<int:pk>/', views.delete_journeyHighlight, name='delete_journey_highlight'),
] 