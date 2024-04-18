from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Snippet, Tag
from django.urls import reverse


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = User.objects.filter(username=data.get('username')).first()
        if user and user.check_password(data.get('password')):
            refresh = RefreshToken.for_user(user)
            return {'token': str(refresh.access_token)}
        raise serializers.ValidationError("Incorrect username or password")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title']

# class SnippetSerializer(serializers.ModelSerializer):
#     tags = TagSerializer(many=True)
#     class Meta:
#         model = Snippet
#         fields = ['title', 'text', 'timestamp', 'tags']

#     def create(self, validated_data):
#         tags_data = validated_data.pop('tags', [])
#         snippet = Snippet.objects.create(**validated_data)
#         for tag_data in tags_data:
#             tag, _ = Tag.objects.get_or_create(**tag_data)
#             snippet.tags.add(tag)
#         return snippet


class SnippetSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    tags = TagSerializer(many=True)

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'text', 'timestamp', 'tags', 'detail_url']

    def get_detail_url(self, obj):
        return reverse('snippet-detail', kwargs={'pk': obj.pk})

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        snippet = Snippet.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(**tag_data)
            snippet.tags.add(tag)
        return snippet