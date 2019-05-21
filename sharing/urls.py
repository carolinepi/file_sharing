from django.urls import path
from . import views
from sharing.views import print_hello


urlpatterns = [
    path('', views.add_new, name='index'),
    path('my_uploading/', views.show_files, name='my_uploading'),
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/', views.new_page, name='new_page'),
    path('hello/', views.print_hello, name="print_hello")
]

handler404 = views.handler404
print_hello(repeat=10, repeat_until=None)


