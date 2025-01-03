from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.portfolio_view, name='portfolio'),
    path('create/', views.create_project, name='create_portfolio'),
    # path('/static', include('../static')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)