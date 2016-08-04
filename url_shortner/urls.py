"""url_shortner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from urlbook.views import IndexView, BookMarkListView, SignUpView, CreateBookMarkView, ClickListView,\
 MyBookMarkView, BookMarkUpdateView, BookMarkDeleteView, BookMarkDetailView, MyBookMarkRedirectView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^signup/$', SignUpView.as_view(), name='sign_up_view'),
    url(r'^login/$', login, name="login_view"),
    url(r'^logout/$', logout, name="logout_view"),
    url(r'^template/$', BookMarkListView.as_view(), name="bookmark_template_view"),
    url(r'^template/(?P<pk>\d+)/$', BookMarkDetailView.as_view(), name='bookmark_detail_view'),
    url(r'^template/(?P<url>\d+)/$', MyBookMarkRedirectView.as_view(),name='my_bookmark_redirect_view'),
    url(r'^bookmark/$',CreateBookMarkView.as_view(), name="create_bookmark_view"),
    url(r'^bookmark_update/(?P<pk>\d+)$', BookMarkUpdateView.as_view(), name="bookmark_update"),
    url(r'^bookmark_delete/(?P<pk>\d+)$', BookMarkDeleteView.as_view(), name="bookmark_delete"),
    url(r'^mybookmarks/$', MyBookMarkView.as_view(), name="my_bookmark_view"),
    url(r'^click/$', ClickListView.as_view(), name="click_list_view")

    ]
