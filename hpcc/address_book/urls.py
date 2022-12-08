from django.urls import path

from . import views

app_name = "addr_book"
urlpatterns = [
    path('', views.index, name='index'),
    path('edit_user/<int:user_id>', views.edit_user, name='edit'),
    path('edit_user/<int:user_id>/submit', views.edit_user_modify, name='edit_modify')
]
