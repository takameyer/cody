# Cody

This Python application uses LangChain to interact with OpenAI's GPT-4 API. It analyzes a code file and provides a summary of its functionality, with an option to annotate the code with comments.

## Features
- **Summarize Code**: Provides a detailed summary of what the code does.
- **Annotate Code**: Adds comments to the code explaining its functionality.
- **Output to File**: Save the result to a specified file.

## Requirements
- Python 3.9+
- OpenAI API key

## Setup
1. Clone the repository:
    ```bash
    git clone <repo-url>
    cd code-analyzer
    ```

2. Install dependencies using Pipenv:
    ```bash
    pipenv install
    ```

3. Add your OpenAI API key as an environment variable:
    ```bash
    export OPENAI_API_KEY="your-openai-api-key"
    ```

## Usage
Run the application with the desired file as an argument:
```bash
pipenv run python main.py <file-path>

