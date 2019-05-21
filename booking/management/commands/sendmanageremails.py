# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

from django.core.management.base import BaseCommand

"""
Send one email per manager for pending reservation

This management command should be called daily by a cron.
"""


class Command(BaseCommand):
    help = 'Send one email per manager for pending reservation'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('TODO'))
