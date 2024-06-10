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
    # Deserialize the request data using the serializer
    serializer = CodeInterpreterSerializer(data=request.data)
    
    # Check if the data is valid
    if serializer.is_valid():
        # Extract file, prompt, and file type from the serializer data
        file = serializer.validated_data['file']
        prompt = serializer.validated_data['prompt']
        file_type = file.name.split('.')[-1].lower()
        
        try:
            # Read the content of the file based on its type
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
            # Log and return an error if there's an issue reading the file
            logger.error(f"Error reading file: {str(e)}")
            return Response({'error': 'Error reading file'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Construct the code prompt for code generation
        code_prompt = f"Generate Python code for {prompt} "
        
        try:
            # Generate code based on the prompt and content
            code = generate_code(code_prompt, content)
            
            # Execute the generated code
            result = execute_code(code)
        except Exception as e:
            # Log and return an error if there's an issue generating or executing the code
            logger.error(f"Error generating or executing code: {str(e)}")
            return Response({'error': 'Error generating or executing code'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        # Return the result and generated code
        return Response({'result': result, 'code': code}, status=status.HTTP_200_OK)
    else:
        # Log and return an error if the data is invalid
        logger.warning(f"Invalid data: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
