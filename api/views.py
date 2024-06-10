# api/views.py
import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CodeInterpreterSerializer
from .file_reader import read_pdf, read_xlsx, read_csv, read_docx
from .code_writer import generate_code
from .code_executor import execute_code
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)

@csrf_exempt
@api_view(['POST'])
def code_interpreter(request):
    serializer = CodeInterpreterSerializer(data=request.data)
    if serializer.is_valid():
        file = serializer.validated_data['file']
        prompt = serializer.validated_data['prompt']
        file_type = file.name.split('.')[-1].lower()
        
        try:
            if file_type == 'pdf':
                content = read_pdf(file)
            elif file_type == 'xlsx':
                content = read_xlsx(file)
            elif file_type == 'csv':
                content = read_csv(file)
            elif file_type == 'docx':
                content = read_docx(file)
            else:
                return Response({'error': 'Unsupported file type'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error reading file: {str(e)}")
            return Response({'error': 'Error reading file'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        code_prompt = f"Generate Python code for {prompt} "
        try:
            code = generate_code(code_prompt,content)
            print(code)
            result = execute_code(code)
        except Exception as e:
            logger.error(f"Error generating or executing code: {str(e)}")
            return Response({'error': 'Error generating or executing code'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({'result': result, 'code': code}, status=status.HTTP_200_OK)
    else:
        logger.warning(f"Invalid data: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
