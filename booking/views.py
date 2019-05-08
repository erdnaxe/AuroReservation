# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from .models import Tag, Building, Room, Reservation
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
def add(request, room_id):
    """
    Reservation create view
    """
    try:
        room = Room.objects.get(pk=room_id)
    except Room.DoesNotExist:
        raise Http404("Room does not exist")

    context = {
        'title': _('Create a reservation for ') + room.name,
    }

    return render(request, 'booking/add.html', context=context)


@login_required
def edit(request, reservation_id):
    """
    Reservation edit view
    """
    try:
        reservation = Reservation.objects.get(pk=reservation_id)
    except Reservation.DoesNotExist:
        raise Http404("Room does not exist")

    context = {
        'title': _('Edit reservation ') + reservation.purpose_title,
    }

    return render(request, 'booking/edit.html', context=context)


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
    buildings = Building.objects.all()
    data = [{
        "id": f'b{b.id}',
        "title": b.name,
    } for b in buildings]

    rooms = Room.objects.all()
    for r in rooms:
        resource = {
            "id": r.id,
            "title": r.name,
            "comment": r.comment,
            "add_url": reverse('add', args=(r.id,)),
        }
        if r.building:
            resource["parentId"] = f'b{r.building.id}'
        data.append(resource)
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
            start_time__lt=end_time,
            end_time__gt=start_time,
            validation=True,
        )
    else:
        queryset = Reservation.objects.filter(validation=True)

    data = [{
        "resourceId": reservation.room.id,
        "title": reservation.purpose_title,
        "start": reservation.start_time,
        "end": reservation.end_time,
        "url": reverse('edit', args=(reservation.id,)),
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
