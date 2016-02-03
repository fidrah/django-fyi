from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^loginscreen', 'userauth.views.loginscreen'),
    url(r'^authenticate', 'userauth.views.authenticatelogin'),
    #url(r'^test', 'userauth.views.testmethod'),
]
