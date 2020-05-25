# Generated by Django 2.2.5 on 2020-03-31 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200329_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='insights_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_insights_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
