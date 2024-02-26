# Generated by Django 3.2.23 on 2024-02-25 02:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posters', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('amended_at', models.DateField(auto_now=True)),
                ('user_displayed_name', models.CharField(blank=True, max_length=40)),
                ('title', models.CharField(max_length=80)),
                ('content', models.TextField()),
                ('rating', models.PositiveIntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posters.poster')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]