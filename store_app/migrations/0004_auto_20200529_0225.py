# Generated by Django 2.2 on 2020-05-29 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0003_auto_20200529_0217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='user',
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ManyToManyField(null='True', related_name='items', to='store_app.User'),
            preserve_default='True',
        ),
    ]
