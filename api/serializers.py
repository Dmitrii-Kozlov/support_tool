from rest_framework import serializers
from cases.models import Case


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        # fields = ('id', 'title', 'description', 'emails_list', 'module', 'docfile', 'author', 'created', 'active')
        fields = '__all__'
