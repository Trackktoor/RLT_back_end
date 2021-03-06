# Generated by Django 3.2.5 on 2021-07-12 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_participant_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='avatar',
            field=models.ImageField(upload_to='', verbose_name='Картинка Участника'),
        ),
        migrations.AlterField(
            model_name='project',
            name='telegram_chat_id',
            field=models.TextField(verbose_name='ID чата в телеграмме'),
        ),
    ]
