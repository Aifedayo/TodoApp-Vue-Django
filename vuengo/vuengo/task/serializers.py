from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'status', 'formatted_created_date', 'formatted_done_date')
