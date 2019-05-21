# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

from rest_framework import routers

from booking.views.api import TagViewSet, RoomViewSet, ReservationViewSet
from users.views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()

# users app
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

# booking app
router.register(r'tags', TagViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = router.urls
