# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

from django.urls import path

from .views import profile

urlpatterns = [
    path('profile/', profile, name='profile'),
]
