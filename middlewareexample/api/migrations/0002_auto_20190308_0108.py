# Generated by Django 2.1.1 on 2019-03-08 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expiry',
            name='expirytime',
            field=models.DateField(blank=True),
        ),
    ]
