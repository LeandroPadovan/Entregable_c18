# Generated by Django 4.1.3 on 2022-12-05 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appfamiliares', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='nacimiento',
            field=models.DateField(auto_now=True),
        ),
    ]
