# Generated by Django 3.0.3 on 2020-05-08 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200508_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='state',
            field=models.CharField(choices=[('private', 'private'), ('public', 'public')], default='public', max_length=35),
        ),
    ]
