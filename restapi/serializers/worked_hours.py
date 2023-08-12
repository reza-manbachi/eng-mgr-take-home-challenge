from rest_framework import serializers
from ..models.worked_hours import WorkedHour

class WorkedHourSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user_id')  # Map user_id to id
    
    class Meta:
        model = WorkedHour
        fields = ['id', 'date', 'hours']
