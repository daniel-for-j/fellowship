# Generated by Django 5.0.2 on 2024-09-28 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_audiomessage_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimony',
            name='testimony',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='testimony',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
