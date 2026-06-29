from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('traffic-rules/', views.traffic_rules, name='traffic_rules'),
    path('traffic-signs/', views.traffic_signs, name='traffic_signs'),
    path('report-hazard/', views.report_hazard, name='report_hazard'),
    path('my-reports/', views.my_reports, name='my_reports'),
    path('emergency-contacts/', views.emergency_contacts, name='emergency_contacts'),
    path('safety-tips/', views.safety_tips, name='safety_tips'),
]
