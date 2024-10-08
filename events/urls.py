from django.urls import path
from . import views

urlpatterns = [
    path('<int:year>/<int:month>/', views.monthly_view, name='monthly_view'),
    path('wydarzenia/', views.monthly_view, name='monthly_view_default'),  
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('filter/', views.filter_events_by_tag, name='filter_events'),
    path('kalendarz/', views.calendar_view, name='calendar_view'),  
    path('', views.home, name='home'),

]
