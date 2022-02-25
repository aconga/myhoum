from django.urls import path, include
from position.api import views

urlpatterns = [
    path('', views.PropertyList.as_view(), name='position-list'),
    path('<int:id>/', views.PropertyDetail.as_view(), name='position-detail'),
    path('details', views.PropertyInfoList.as_view(), name='positiondetail-list'),

]