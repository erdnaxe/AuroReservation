# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from .models import Tag, Room, Reservation
from .serializers import TagSerializer, RoomSerializer, ReservationSerializer


@login_required
def index(request):
    """
    Index view
    """
    context = {
        'title': _('Home'),
    }

    return render(request, 'booking/index.html', context=context)


@login_required
def profile(request):
    """
    User profile view
    """
    context = {
        'title': _('My profile'),
    }

    return render(request, 'booking/profile.html', context=context)


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tags to be viewed or edited.
    """
    permission_classes = (DjangoModelPermissions,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class RoomViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows rooms to be viewed or edited.
    """
    permission_classes = (DjangoModelPermissions,)
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ReservationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows reservations to be viewed or edited.

    It is read-only for security reasons.
    """
    permission_classes = (DjangoModelPermissions,)
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
