from rest_framework import serializers
from apps.tasks.models import Task
from django.core.exceptions import ValidationError


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate(self, data):
        title = data.get('title', getattr(self.instance, 'title', None))
        description = data.get('description', getattr(self.instance, 'description', None))

        if not title:
            raise ValidationError("Title is required.")

        if len(description) < 10:
            raise ValidationError("Description must be at least 5 characters long.")

        return data
