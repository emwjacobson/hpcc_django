from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:user_id>', views.edit_user, name='edit')
]