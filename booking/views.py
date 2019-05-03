from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def index(request):
    context = {
        'title': _('Home'),
    }

    return render(request, 'booking/index.html', context=context)
