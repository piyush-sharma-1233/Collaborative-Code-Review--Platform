# review/serializers.py

from rest_framework import serializers
from .models import Session, CodeSnippet, Comment, Reviewer
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'line_number', 'content', 'resolved')

class CodeSnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeSnippet
        fields = ('id', 'file', 'language')

class SessionSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    code_snippet = CodeSnippetSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    reviewers = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Session
        fields = ('id', 'name', 'creator', 'status', 'creation_date', 'code_snippet', 'comments', 'reviewers')

class SessionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('name',)

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('line_number', 'content')
