# Generated by Django 2.2.1 on 2020-05-14 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='qid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
