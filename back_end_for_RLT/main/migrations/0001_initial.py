# Generated by Django 3.2.5 on 2021-07-10 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.TextField()),
                ('password', models.TextField()),
                ('avatar', models.JSONField()),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('position', models.CharField(max_length=150, verbose_name='Должность')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.TextField()),
                ('password', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('position', models.CharField(max_length=150, verbose_name='Должность')),
                ('avatar', models.JSONField(verbose_name='Аватар участника')),
                ('telegram_id', models.IntegerField(verbose_name='ID участника в телеграме')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_project', models.CharField(max_length=155)),
                ('gitHub', models.TextField(verbose_name='GitHub')),
                ('ssh_key', models.TextField(verbose_name='ssh_key')),
                ('telegram_chat_id', models.CharField(max_length=100, verbose_name='ID чата в телеграмме')),
                ('date_start', models.DateField(verbose_name='Дата старта')),
                ('date_end', models.DateField(verbose_name='Дата оканчания')),
                ('status_project', models.CharField(max_length=70, verbose_name='Статус')),
                ('percentage_completion', models.IntegerField(verbose_name='Процент выполения')),
                ('qr_token', models.CharField(max_length=32, verbose_name='QR токен для проекта')),
                ('project_picture', models.JSONField(verbose_name='Картинка проекта')),
            ],
        ),
    ]
