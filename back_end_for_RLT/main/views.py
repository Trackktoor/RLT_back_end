from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
import json
from rest_framework import status
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import psycopg2
from rest_framework.views import APIView
from django.core.files.storage import FileSystemStorage
import telebot
from .serializers import *


class create_new_project(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None, *args, **kwargs):
        #if len(request.user.groups.all()) != 0 and str(request.user.groups.all()[0]) == 'Manager':
            serializer = ProjectSerializer(data=request.data)
            if serializer.is_valid():
                try:
                    # КОНЕКТ К БД
                    connection = psycopg2.connect(
                        user="postgres",
                        password="roma.ru12",
                        host="127.0.0.1",
                        port="5432",
                        database="postgres_db")
                    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                    # Курсор для выполнения операций с базой данных
                    cursor = connection.cursor()
                except:
                    connection.close()
                    return Response({'status': 'ERR', 'errCode': 'Database is not responding'})

                cursor.execute(
                    f"INSERT INTO TELEGRAM_CHATS_ID (CHAT_ID) VALUES ({request.data['telegram_chat_id']})"
                )

                if request.FILES['project_picture']:
                    project_picture = request.FILES['project_picture']
                    fs = FileSystemStorage()
                    save_photo = fs.save(project_picture.name, project_picture)
                    serializer.save()
                    return Response({'data': {}, 'status': "OK"}, status=status.HTTP_201_CREATED)
                else:
                    serializer.save()
                    return Response({'data': {}, 'status': "OK"}, status=status.HTTP_201_CREATED)
            else:
                return Response({'status': "ERR", 'errCode': serializer.errors})
        #else:
        #    return Response({'status': 'ERR', 'errCode': 'Not enough rights'})


class create_new_participant(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None, *args, **kwargs):
        if len(request.user.groups.all()) != 0 and str(request.user.groups.all()[0]) == 'Manager':
            serializer = ParticipantSerializer(data=request.data)
            if serializer.is_valid():
                if request.FILES['avatar']:
                    avatar = request.FILES['avatar']
                    fs = FileSystemStorage()
                    save_photo = fs.save(avatar.name, avatar)
                    serializer.save()
                else:
                    serializer.save()
                return Response({'data': {}, 'status': "OK"}, status=status.HTTP_201_CREATED)
            else:
                return Response({'status': 'ERR', 'errCode': serializer.errors})
        else:
            return Response({'status': 'ERR', 'errCode': 'Not enough rights'})


class pinning_participant(APIView):
    parser_classes = (JSONParser, FormParser)

    def post(self, request, format=None, *args, **kwargs):
        if len(request.user.groups.all()) != 0 and str(request.user.groups.all()[0]) == 'Manager':
            try:
                id_project = request.data['id_project']
                id_participant = request.data['id_participant']
                participant = Participant.objects.get(id=id_participant)
                project = Project.objects.get(id=id_project)

                project.participant_set.add(participant)

                return Response({'data': {}, 'status': "OK"}, status=status.HTTP_201_CREATED)
            except:
                return Response({'status': 'ERR', 'errCode': 'BAD_REQUEST'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'status': 'ERR', 'errCode': 'Not enough rights'})


class get_info_for_project(APIView):
    parser_classes = (JSONParser, FormParser)

    def get(self, request):
        if len(request.user.groups.all()) != 0 and str(request.user.groups.all()[0]) == 'Client':
            try:
                if request.data['id_project'] != None:
                    project_id = request.data['id_project']
                else:
                    project_id = 1
                project = Project.objects.get(id=project_id)

                return Response({'data': {json.dumps(project.as_json(), indent=4)}, 'status': "OK"},
                                status=status.HTTP_200_OK)
            except:
                return Response({'status': 'ERR', 'errCode': 'BAD_REQUEST'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'status': 'ERR', 'errCode': 'Not enough rights'})


class send_message_in_telegram_chat(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        #if len(request.user.groups.all()) != 0 and str(request.user.groups.all()[0]) == 'Client':
            try:
                # КОНЕКТ К БД
                connection = psycopg2.connect(
                    user="postgres",
                    password="roma.ru12",
                    host="127.0.0.1",
                    port="5432",
                    database="postgres_db")
                connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                # Курсор для выполнения операций с базой данных
                cursor = connection.cursor()
            except:
                connection.close()
                return Response({'status': 'ERR', 'errCode': 'Database is not responding'})

            cursor.execute(
                "SELECT CHAT_ID from TELEGRAM_CHATS_ID"
            )
            chats = cursor.fetchall()

            bot = telebot.TeleBot('1833138112:AAH4WaldLi4tzlG2yPPk2g_NYqxsq-t4xOk') # пернести в отдельный файл
            for chat in chats:
                file = request.FILES['document']
                bot.send_document(chat[0], file, caption=f'Имя: {request.POST["name"]}\nСообщение: {request.POST["msg"]}')
                file.seek(0)
            return Response({'data': {}, 'status': "OK"}, status=status.HTTP_201_CREATED)

        #else:
        #    return Response({'status': 'ERR', 'errCode': 'Not enough rights'})


class get_messages_for_telegram_chat(APIView):
    parser_classes = (JSONParser, FormParser)

    def get(self, request):
        #if len(request.user.groups.all()) != 0 and str(request.user.groups.all()[0]) == 'Client':
            try:
                # КОНЕКТ К БД
                connection = psycopg2.connect(
                    user="postgres",
                    password="roma.ru12",
                    host="127.0.0.1",
                    port="5432",
                    database="postgres_db")
                connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                # Курсор для выполнения операций с базой данных
                cursor = connection.cursor()
            except:
                connection.close()
                return Response({'status': 'ERR', 'errCode': 'Database is not responding'})

            cursor.execute(
                "SELECT MESSAGEID, TELEGRAMUSERID, MESSAGE, FILE, RESPONSETO, RESPONSE_MESSAGE from LOGGING_MESSAGES")

            data = []
            rows = cursor.fetchall()
            for row in rows:
                try:
                    if len(data) <= request.data['count']:
                        data.append(row)
                    else:
                        continue
                except:
                    data.append(row)

            return Response({'data': {json.dumps(data)}, 'status': "OK"}, status=status.HTTP_200_OK)
        #else:
        #    return Response({'status': 'ERR', 'errCode': 'Not enough rights'})


class create_new_client(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, cache):
        for el in Project.objects.all():
            if el.qr_token == cache:
                serializer = ClientSerializer(data=request.data)
                if serializer.is_valid():
                    if request.FILES['avatar']:
                        avatar = request.FILES['avatar']
                        fs = FileSystemStorage()
                        save_photo = fs.save(avatar.name, avatar)
                        user = User.objects.create_user(username=request.data['name'],
                                                        password=request.data['password'], )
                        user.save()
                        client_group = Group.objects.get(name='Client')

                        client_group.user_set.add(user)
                        client = Client.objects.create(name=request.data['name'],
                                                       login=request.data['login'],
                                                       password=request.data['password'],
                                                       avatar=request.data['avatar'],
                                                       position=request.data['position'],
                                                       user=user)
                        client.save()
                        return Response({'data': {}, 'status': "OK"}, status=status.HTTP_201_CREATED)
                    else:
                        user = User.objects.create_user(username=request.data['name'],
                                                        password=request.data['password'], )
                        client_group = Group.objects.get(name='Client')
                        user.save()
                        client_group.user_set.add(user)
                        serializer.save()
                        return Response({'data': {}, 'status': "OK"}, status=status.HTTP_201_CREATED)
                else:
                    print(serializer.errors)
                    return Response({'status': 'ERR', 'errCode': 'BAD_REQUEST'})
            else:
                return Response({'status': 'ERR', 'errCode': 'invalid cache'})


class create_new_entry_for_chronicle(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        if len(request.user.groups.all()) != 0 and str(request.user.groups.all()[0]) == 'Manager':
            project = Project.objects.get(qr_token=request.data['qr_token'])
            chronicle = Chronicle.objects.get(id=project.id_chronicle)
            request.data['chronicle'] = chronicle.pk

            serializer = EntryForChronicleSerializer(data=request.data)
            if serializer.is_valid():
                if request.data['category'] in ['Git', 'Default', 'Core']:
                    serializer.save()
                    return Response({'data': {}, 'status': "OK"}, status=status.HTTP_201_CREATED)
                else:
                    print(serializer.errors)
                    return Response({'status': 'ERR', 'errCode': 'BAD_REQUEST'})
            else:
                print(serializer.errors)
                return Response({'status': 'ERR', 'errCode': 'BAD_REQUEST'})
        else:
            return Response({'status': 'ERR', 'errCode': 'Not enough rights'})


