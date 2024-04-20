from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menuView.as_view(), name='menu'),
    path('menu/<int:pk>', views.singleMenuView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
    
]
