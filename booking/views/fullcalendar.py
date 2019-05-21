# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later
from django.contrib.auth.decorators import login_required
from django.forms.fields import DateTimeField
from django.http import JsonResponse
from django.urls import reverse
from django.utils import timezone
# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

from django.utils.translation import gettext_lazy as _

from ..models import Building, Room, Reservation

"""
Views specific to FullCalendar

These views generate JSON API endpoints that FullCalendar can use.
"""


@login_required
def fc_resources(request):
    """
    Returns resources in JSON for FullCalendar
    """
    # Add all buildings
    buildings = Building.objects.order_by('name').all()
    data = [{
        "id": f'b{b.id}',
        "title": b.name,
    } for b in buildings]

    # Add all rooms (with comment and url)
    rooms = Room.objects.order_by('name').all()
    for room in rooms:
        resource = {
            'id': room.id,
            'title': room.name,
            'add_url': reverse('add', args=(room.id,)),
        }
        if room.comment:
            resource['comment'] = room.comment
        if room.building:
            resource['parentId'] = f'b{room.building.id}'
        data.append(resource)

    return JsonResponse(data, safe=False)


@login_required
def fc_events(request):
    """
    Returns events in JSON for FullCalendar

    It returns validated reservations between start and end GET parameters
    """
    # Get only events corresponding to the time slot
    start_time = request.GET.get('start')
    end_time = request.GET.get('end')
    if start_time and end_time:
        start = DateTimeField().clean(start_time.replace('T', ' '))
        end = DateTimeField().clean(end_time.replace('T', ' '))
        queryset = Reservation.objects.filter(
            start_time__lt=end,
            end_time__gt=start,
        )
    else:
        queryset = Reservation.objects

    data = []

    # Add user reservation
    for reservation in queryset.filter(in_charge=request.user):
        event = {
            'resourceId': reservation.room.id,
            'title': reservation.purpose_title,
            'start': timezone.localtime(reservation.start_time),
            'end': timezone.localtime(reservation.end_time),
            'url': reverse('edit', args=(reservation.id,)),
        }
        if reservation.validation:
            event['comment'] = _('Validated')
            event['color'] = 'green'
        elif reservation.validation is None:
            event['comment'] = _('Being validated')
            event['color'] = 'black'
        else:
            event['comment'] = _('Denied')
            event['color'] = 'red'
        data.append(event)

    # Add all other reservation
    for reservation in \
            queryset.filter(validation=True).exclude(in_charge=request.user):
        event = {
            'resourceId': reservation.room.id,
            'title': reservation.purpose_title,
            'start': timezone.localtime(reservation.start_time),
            'end': timezone.localtime(reservation.end_time),
        }
        data.append(event)

    return JsonResponse(data, safe=False)
