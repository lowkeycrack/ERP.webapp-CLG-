# Generated by Django 3.2.19 on 2023-09-09 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField()),
                ('location', models.CharField(max_length=255)),
                ('event_image', models.ImageField(blank=True, null=True, upload_to='event_images/')),
                ('registration_deadline', models.DateField(blank=True, null=True)),
                ('max_participants', models.PositiveIntegerField(blank=True, null=True)),
                ('event_type', models.CharField(max_length=100)),
                ('tags', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('additional_information', models.TextField(blank=True, null=True)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organized_events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]