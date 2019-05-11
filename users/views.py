# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from .serializers import UserSerializer, GroupSerializer


@login_required
def profile(request):
    """
    User profile view
    """
    context = {'title': _('My profile')}
    return render(request, 'users/profile.html', context=context)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (DjangoModelPermissions,)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = (DjangoModelPermissions,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
