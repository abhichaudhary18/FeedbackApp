# Generated by Django 3.0.3 on 2020-05-13 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0003_sendmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendmessage',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='sendmessage',
            name='meme',
            field=models.ImageField(upload_to=''),
        ),
    ]