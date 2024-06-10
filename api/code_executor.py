import sys
import io

def execute_code(code):
    """
    Execute Python code and capture the output.
    
    Args:
    - code (str): Python code to execute.
    
    Returns:
    - str: Output of the code execution.
    """
    # Redirect stdout to capture the output
    sys.stdout = io.StringIO()
    
    # Execute the code
    exec(code)
    
    # Get the output
    output = sys.stdout.getvalue()
    
    # Reset stdout
    sys.stdout = sys.__stdout__
    
    return output
