# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import hashers
from forms import UserForm
from models import User

# Create your views here.
def test(req):
    print """
    Boob ya!
    """

def render_portal(req):
    context = {}
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            print """
            Boob ya!
            """
            auth_user = check_user(form)
            if auth_user[1]:
                # Log this sucka in!
                print """
                It's a Rick and Mordy Adventure
                """
                pass
            elif auth_user[0]:
                # Tell them their email is registered,
                # But the password is wrong
                print """
                I was not in control of that situation
                """
                pass
            else:
                # Offer registration
                print """
                Don't even trip
                """
                pass
        else:
            # If the form isn't valid, it will save errors.
            # We can then just pass the form back to the view
            print form.errors.as_data()
    else:
        # If we got here through a get method, send a blank form
        form = UserForm()
    
    context['form'] = form
    return render(req, 'app_portal/index.html', context)   

def check_user(form_object):
    form_email = form_object.cleaned_data.get('email')
    form_password = form_object.cleaned_data.get('password')
    try:
        user = User.objects.get(email=form_email)
        return (True, hashers.check_password(form_password, user.password))
    except:
        return (False, False)

def process_login(req):
    pass

def process_logout(req):
    pass

def process_reg(req):
    pass