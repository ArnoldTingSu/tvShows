from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_shows),
    path('shows', views.all_shows),
    path('shows/', views.all_shows),
    path('shows/new', views.new),
    path('shows/create', views.create),
    path('shows/<int:show_id>/edit', views.edit),
    path('shows/<int:show_id>/update', views.update),
    path('shows/<int:show_id>/delete', views.delete),
    path('shows/<int:show_id>', views.show_details)
]