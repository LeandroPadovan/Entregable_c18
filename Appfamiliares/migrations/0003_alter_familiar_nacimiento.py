# Generated by Django 4.1.3 on 2022-12-05 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appfamiliares', '0002_familiar_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='nacimiento',
            field=models.CharField(max_length=10),
        ),
    ]