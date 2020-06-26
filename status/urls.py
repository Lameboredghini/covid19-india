from django.urls import path
from . import views

urlpatterns=[
    path('',views.HomeView.as_view(),name='home'),
    path('about/',views.about,name='about'),
    path('about-dark/',views.about_dark,name='about-dark'),
]