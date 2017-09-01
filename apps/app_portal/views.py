# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from forms import UserForm

# Create your views here.
def test(req):
    print """
    Boob ya!
    """

def render_portal(req):
    context = {
        'form' : UserForm(),
    }
    return render(req, 'app_portal/index.html', context)

def process_login(req):
    pass

def process_logout(req):
    pass

def process_reg(req):
    pass