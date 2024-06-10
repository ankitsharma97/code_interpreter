# api/serializers.py
from rest_framework import serializers

class CodeInterpreterSerializer(serializers.Serializer):
    file = serializers.FileField()
    prompt = serializers.CharField(max_length=500)
