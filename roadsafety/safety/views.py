from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import TrafficRule, TrafficSign, HazardReport, EmergencyContact, SafetyTip
from .forms import RegisterForm, HazardReportForm


def home(request):
    tips = SafetyTip.objects.all()[:6]
    contacts = EmergencyContact.objects.all()
    return render(request, 'safety/home.html', {'tips': tips, 'contacts': contacts})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}! Account created successfully.')
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'safety/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'safety/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


@login_required
def dashboard(request):
    reports = HazardReport.objects.filter(user=request.user).order_by('-reported_at')[:5]
    total_reports = HazardReport.objects.filter(user=request.user).count()
    return render(request, 'safety/dashboard.html', {
        'reports': reports,
        'total_reports': total_reports,
    })


def traffic_rules(request):
    category = request.GET.get('category', '')
    rules = TrafficRule.objects.all()
    if category:
        rules = rules.filter(category=category)
    return render(request, 'safety/traffic_rules.html', {'rules': rules, 'selected': category})


def traffic_signs(request):
    sign_type = request.GET.get('type', '')
    signs = TrafficSign.objects.all()
    if sign_type:
        signs = signs.filter(sign_type=sign_type)
    return render(request, 'safety/traffic_signs.html', {'signs': signs, 'selected': sign_type})


@login_required
def report_hazard(request):
    if request.method == 'POST':
        form = HazardReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            messages.success(request, 'Hazard reported successfully! Thank you for keeping roads safe.')
            return redirect('my_reports')
    else:
        form = HazardReportForm()
    return render(request, 'safety/report_hazard.html', {'form': form})


@login_required
def my_reports(request):
    reports = HazardReport.objects.filter(user=request.user).order_by('-reported_at')
    return render(request, 'safety/my_reports.html', {'reports': reports})


def emergency_contacts(request):
    contacts = EmergencyContact.objects.all()
    return render(request, 'safety/emergency.html', {'contacts': contacts})


def safety_tips(request):
    drivers = SafetyTip.objects.filter(audience='driver')
    riders = SafetyTip.objects.filter(audience='rider')
    pedestrians = SafetyTip.objects.filter(audience='pedestrian')
    return render(request, 'safety/safety_tips.html', {
        'drivers': drivers, 'riders': riders, 'pedestrians': pedestrians
    })
