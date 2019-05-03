# -*- coding: utf-8 -*-
from django.contrib import admin
from reversion.admin import VersionAdmin

from .models import Room, Tag, Reservation


@admin.register(Room)
class RoomAdmin(VersionAdmin, admin.ModelAdmin):
    list_display = ('name', 'comment',)
    list_filter = ('tags', 'managers',)
    search_fields = ('name', 'tags__name',)
    autocomplete_fields = ('tags', 'managers')


@admin.register(Tag)
class TagAdmin(VersionAdmin, admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Reservation)
class ReservationAdmin(VersionAdmin, admin.ModelAdmin):
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
        return user == instance.in_charge or (user in instance.room.managers)

    def has_change_permission(self, request, obj=None):
        if obj is not None and self.has_ownership(request.user, obj):
            return True
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj is not None and self.has_ownership(request.user, obj):
            return True
        return super().has_delete_permission(request, obj)
