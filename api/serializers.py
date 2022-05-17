from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from cases.models import Case, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id','case', 'body', 'author', 'created')

    def get_author(self, obj):
        return obj.author.username


class CaseSerializer(serializers.ModelSerializer):
    # comments = CommentSerializer(source='comments.body')
    author = SerializerMethodField()
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())

    class Meta:
        model = Case
        fields = ('id', 'title', 'comments', 'description', 'emails_list', 'module', 'docfile', 'author', 'created', 'active')
        # fields = '__all__'

    def get_author(self, obj):
        return obj.author.username