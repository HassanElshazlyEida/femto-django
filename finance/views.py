from django.shortcuts import render, redirect ,HttpResponse
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
import datetime

from .forms import GoalForm
from .models import Goal

@login_required
def home(request):
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'finance/home.html', {'goals': goals})

@csrf_exempt
def User_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('finance:home')
    else:
        form = UserCreationForm()
    return render(request, 'finance/register.html', {'form': form})

@csrf_exempt
def User_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('finance:home')
    else:
        form = AuthenticationForm()
    return render(request, 'finance/login.html', {'form': form})

@login_required
def create_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            # Calculate monthly deposit value

            total_amount = goal.total_amount
            goal_date = goal.goal_date
            current_date = datetime.date.today()
            
            months_remaining = (goal_date.year - current_date.year) * 12 + (goal_date.month - current_date.month)
            monthly_deposit = total_amount / months_remaining
          
            goal.total_amount = monthly_deposit
            goal.save()
            return redirect('finance:home')
    else:
        form = GoalForm()
    return render(request, 'finance/create_goal.html', {'form': form})

@login_required
def get_goals(request):
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'finance/goals.html', {'goals': goals})
def logout_view(request):
    logout(request)
    return redirect('finance:home')