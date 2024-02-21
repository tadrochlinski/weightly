from django.urls import path
from .views import dashboard_view, logout_view, settings_view, add_weight_view, delete_weight_entry


urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('settings/', settings_view, name='settings'),
    path('add-weight/', add_weight_view, name='add_weight'),
    path('delete_weight_entry/<int:entry_id>/', delete_weight_entry, name='delete_weight_entry'),
]
