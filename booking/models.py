# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    """
    Rooms can be tagged
    """
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
    )

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

    def __str__(self):
        return self.name


class Building(models.Model):
    """
    Represent a physical Building to group rooms
    """
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
    )

    class Meta:
        verbose_name = _('building')
        verbose_name_plural = _('buildings')

    def __str__(self):
        return self.name


class Room(models.Model):
    """
    Represent a room that an user can reserve
    """
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
    )
    comment = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('comment'),
        help_text=_('Describe what is special about this room, '
                    'such as available equipment.'),
    )
    managers = models.ManyToManyField(
        User,
        verbose_name=_('managers'),
        help_text=_('Will manage booking for this room.'),
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        verbose_name=_('tags'),
    )
    building = models.ForeignKey(
        Building,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_('building'),
    )

    class Meta:
        ordering = ['name']
        verbose_name = _('room')
        verbose_name_plural = _('rooms')

    def __str__(self):
        return self.name


class Reservation(models.Model):
    """
    A reservation ticket
    """
    start_time = models.DateTimeField(
        verbose_name=_('start time'),
    )
    end_time = models.DateTimeField(
        verbose_name=_('end time'),
    )
    room = models.ForeignKey(
        Room,
        verbose_name=_('room'),
        on_delete=models.PROTECT,
    )
    number_participants = models.IntegerField(
        verbose_name=_('number of participants'),
        help_text=_('Approximate if unknown.'),
    )
    validation = models.BooleanField(
        verbose_name=_('validation'),
        null=True
    )
    purpose_title = models.CharField(
        verbose_name=_('title'),
        max_length=255,
    )
    purpose_body = models.TextField(
        verbose_name=_('purpose'),
        help_text=_('Specify here if it is for a club.'),
    )
    in_charge = models.ForeignKey(
        User,
        verbose_name=_('in charge'),
        on_delete=models.PROTECT,
    )

    class Meta:
        ordering = ['start_time']
        verbose_name = _('reservation')
        verbose_name_plural = _('reservations')

    def __str__(self):
        return str(self.start_time) + " -> " + str(
            self.end_time) + " : " + self.purpose_title
