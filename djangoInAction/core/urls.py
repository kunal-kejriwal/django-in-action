from django.urls import path
from . import views
urlpatterns = [
    path('', views.core_home),
    path('first-app/', views.first_view),
    path('context/', views.context_template),
]
