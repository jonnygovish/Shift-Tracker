from django.shortcuts import render,redirect
from .forms import EmployeeProfileForm,UserForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Shift,Employee_profile
from django.db import transaction

# Create your views here.
def index(request):
  shifts= Shift.get_shift()
  return render(request, 'index.html',{"shifts":shifts})


def update_profile(request, username):
  user = User.objects.get(username = username)
  if request.method == 'POST':
    user_form = UserForm(request.POST, instance = request.user)
    profile_form = EmployeeProfileForm(request.POST, instance = request.user.employee_profile,files =request.FILES)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request, ('Your profile was successfully updated!'))
      return redirect(reverse('profile', kwargs={'username': request.user.username}))
    else:
      messages.error(request, ('Please correct the error below.'))
  else:
    user_form = UserForm(instance = request.user)
    profile_form = EmployeeProfileForm(instance = request.user.employee_profile)
  return render(request, 'profiles/profile.html', {"user_form": user_form,"profile_form": profile_form})


@transaction.atomic
@login_required
def profile(request, username):
  user = User.objects.get(username = username)
  if not user:
    return redirect('Home')
  profile = Employee_profile.objects.get(user =user)
  if request.method == 'POST':
    user_form = UserForm(request.POST, instance = request.user)
    profile_form = EmployeeProfileForm(request.POST, instance=request.user.employee_profile,files =request.FILES)
    if user_form.is_valid() and  profile_form.is_valid:
      user_form.save()
      print('booya!')
      profile_form.save()
      print('success')
      messages.success(request, ('Your profile was successfully updated!'))
      return redirect(reverse('profile', kwargs={'username': request.user.username}))
    else:
      messages.error(request, ('Please correct the error below.'))
  else:
    user_form = UserForm(instance = request.user)
    profile_form = EmployeeProfileForm(instance = request.user.employee_profile)


  title = f"{user.username}"
  return render(request, 'profiles/profile.html', {"title": title, "user":user, "profile":profile,"user_form": user_form,"profile_form": profile_form})

def employees(request):
  users= User.objects.all()
  employees = Employee_profile.objects.all()

  return render(request, 'employee.html', {"users":users, "employees":employees})




