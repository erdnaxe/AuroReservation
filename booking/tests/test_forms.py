# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

import datetime

from django.test import TestCase

from ..forms import ReservationForm


class ReservationFormTest(TestCase):
    def test_reservation_in_the_past(self):
        start_time = datetime.datetime.now() - datetime.timedelta(days=1)
        end_time = datetime.datetime.now()
        form = ReservationForm(data={
            'start_time': start_time,
            'end_time': end_time,
        })
        self.assertFalse(form.is_valid())

    def test_reservation_start_after_end(self):
        start_time = datetime.datetime.now() + datetime.timedelta(days=2)
        end_time = datetime.datetime.now() + datetime.timedelta(days=1)
        form = ReservationForm(data={
            'start_time': start_time,
            'end_time': end_time,
        })
        self.assertFalse(form.is_valid())
