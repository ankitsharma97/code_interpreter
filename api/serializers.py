from rest_framework import serializers

class CodeInterpreterSerializer(serializers.Serializer):
    """
    Serializer for the code interpreter API.
    
    Attributes:
    - file (FileField): File containing input data.
    - prompt (CharField): Prompt for generating code.
    """
    file = serializers.FileField()
    prompt = serializers.CharField(max_length=500)
