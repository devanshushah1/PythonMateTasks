# Generated by Django 3.1.5 on 2021-01-11 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0003_auto_20210110_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shift',
            name='weekdays',
            field=models.CharField(max_length=50),
        ),
    ]