# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, Http404
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import CreateView, UpdateView
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from .forms import ReservationForm
from .models import Tag, Building, Room, Reservation
from .serializers import TagSerializer, RoomSerializer, ReservationSerializer


@login_required
def index(request):
    """
    Index view with the calendar
    """
    context = {'title': _('Home')}
    return render(request, 'booking/index.html', context=context)


class ReservationCreate(LoginRequiredMixin, CreateView):
    """
    View to create a reservation
    """
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Create reservation')
        return context

    def form_valid(self, form):
        """
        Assign user and validation state
        """
        reservation = form.save(commit=False)
        reservation.in_charge = self.request.user
        reservation.validation = None
        return super().form_valid(form)


class ReservationUpdate(LoginRequiredMixin, UpdateView):
    """
    View to edit a reservation
    """
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Edit reservation')

        # Check user own reservation
        reservation = self.object
        if not reservation.in_charge == self.request.user:
            raise Http404

        # Warn user if the validation is already validated
        if reservation.validation:
            messages.add_message(self.request, messages.WARNING,
                                 _('By editing this reservation, '
                                   'it will be unvalidated!'))

        return context

    def form_valid(self, form):
        """
        Assign user and validation state
        """
        reservation = form.save(commit=False)
        reservation.in_charge = self.request.user
        reservation.validation = None
        return super().form_valid(form)


@login_required
def fc_resources(request):
    """
    Returns resources in JSON for FullCalendar
    """
    # Add all buildings
    buildings = Building.objects.all()
    data = [{
        "id": f'b{b.id}',
        "title": b.name,
    } for b in buildings]

    # Add all rooms (with comment and url)
    rooms = Room.objects.all()
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
        queryset = Reservation.objects.filter(
            start_time__lt=end_time,
            end_time__gt=start_time,
        )
    else:
        queryset = Reservation.objects

    data = []

    # Add user reservation
    for reservation in queryset.filter(in_charge=request.user):
        event = {
            'resourceId': reservation.room.id,
            'title': reservation.purpose_title,
            'start': reservation.start_time,
            'end': reservation.end_time,
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
            'start': reservation.start_time,
            'end': reservation.end_time,
        }
        data.append(event)

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
