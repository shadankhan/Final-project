# Generated by Django 2.2.14 on 2021-02-12 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('totalk_app', '0003_auto_20210211_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='profile',
            field=models.ForeignKey(blank=True, default=2, on_delete=django.db.models.deletion.CASCADE, to='totalk_app.Profile'),
            preserve_default=False,
        ),
    ]