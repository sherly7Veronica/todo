from django.urls import path, include
from django.conf import settings
from . import views
from .views import *
from django.conf.urls.static import static
from django.contrib.auth import views as auth


urlpatterns = [
		path('', views.index, name ='index'),
		path('api/', TaskViewSet.as_view({'get': 'list'})),
        ##### user related path##########################
		path('login/', Login, name ='login'),
		path('logout/', auth.LogoutView.as_view(template_name ='user/index.html'), name ='logout'),
		path('register/', register, name ='register'),
]

