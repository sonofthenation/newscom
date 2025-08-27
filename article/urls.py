from django.urls import path
from article import views

urlpatterns=[
    path('',views.get_all,name='home'),
    path('detail/<int:pk>/',views.get_detail,name='detail'),
]