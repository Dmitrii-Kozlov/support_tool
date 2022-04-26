from rest_framework import serializers
from cases.models import Case


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ('title', 'description', )
