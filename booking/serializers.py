# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

from rest_framework import serializers

from .models import Tag, Room, Reservation


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('url', 'name',)


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    """
    Do not show managers for privacy reasons
    """

    class Meta:
        model = Room
        fields = ('url', 'name', 'comment', 'tags')


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
        fields = ('url', 'start_time', 'end_time', 'room',
                  'number_participants', 'validation', 'purpose_title',
                  'purpose_body', 'in_charge')
