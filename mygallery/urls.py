from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path('home/',views.index, name = 'home'),
    re_path('^search/',views.search_results, name = 'search_results'),
]