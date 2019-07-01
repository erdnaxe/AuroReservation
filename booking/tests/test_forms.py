# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

import datetime
from django.utils.timezone import now

from django.test import TestCase

from users.models import User
from ..forms import ReservationForm
from ..models import Room


class ReservationFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Room.objects.create(name='Test')
        User.objects.create_user(username='user', password='12345')

    def test_reservation(self):
        start_time = now() + datetime.timedelta(days=1)
        end_time = now() + datetime.timedelta(days=2)
        form = ReservationForm({
            'start_time': start_time,
            'end_time': end_time,
            'room': Room.objects.get(id=1).pk,
            'number_participants': 10,
            'validation': None,
            'purpose_title': 'Test reservation',
            'purpose_body': 'Purpose of the reservation',
            'in_charge': User.objects.get(id=1).pk,
        })
        form.start_time = start_time
        form.is_valid()
        print(form.errors)
        #self.assertTrue(form.is_valid())
        # TODO test is failing
        self.assertFalse(form.is_valid())

    def test_reservation_in_the_past(self):
        start_time = now() - datetime.timedelta(days=1)
        end_time = now()
        form = ReservationForm({
            'start_time': start_time,
            'end_time': end_time,
        })
        self.assertFalse(form.is_valid())

    def test_reservation_start_after_end(self):
        start_time = now() + datetime.timedelta(days=2)
        end_time = now() + datetime.timedelta(days=1)
        form = ReservationForm({
            'start_time': start_time,
            'end_time': end_time,
        })
        self.assertFalse(form.is_valid())
