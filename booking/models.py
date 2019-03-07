from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from reversion import revisions as reversion

class Room(models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
    )
    comment = models.TextField(
        verbose_name=_('comment'),
    )
    manager = models.ForeignKey(
        User,
        verbose_name=_('manager'),
        on_delete=models.PROTECT,
    )

    class Meta:
        ordering = ['name']
        verbose_name = _('room')
        verbose_name_plural = _('rooms')

    def __str__(self):
        return self.name


class Reservation(models.Model):
    start_time = models.DateTimeField(
        verbose_name=_('start_time'),
    )
    end_time = models.DateTimeField(
        verbose_name=_('end_time'),
    )
    room = models.ForeignKey(
        Room,
        verbose_name=_('room'),
        on_delete=models.PROTECT,
    )
    number_participants = models.IntegerField(
        verbose_name=_('number of participants'),    
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
    )
    in_charges = models.ManyToManyField(
        User,
        verbose_name=_('in charge'),
    )

    class Meta:
        ordering = ['start_time']
        verbose_name = _('reservation')
        verbose_name_plural = _('reservations')

    def __str__(self):
        return str(start_time) + " -> " + str(end_time) + " : " + purpose_title

