# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
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


@login_required
def fc_resources(request):
    """
    Returns resources in JSON for FullCalendar
    """
    rooms = Room.objects.all()
    data = [{
        "id": r.id,
        "title": r.name,
        "comment": r.comment
    } for r in rooms]
    return JsonResponse(data, safe=False)


@login_required
def fc_events(request):
    """
    Returns events in JSON for FullCalendar

    It returns validated reservations between start and end GET parameters
    """
    start_time = request.GET.get('start')
    end_time = request.GET.get('end')
    if start_time and end_time:
        queryset = Reservation.objects.filter(
            start_time__gt=start_time,
            end_time__lt=end_time,
            validation=True,
        )
    else:
        queryset = Reservation.objects.filter(validation=True)

    data = [{
        "resourceId": reservation.room.id,
        "title": reservation.purpose_title,
        "start": reservation.start_time,
        "end": reservation.end_time,
    } for reservation in queryset]
    return JsonResponse(data, safe=False)


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
