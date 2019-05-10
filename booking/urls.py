# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

from django.urls import path

from .views import index, add, ReservationUpdate, profile, fc_resources, \
    fc_events

urlpatterns = [
    path('', index, name='index'),
    path('reservation/<int:room_id>/add', add, name='add'),
    path('reservation/<int:pk>', ReservationUpdate.as_view(), name='edit'),
    path('accounts/profile/', profile, name='profile'),

    # API endpoints for FullCalendar
    path('fc/resources.json', fc_resources),
    path('fc/events.json', fc_events),
]
