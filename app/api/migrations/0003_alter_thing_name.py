# Generated by Django 4.0.4 on 2022-04-27 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_thing_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]