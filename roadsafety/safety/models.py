from django.db import models
from django.contrib.auth.models import User


class TrafficRule(models.Model):
    CATEGORY_CHOICES = [
        ('general', 'General Rules'),
        ('highway', 'Highway Rules'),
        ('pedestrian', 'Pedestrian Rules'),
        ('cyclist', 'Cyclist Rules'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='general')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TrafficSign(models.Model):
    SIGN_TYPE_CHOICES = [
        ('mandatory', 'Mandatory Signs'),
        ('cautionary', 'Cautionary Signs'),
        ('informatory', 'Informatory Signs'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField()
    sign_type = models.CharField(max_length=50, choices=SIGN_TYPE_CHOICES, default='mandatory')
    emoji = models.CharField(max_length=10, default='🚦')

    def __str__(self):
        return self.name


class HazardReport(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('resolved', 'Resolved'),
    ]
    HAZARD_TYPE_CHOICES = [
        ('pothole', 'Pothole'),
        ('accident', 'Accident'),
        ('flooding', 'Road Flooding'),
        ('construction', 'Road Construction'),
        ('signal', 'Broken Signal'),
        ('other', 'Other'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    hazard_type = models.CharField(max_length=50, choices=HAZARD_TYPE_CHOICES, default='other')
    location = models.CharField(max_length=300)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} — {self.location}"


class EmergencyContact(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    emoji = models.CharField(max_length=10, default='📞')

    def __str__(self):
        return self.name


class SafetyTip(models.Model):
    AUDIENCE_CHOICES = [
        ('driver', 'Drivers'),
        ('rider', 'Riders'),
        ('pedestrian', 'Pedestrians'),
    ]
    tip = models.TextField()
    audience = models.CharField(max_length=50, choices=AUDIENCE_CHOICES, default='driver')

    def __str__(self):
        return self.tip[:60]
