
from django.urls import path
from . import views
urlpatterns = [
    path('', views.apiOverView.as_view(), name='api-overview'),
    path('user-list/', views.userList.as_view(), name='user-list'),
    path('user-create/', views.userCreate.as_view(), name='user-create'),
    path('user-update/<str:pk>/', views.userUpdate.as_view(), name='user-update'),
    path('user-delete/<str:pk>/', views.userDelete.as_view(), name='user-delete'),
    path('user/', views.userDetails.as_view(), name='user')
]
