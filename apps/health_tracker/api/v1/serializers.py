from rest_framework import serializers


class HealthScoreSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    health_score = serializers.IntegerField()
