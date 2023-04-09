from rest_framework import serializers
from django.core.validators import FileExtensionValidator

class OCRSerializer(serializers.Serializer):
    file = serializers.FileField(required=True)

    class Meta:
        fields = ('file', )

    def validate(self, attrs):
        if attrs['file'].content_type != 'application/pdf':
            raise serializers.ValidationError("file type must be pdf")
        return super().validate(attrs)