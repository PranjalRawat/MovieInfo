from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import *
from . import views

urlpatterns = [
    url(r'^$',ProductListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',ProductDetailView.as_view(),name='detail'),
    url(r'^create',ProductCreateView.as_view(),name='create'),
    url(r'^(?P<pk>\d+)/update$',ProductUpdateView.as_view(),name='update'),
    url(r'^(?P<pk>\d+)/delete$',ProductDeleteView.as_view(),name='delete'),

    url(r'^hollywood/$',Hollywood.as_view(),name='hollywood'),
    url(r'^bollywood/$',Bollywood.as_view(),name='bollywood'),
    url(r'^tollywood/$',Tollywood.as_view(),name='tollywood'),
    url(r'^animated/$',Animated.as_view(),name='animated'),

    url(r'^login/$',auth_views.LoginView.as_view(template_name='product/login.html'), name='login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(), name='logout'),
    url(r'^signup/$',views.SignUp.as_view(), name='signup'),


]