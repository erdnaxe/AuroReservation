# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

"""Project URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from .views import about

urlpatterns = [
    path('', include('booking.urls')),
    path('accounts/', include('users.urls')),
    path('about/', about, name='about'),
    path('api/', include('api.urls')),

    # Include Django Contrib and Core routers
    # admin/login/ is redirected to the non-admin login page
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/login/', RedirectView.as_view(pattern_name='login')),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
]
