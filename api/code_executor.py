import sys
import io

def execute_code(code):
    
    sys.stdout = io.StringIO()
    
    exec(code)
    
    output = sys.stdout.getvalue()
    
    sys.stdout = sys.__stdout__
    
    return output