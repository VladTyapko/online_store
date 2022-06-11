"""online_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from categories.urls import urlpatterns as categories_urls
from accounts.urls import urlpatterns as accounts_urls
from order.urls import urlpatterns as orders_urls
from api.urls import urlpatterns as api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include((accounts_urls, 'accounts'), namespace='accounts')),
    path('', include((categories_urls, 'categories'), namespace='categories')),
    path('orders/', include((orders_urls, 'orders'), namespace='orders')),
    path('about/', TemplateView.as_view(template_name="about.html"), name="about"),
    path('api/', include((api_urls, 'api'), namespace="api")),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)