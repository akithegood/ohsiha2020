from django.urls import path
from . import views

app_name = 'kegs'

urlpatterns = [
  path('beers', views.beer_list, name='beer_list'),
  path('kegs', views.keg_list, name='keg_list'),
  path('beers/new', views.beer_create, name='beer_new'),
  path('kegs/new', views.keg_create, name='keg_new'),
  path('beers/edit/<int:pk>', views.beer_update, name='beer_edit'),
  path('kegs/edit/<int:pk>', views.keg_update, name='keg_edit'),
  path('beers/delete/<int:pk>', views.beer_delete, name='beer_delete'),
  path('kegs/delete/<int:pk>', views.keg_delete, name='keg_delete'),
]