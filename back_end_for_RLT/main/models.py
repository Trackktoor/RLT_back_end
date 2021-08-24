from django.db import models
from hashlib import md5
from django.conf import settings
from django.contrib.auth.models import User
import random


class Chronicle(models.Model):
    name_project = models.TextField('Имя проекта', blank=False)

class Entry_for_chronicle(models.Model):
    chronicle = models.ForeignKey(Chronicle, on_delete=models.CASCADE)
    name = models.TextField('Название записи')
    description = models.TextField('Описание')
    attachments = models.FileField('Вложения', blank=False, null=True)
    category = models.CharField('Категория', max_length=100)
    date_of_action = models.DateField()
    def save(self, *args, **kwargs):
        if self.attachments != None:
            self.attachments = ''
            self.attachments = settings.MEDIA_ROOT + '\\' + str(self.attachments)

class Project(models.Model):
    name_project = models.CharField(max_length=255)
    gitHub = models.TextField('GitHub')
    ssh_key = models.TextField('ssh_key')
    telegram_chat_id = models.TextField('ID чата в телеграмме')
    date_start = models.DateField('Дата старта')
    date_end = models.DateField('Дата оканчания')
    status_project = models.CharField('Статус', max_length=255)
    percentage_completion = models.IntegerField('Процент выполения')
    qr_token = models.CharField('QR токен для проекта', max_length=96, blank=False)
    project_picture = models.ImageField('Картинка проекта', blank=False, max_length=500)
    chronicle_for_project = models.ForeignKey(Chronicle, on_delete=models.CASCADE, default=(Chronicle.objects.create(name_project='Chronical')).save())
    id_chronicle = models.BigIntegerField(blank=False, null=True)
    def save(self, *args, **kwargs):
        if self.project_picture != None:
            self.project_picture = ''
            self.project_picture = settings.MEDIA_ROOT + '\\' + str(self.project_picture)
            self.qr_token = md5(self.name_project.encode('ISO-8859-1')).hexdigest()[:96] + str(random.randint(1, 10000))
            chronicle = Chronicle.objects.create(name_project=self.qr_token)
            chronicle.save()
            print(chronicle)
            self.chronicle_for_project = chronicle
            self.id_chronicle = chronicle.id
            return super().save(*args, **kwargs)

    def as_json(self):
        return dict(
            name_project=self.name_project,
            gitHub=self.gitHub,
            ssh_key=self.ssh_key,
            telegram_chat_id=self.telegram_chat_id,
            date_start=str(self.date_start),
            date_end=str(self.date_end),
            status_project=self.status_project,
            percentage_completion=self.percentage_completion,
            qr_token=self.qr_token,
            project_picture=str(self.project_picture)

        )

    def __str__(self):
        return self.name_project

class Participant(models.Model):
    main_projects_for_participant = models.ManyToManyField(Project, blank=False)

    name = models.CharField('Имя', max_length=100)
    position = models.CharField('Должность', max_length=140)
    avatar = models.ImageField('Картинка Участника', blank=False, max_length=500)
    telegram_id = models.IntegerField('ID участника в телеграме')

    def save(self, *args, **kwargs):
        if self.avatar != None:
            self.avatar = ''
            self.avatar = settings.MEDIA_ROOT + '\\' + str(self.avatar)
            return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Manager(models.Model):
    login = models.TextField()
    password = models.TextField()

    def __str__(self):
        return self.login

class Client(models.Model):
    login = models.TextField()
    password = models.TextField()
    avatar = models.ImageField(blank=False)
    name = models.CharField('Имя', max_length=200)
    position = models.CharField('Должность', max_length=140)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=True)

    def save(self, *args, **kwargs):
        if self.avatar != None:
            self.avatar = ''
            self.avatar = settings.MEDIA_ROOT + '\\' + str(self.avatar)
            return super().save(*args, **kwargs)
