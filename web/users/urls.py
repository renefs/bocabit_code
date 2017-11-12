from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    url(r'profile/$', views.AccountProfileView.as_view(), name='profile'),
    # url(r'logout/$', views.logout_view, name='logout'),
]