from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    """Extra info attached to each registered user."""
    ROLE_CHOICES = [
        ('driver', 'Driver'),
        ('rider', 'Rider (Two-wheeler)'),
        ('pedestrian', 'Pedestrian'),
        ('cyclist', 'Cyclist'),
        ('admin', 'Administrator'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='driver')
    city = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class TrafficSign(models.Model):
    """A traffic sign or symbol with explanation, for the signs guide page."""
    CATEGORY_CHOICES = [
        ('mandatory', 'Mandatory Sign'),
        ('cautionary', 'Cautionary / Warning Sign'),
        ('informatory', 'Informatory Sign'),
    ]

    name = models.CharField(max_length=150)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='traffic_signs/', blank=True, null=True)

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return self.name


class SafetyTip(models.Model):
    """A safety tip targeted at a specific category of road user."""
    AUDIENCE_CHOICES = [
        ('driver', 'Drivers'),
        ('rider', 'Riders'),
        ('pedestrian', 'Pedestrians'),
        ('cyclist', 'Cyclists'),
        ('general', 'Everyone'),
    ]

    title = models.CharField(max_length=200)
    audience = models.CharField(max_length=20, choices=AUDIENCE_CHOICES, default='general')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['audience', '-created_at']

    def __str__(self):
        return self.title


class TrafficRule(models.Model):
    """A traffic rule / regulation entry for the awareness section."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    penalty = models.CharField(max_length=255, blank=True, help_text="Typical penalty / fine, if applicable")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class EmergencyContact(models.Model):
    """Emergency / helpline contact info shown to all users."""
    CATEGORY_CHOICES = [
        ('police', 'Police'),
        ('ambulance', 'Ambulance / Medical'),
        ('fire', 'Fire Department'),
        ('highway', 'Highway Patrol / Helpline'),
        ('women', 'Women Helpline'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=150)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    phone_number = models.CharField(max_length=20)
    description = models.CharField(max_length=255, blank=True)
    region = models.CharField(max_length=100, blank=True, help_text="e.g. National, or a specific state/city")

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} ({self.phone_number})"


class HazardReport(models.Model):
    """A road hazard or accident report submitted by a user."""
    HAZARD_TYPE_CHOICES = [
        ('pothole', 'Pothole'),
        ('accident', 'Accident'),
        ('broken_signal', 'Broken Traffic Signal'),
        ('damaged_sign', 'Damaged / Missing Sign'),
        ('waterlogging', 'Waterlogging'),
        ('debris', 'Debris / Obstruction'),
        ('streetlight', 'Streetlight Not Working'),
        ('other', 'Other'),
    ]

    SEVERITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending Review'),
        ('verified', 'Verified'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('rejected', 'Rejected'),
    ]

    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hazard_reports')
    hazard_type = models.CharField(max_length=20, choices=HAZARD_TYPE_CHOICES)
    location = models.CharField(max_length=255, help_text="Street name, landmark, or coordinates")
    description = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES, default='medium')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    photo = models.ImageField(upload_to='hazard_reports/', blank=True, null=True)
    reported_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-reported_at']

    def __str__(self):
        return f"{self.get_hazard_type_display()} at {self.location}"

    def get_absolute_url(self):
        return reverse('hazard_detail', kwargs={'pk': self.pk})

    def severity_badge_class(self):
        """Used in templates to colour-code severity badges."""
        return {
            'low': 'success',
            'medium': 'warning',
            'high': 'danger',
            'critical': 'dark',
        }.get(self.severity, 'secondary')

    def status_badge_class(self):
        return {
            'pending': 'secondary',
            'verified': 'info',
            'in_progress': 'warning',
            'resolved': 'success',
            'rejected': 'danger',
        }.get(self.status, 'secondary')
