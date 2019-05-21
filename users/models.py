# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    """
    An user profile

    We do not want to patch the Django Contrib Auth User class
    so this model add an user profile with additional information.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    phone_number = models.CharField(
        max_length=255,
        verbose_name=_('phone number'),
    )

    class Meta:
        verbose_name = _('user profile')
        verbose_name_plural = _('user profile')

    def __str__(self):
        return self.user.get_username()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **_kwargs):
    """Hook to save an user profile when an user is updated"""
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
