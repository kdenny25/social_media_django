# dwitter/urls.py

from django.urls import path
from .views import dashboard, profile_list, profile
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include

app_name = 'dwitter'

urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile_list/', profile_list, name="profile_list"),
    path('profile/<int:pk>', profile, name="profile"),
]

urlpatterns += staticfiles_urlpatterns()