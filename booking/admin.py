# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

from django.contrib import admin
from reversion.admin import VersionAdmin

from .forms import ReservationAdminForm
from .models import Room, Tag, Reservation, Building


@admin.register(Room)
class RoomAdmin(VersionAdmin, admin.ModelAdmin):
    list_display = ('name', 'building', 'comment',)
    list_filter = ('building', 'tags', 'managers',)
    search_fields = ('name', 'building__name', 'tags__name',)
    autocomplete_fields = ('building', 'tags', 'managers')


@admin.register(Tag)
class TagAdmin(VersionAdmin, admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Building)
class BuildingAdmin(VersionAdmin, admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Reservation)
class ReservationAdmin(VersionAdmin, admin.ModelAdmin):
    form = ReservationAdminForm
    list_display = (
        'purpose_title',
        'validation',
        'room',
        'start_time',
        'end_time',
        'number_participants',
    )
    list_filter = ('start_time', 'end_time', 'room', 'validation',)
    search_fields = ('in_charge__username', 'room__name',)
    autocomplete_fields = ('in_charge', 'room',)

    def has_change_permission(self, request, obj=None):
        """
        Override change permission when user is a manager of the room
        """
        own = obj is not None and request.user in obj.room.managers.all()
        return own or super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        """
        Override delete permission when user is a manager of the room
        """
        own = obj is not None and request.user in obj.room.managers.all()
        return own or super().has_delete_permission(request, obj)
