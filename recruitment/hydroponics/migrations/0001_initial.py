# Generated by Django 4.1.13 on 2025-02-23 13:50

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
            name='HydroponicSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='hydroponic_systems', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph', models.DecimalField(decimal_places=2, max_digits=4)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('tds', models.DecimalField(decimal_places=2, max_digits=6)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('hydroponic_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='hydroponics.hydroponicsystem')),
            ],
        ),
    ]
