# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def about(request):
    """
    About view with legal information
    """
    context = {'title': _('About ') + request.site.name}
    return render(request, 'about.html', context=context)
