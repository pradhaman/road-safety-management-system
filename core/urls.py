from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Auth
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),

    # Info sections
    path('traffic-rules/', views.traffic_rules_view, name='traffic_rules'),
    path('traffic-signs/', views.traffic_signs_view, name='traffic_signs'),
    path('safety-tips/', views.safety_tips_view, name='safety_tips'),
    path('emergency-contacts/', views.emergency_contacts_view, name='emergency_contacts'),

    # Hazard reporting
    path('reports/', views.HazardListView.as_view(), name='hazard_list'),
    path('reports/new/', views.HazardCreateView.as_view(), name='hazard_create'),
    path('reports/<int:pk>/', views.HazardDetailView.as_view(), name='hazard_detail'),
    path('reports/<int:pk>/edit/', views.HazardUpdateView.as_view(), name='hazard_edit'),
    path('reports/<int:pk>/delete/', views.HazardDeleteView.as_view(), name='hazard_delete'),
]
