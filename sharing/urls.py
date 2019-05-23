from django.urls import path
from . import views


urlpatterns = [
    path('', views.add_new, name='index'),
    path('my_uploading/', views.show_files, name='my_uploading'),
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/', views.file_page, name='file_page'),
    path('accounts/login/', views.log_in, name="log_in"),
]

handler404 = views.handler404
