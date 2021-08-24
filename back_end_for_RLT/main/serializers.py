from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'name_project',
            'gitHub', 'ssh_key',
            'telegram_chat_id',
            'date_start',
            'date_end',
            'status_project',
            'percentage_completion',
            'qr_token',
            'project_picture'
        )

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = (
            'name',
            'position',
            'avatar',
            'telegram_id',
        )

    def create(self, validated_data):
        return Participant.objects.create(**validated_data)

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'name',
            'login',
            'password',
            'avatar',
            'position',
            'user'
        )

    def create(self, user, validated_data):
        return Client.objects.create(**validated_data)

    def save(self, user, *args, **kwargs):
        return super().save(*args, **kwargs)

class EntryForChronicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry_for_chronicle
        fields = (
            'chronicle',
            'name',
            'description',
            'attachments',
            'category',
            'date_of_action'
        )

    def create(self, validated_data):
        return Entry_for_chronicle.objects.create(**validated_data)