# Generated by Django 4.1.9 on 2023-11-11 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='jins',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
