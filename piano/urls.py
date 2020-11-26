from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page_test', views.page_test, name="example")
]