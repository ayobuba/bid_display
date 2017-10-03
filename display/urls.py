from django.conf.urls import url
from . import views

app_name = 'display'

urlpatterns = [
    url(r'^$', views.DisplayView.as_view(),name='home'),


]





