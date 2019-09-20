"""tasktracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from accounts import urls as urls_accounts
from accounts.views import IndexView
from blog.views import BlogPostView
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from tasks.views import ArticlesView, ChargeView, PiecesView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^articles/', ArticlesView.as_view(), name='articles'),
    url(r'^charge/', ChargeView.as_view(), name='charge'),
    url(r'^pieces/', PiecesView.as_view(), name='pieces'),
    url(r'^blog/', BlogPostView.as_view(), name='blog'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
