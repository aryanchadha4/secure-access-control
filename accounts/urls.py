from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('unauthorized/', views.unauthorized_view, name='unauthorized'),
    path('logout/', views.logout_view, name='logout'),
    path('logs/', views.view_logs, name='view_logs'),
]
