from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('category', models.CharField(choices=[('police', 'Police'), ('ambulance', 'Ambulance / Medical'), ('fire', 'Fire Department'), ('highway', 'Highway Patrol / Helpline'), ('women', 'Women Helpline'), ('other', 'Other')], max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('region', models.CharField(blank=True, help_text='e.g. National, or a specific state/city', max_length=100)),
            ],
            options={
                'ordering': ['category', 'name'],
            },
        ),
        migrations.CreateModel(
            name='SafetyTip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('audience', models.CharField(choices=[('driver', 'Drivers'), ('rider', 'Riders'), ('pedestrian', 'Pedestrians'), ('cyclist', 'Cyclists'), ('general', 'Everyone')], default='general', max_length=20)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['audience', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TrafficRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('penalty', models.CharField(blank=True, help_text='Typical penalty / fine, if applicable', max_length=255)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='TrafficSign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('category', models.CharField(choices=[('mandatory', 'Mandatory Sign'), ('cautionary', 'Cautionary / Warning Sign'), ('informatory', 'Informatory Sign')], max_length=20)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='traffic_signs/')),
            ],
            options={
                'ordering': ['category', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('role', models.CharField(choices=[('driver', 'Driver'), ('rider', 'Rider (Two-wheeler)'), ('pedestrian', 'Pedestrian'), ('cyclist', 'Cyclist'), ('admin', 'Administrator')], default='driver', max_length=20)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HazardReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hazard_type', models.CharField(choices=[('pothole', 'Pothole'), ('accident', 'Accident'), ('broken_signal', 'Broken Traffic Signal'), ('damaged_sign', 'Damaged / Missing Sign'), ('waterlogging', 'Waterlogging'), ('debris', 'Debris / Obstruction'), ('streetlight', 'Streetlight Not Working'), ('other', 'Other')], max_length=20)),
                ('location', models.CharField(help_text='Street name, landmark, or coordinates', max_length=255)),
                ('description', models.TextField()),
                ('severity', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('critical', 'Critical')], default='medium', max_length=10)),
                ('status', models.CharField(choices=[('pending', 'Pending Review'), ('verified', 'Verified'), ('in_progress', 'In Progress'), ('resolved', 'Resolved'), ('rejected', 'Rejected')], default='pending', max_length=15)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='hazard_reports/')),
                ('reported_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reported_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hazard_reports', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-reported_at'],
            },
        ),
    ]
