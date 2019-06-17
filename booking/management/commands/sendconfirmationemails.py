# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

"""
Send all pending confirmation emails

This management command should be called frequently by a cron.
It sends a email to make user confirm a reservation one day before the event.
"""

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Send all pending confirmation emails'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('TODO'))
