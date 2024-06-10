import os
import google.generativeai as genai
import re

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_code(prompt, content):
    """
    Generate Python code based on a prompt and content using a generative AI model.
    
    Args:
    - prompt (str): The prompt for generating the code.
    - content (str): The content to be included in the code.
    
    Returns:
    - str: The generated Python code.
    """
    # Replace the placeholder 'content' in the prompt with the actual content
    prompt = prompt.replace("content", content)

    # Generate the code from the model
    response = model.generate_content(prompt)
    text_code = response.candidates[0].content.parts[0].text

    # Use regular expression to extract only Python code blocks
    code_pattern = r"```python\n([\s\S]*?)\n```"
    matches = re.findall(code_pattern, text_code)

    # Extracted Python code
    extracted_code = "\n".join(matches)

    # Return the extracted Python code
    return extracted_code
