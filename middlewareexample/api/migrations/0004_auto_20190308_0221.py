# Generated by Django 2.1.1 on 2019-03-08 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190308_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expiry',
            name='expirytime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]