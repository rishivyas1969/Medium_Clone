# Generated by Django 3.0.3 on 2020-08-08 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200809_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved_comment',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]