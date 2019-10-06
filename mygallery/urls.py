from django.urls import path, re_path
from . import views


urlpatterns = [
  
    re_path('images/',views.index, name = 'home'),
    path('',views.landing, name = 'landing'),
    path('aboretum', views.aboretum_images, name = "aboretum"),
    path('nature', views.nature_images, name = "nature"),
    re_path('^search/',views.search_results, name = 'search_results'),
]