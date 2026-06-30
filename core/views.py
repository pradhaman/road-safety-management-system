from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator

from .models import (
    TrafficRule, TrafficSign, SafetyTip, EmergencyContact, HazardReport
)
from .forms import SignUpForm, HazardReportForm, ProfileUpdateForm, UserUpdateForm, StyledAuthenticationForm


def home(request):
    """Landing page with quick stats and highlights."""
    context = {
        'total_reports': HazardReport.objects.count(),
        'resolved_reports': HazardReport.objects.filter(status='resolved').count(),
        'rules_count': TrafficRule.objects.count(),
        'recent_tips': SafetyTip.objects.all()[:3],
    }
    return render(request, 'core/home.html', context)


# ---------- Authentication ----------

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    authentication_form = StyledAuthenticationForm


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}! Your account has been created.")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def profile_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    my_reports = HazardReport.objects.filter(reported_by=request.user)
    return render(request, 'core/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'my_reports': my_reports,
    })


# ---------- Static info sections ----------

def traffic_rules_view(request):
    query = request.GET.get('q', '')
    rules = TrafficRule.objects.all()
    if query:
        rules = rules.filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, 'core/traffic_rules.html', {'rules': rules, 'query': query})


def traffic_signs_view(request):
    category = request.GET.get('category', '')
    signs = TrafficSign.objects.all()
    if category:
        signs = signs.filter(category=category)
    return render(request, 'core/traffic_signs.html', {
        'signs': signs,
        'categories': TrafficSign.CATEGORY_CHOICES,
        'selected_category': category,
    })


def safety_tips_view(request):
    audience = request.GET.get('audience', '')
    tips = SafetyTip.objects.all()
    if audience:
        tips = tips.filter(audience=audience)
    return render(request, 'core/safety_tips.html', {
        'tips': tips,
        'audiences': SafetyTip.AUDIENCE_CHOICES,
        'selected_audience': audience,
    })


def emergency_contacts_view(request):
    contacts = EmergencyContact.objects.all()
    return render(request, 'core/emergency_contacts.html', {'contacts': contacts})


# ---------- Hazard reporting (CRUD) ----------

class HazardListView(ListView):
    model = HazardReport
    template_name = 'core/hazard_list.html'
    context_object_name = 'reports'
    paginate_by = 9

    def get_queryset(self):
        qs = HazardReport.objects.all().select_related('reported_by')
        status = self.request.GET.get('status', '')
        hazard_type = self.request.GET.get('type', '')
        if status:
            qs = qs.filter(status=status)
        if hazard_type:
            qs = qs.filter(hazard_type=hazard_type)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['status_choices'] = HazardReport.STATUS_CHOICES
        ctx['type_choices'] = HazardReport.HAZARD_TYPE_CHOICES
        ctx['selected_status'] = self.request.GET.get('status', '')
        ctx['selected_type'] = self.request.GET.get('type', '')
        return ctx


class HazardDetailView(DetailView):
    model = HazardReport
    template_name = 'core/hazard_detail.html'
    context_object_name = 'report'


class HazardCreateView(LoginRequiredMixin, CreateView):
    model = HazardReport
    form_class = HazardReportForm
    template_name = 'core/hazard_form.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.reported_by = self.request.user
        messages.success(self.request, "Thank you — your report has been submitted and will be reviewed shortly.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('hazard_detail', kwargs={'pk': self.object.pk})


class HazardUpdateView(LoginRequiredMixin, UpdateView):
    model = HazardReport
    form_class = HazardReportForm
    template_name = 'core/hazard_form.html'
    login_url = 'login'

    def get_queryset(self):
        # Users may only edit their own reports.
        return HazardReport.objects.filter(reported_by=self.request.user)

    def get_success_url(self):
        messages.success(self.request, "Report updated successfully.")
        return reverse_lazy('hazard_detail', kwargs={'pk': self.object.pk})


class HazardDeleteView(LoginRequiredMixin, DeleteView):
    model = HazardReport
    template_name = 'core/hazard_confirm_delete.html'
    success_url = reverse_lazy('hazard_list')
    login_url = 'login'

    def get_queryset(self):
        return HazardReport.objects.filter(reported_by=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Report deleted.")
        return super().form_valid(form)
