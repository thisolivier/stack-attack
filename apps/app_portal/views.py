# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import hashers
from django.contrib import messages
from forms import UserForm, RegisterInstructorForm, RegisterStudentForm
from models import User

# Create your views here.
def test(req):
    print """
    Boob ya!
    """

def render_portal(req):
    context = {}
    if req.method == 'POST':
        form = UserForm(req.POST, skip_email=True)
        if form.is_valid():
            print """
            Boob ya!
            """
            auth_user = check_user(form)
            if auth_user[1]:
                # Log this sucka in!
                req.session['user'] = User.objects.get(email=form.cleaned_data.get('email')).id
                return redirect('/dashboard')
            elif auth_user[0]:
                # Tell them their email is registered,
                # But the password is wrong
                messages.error(req, "Email is registered, bad password. Instructors can reset passwords.")
            else:
                # Offer registration
                messages.success(req, 'Email not yet registered, initiate yourself.')
                form = UserForm(initial={'email':form.cleaned_data.get('email')}, c_pass=(True, False))
                form.password = "boob"
                context['form2'] = RegisterStudentForm()
                context['form3'] = RegisterInstructorForm()
        
        # If the form isn't valid, it will save errors by default.
        # We can then just pass the form back to the view
            
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

def process_reg(req, methods=['POST']):
    # Split the form up - DONE
    # Run validators
    # If valid
        # Create user
        # Login
        # Send to dashboard
    # Else
        # Add form to session
        # Redirect to portal
        # Refactor portal
    
    

    user_form = {
        'email' : req.POST['email'],
        'pass' : req.POST['password'],
        'c_pass' : req.POST['c_password'],
        'c_world' : 'fishy'
    }
    failed = False

    if req.POST['user_type'] == 'student':
        stu_form = {
            'f_name' : req.POST['first_name'],
            'l_name' : req.POST['first_name'],
        }
    elif req.POST['user_type'] == 'instructor':
        itr_form = {
            'name' : req.POST['name'],
            'code' : req.POST['code'],
        }
    else:
        messages.error(req, "Are you student or instructor, I cannot tell.")
        failed = True

    if failed:
        return redirect('/portal')