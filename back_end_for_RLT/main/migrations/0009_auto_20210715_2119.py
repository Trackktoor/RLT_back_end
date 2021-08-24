# Generated by Django 3.2.5 on 2021-07-15 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_participant_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='avatar',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='client',
            name='position',
            field=models.CharField(max_length=140, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='position',
            field=models.CharField(max_length=140, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_picture',
            field=models.ImageField(max_length=500, upload_to='', verbose_name='Картинка проекта'),
        ),
    ]