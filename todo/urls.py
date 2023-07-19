from django.urls import path
from . import views

urlpatterns = [
    path('', views.sched, name='sched'),
    path('delete/<str:pk>', views.delete, name='delete')
]