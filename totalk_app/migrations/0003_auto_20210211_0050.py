# Generated by Django 2.2.14 on 2021-02-10 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('totalk_app', '0002_invitation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='totalk_app.Profile'),
        ),
    ]