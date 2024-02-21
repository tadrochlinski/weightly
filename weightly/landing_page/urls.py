from django.urls import path
from .views import landing_page_view, login_view, register_view
from dashboard.views import dashboard_view

urlpatterns = [
    path('', landing_page_view, name='landing_page'),
    path('login/', login_view, name='login'),
    path('signup/', register_view, name='signup'),
    path('dashboard/', dashboard_view, name='dashboard'),
]