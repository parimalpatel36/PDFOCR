from rest_framework import generics, viewsets
from .serializers import OCRSerializer
from rest_framework import viewsets
from rest_framework.response import Response
import pdftotext
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import OCRSerializer


from rest_framework.parsers import MultiPartParser
class OCRViewSet(viewsets.ViewSet):
    parser_classes = [MultiPartParser]

    
    @swagger_auto_schema(
        tags=['OCR'],
        operation_description="",
        operation_summary="",
        request_body=OCRSerializer
    )
    def create(self, request):
        serializer = OCRSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            file_obj = request.FILES.get('file')
            pdf = pdftotext.PDF(file_obj, "secret")
            text = "\n".join(pdf)
            return Response({'text':text, 'message': 'OCR done successfully'})