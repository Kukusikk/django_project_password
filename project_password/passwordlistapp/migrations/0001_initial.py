# Generated by Django 3.2.3 on 2021-06-24 23:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passw', models.CharField(max_length=250)),
                ('title', models.TextField()),
                ('deleted', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('running', 'running'), ('deprovision', 'deprovision')], default='running', max_length=27)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passws', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
