# Generated by Django 2.1.1 on 2019-03-08 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190308_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expiry',
            name='expirytime',
            field=models.DateField(blank=True, null=True),
        ),
    ]