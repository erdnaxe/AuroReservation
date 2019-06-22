# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

from django.test import TestCase

from ..models import Tag, Building


class TagModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Tag.objects.create(name='Test')

    def test_name_label(self):
        tag = Tag.objects.get(id=1)
        field_label = tag._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_object_name_is_name(self):
        tag = Tag.objects.get(id=1)
        self.assertEquals(tag.name, str(tag))


class BuildingModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Building.objects.create(name='Test')

    def test_name_label(self):
        building = Building.objects.get(id=1)
        field_label = building._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_object_name_is_name(self):
        building = Building.objects.get(id=1)
        self.assertEquals(building.name, str(building))
