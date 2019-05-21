# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from ..models import Tag, Room, Reservation
from ..serializers import TagSerializer, RoomSerializer, ReservationSerializer


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
