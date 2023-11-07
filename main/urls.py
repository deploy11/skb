from django.urls import path
from .views import *
from .user_views import *

urlpatterns = [
    path('',home,name='home'),
    path('fuqoro/',Fuqoro.as_view(),name='fuqoro'),
    path('tashkilot/',Tashkilot.as_view(),name='tashkilot'),
    # user urls
    path('login/???/',LoginPage,name='login'),
    path('logout/???/',LogoutPage,name='logout'),
]
