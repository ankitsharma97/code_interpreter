import os
import google.generativeai as genai
import re

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

def generate_code(prompt, content):
    
    prompt = prompt.replace("content", content)

    response = model.generate_content(prompt)
    
    text_code = response.candidates[0].content.parts[0].text

    code_pattern = r"```(?:python|bash|sh|shell|java|cpp|c|html|xml|javascript|js|css|php|ruby|perl|go|swift|kotlin|scala|sql)\n([\s\S]*?)\n```"
    matches = re.findall(code_pattern, text_code)

    extracted_code = "\n".join(matches)

    # exec(extracted_code)
    
    return extracted_code

