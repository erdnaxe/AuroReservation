from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


@login_required
def index(request):
    context = {
        'title': _('Home'),
    }

    return render(request, 'booking/index.html', context=context)


@login_required
def profile(request):
    context = {
        'title': _('My profile'),
    }

    return render(request, 'booking/profile.html', context=context)
