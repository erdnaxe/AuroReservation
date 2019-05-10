# -*- coding: utf-8 -*-
from django.contrib import admin
from reversion.admin import VersionAdmin

from .models import Room, Tag, Reservation, Building

from .forms import ReservationAdminForm


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

    def has_ownership(self, user, instance):
        return user in instance.room.managers.all()

    def has_change_permission(self, request, obj=None):
        if obj is not None and self.has_ownership(request.user, obj):
            return True
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj is not None and self.has_ownership(request.user, obj):
            return True
        return super().has_delete_permission(request, obj)
