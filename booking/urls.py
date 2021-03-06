# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

from django.urls import path

from .views.main import index, ReservationCreate, ReservationUpdate
from .views.fullcalendar import fc_resources, fc_events

urlpatterns = [
    path('', index, name='index'),
    path('reservation/<room>/add', ReservationCreate.as_view(), name='add'),
    path('reservation/<int:pk>', ReservationUpdate.as_view(), name='edit'),

    # API endpoints for FullCalendar
    path('fc/resources.json', fc_resources),
    path('fc/events.json', fc_events),
]
