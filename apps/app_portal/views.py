# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def test(req):
    print """
    Boob ya!
    """

def render_portal(req):
    return render(req, 'app_portal/index.html')