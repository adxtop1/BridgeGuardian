# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import ugettext as _


# Create your views here.


def index(request):
    return render(request, 'base.html', {})