# Text Summarization API

This project provides an API for interpreting and executing code generated from a prompt on given Content.

## Prerequisites

- Python 3.7+
- Git
- Virtualenv

## Setup Instructions

1. **Install Python:** [Download and install Python](https://www.python.org/downloads/).

2. **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    ```

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

3. **Clone the Project:**

    ```bash
    git clone https://github.com/ankitsharma97/code_interpreter.git
    cd code_interpreter
    ```

4. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Include API_KEY:**
    ```bash
      export API_KEY=your_gemini_api_key_here 
    ```
6. **Run the Server:**

    ```bash
    python manage.py runserver
    ```

## Testing the API Endpoint

You can test the `/api/code_interpreter/` endpoint using tools like Postman.

### Using Postman

1. Open Postman and create a new POST request.
2. Set the request URL to `http://localhost:8000/api/code_interpreter/`.
3. Add two form-data parameters:
   - Key: `file`, Value: Select File and choose your file.
   - Key: `prompt`, Value: Your prompt here.
4. Click Send to make the request.

You should receive a response containing the result of the code execution and the generated Python code.
