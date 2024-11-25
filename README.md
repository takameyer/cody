# Cody

This Python application uses LangChain to interact with OpenAI's GPT-4 API. It loads a project directory as a RAG reference into context and opens up a chat dialogue to have discussions.

## Features
- **Contextual Project Reference**: LLM is able to speak directly about a given project.
- **Initial Prompt Setting**: User is able to provide the initial prompt for the LLM to determine how it should behave. (You are an expert Python developer)
- **Short Term Chat Memory**: Once the chat prompt begins, all previous prompts from the starts are kept in local history until leaving the chat.

## Requirements
- Python 3.9+
- OpenAI API key

## Setup
1. Clone the repository:
    ```bash
    git clone <repo-url>
    cd cody
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
pipenv run python ./path/to/project --prompt "You are an expert Python developer"
```

You can also provide a `yaml` config as an argument
```bash
pipenv run python --config config.yaml
```

Configuration example:
```yaml
project_path: "./path/to/project"
prompt: "You are an expert Python developer"
```

## Build
Run the `build.sh` to create an executable if you want to load this into your path.


