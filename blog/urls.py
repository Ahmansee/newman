from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.index,  name='index'),
    path('contactUs', views.info, name='contacts'),
    path('category', views.catagory,  name='catagory'),
    path('singleBlog', views.singleblog,  name='singleblog')
]
