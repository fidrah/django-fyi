from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    #url(r'^test', 'userauth.views.testmethod'),
    url(r'^search/products', 'inventory.views.searchproductscreen'),
    url(r'^search/loadpage/(?P<pagenumber>[0-9]+)/(?P<filter>.+)', 'inventory.views.returnproductpage'),
    url(r'^search/product/manage/(?P<productid>[0-9]+)', 'inventory.views.modifyproductscreen'),
    url(r'^modify/product', 'inventory.views.modifyproductaction'),
]
