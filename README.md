# Cody: AI-Powered Project Assistant

## Overview

Cody is a command-line tool that enables intelligent conversation about your project by analyzing its files and providing context-aware insights using an AI-powered chat interface.

## Features

- 🚀 Flexible project analysis
- 📂 Supports multiple file type matching with glob patterns
- 🤖 Configurable AI prompts
- 🔧 Easy configuration via CLI or YAML config file

## Prerequisites

- Python 3.8+
- pip

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cody.git
cd cody
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Options

```bash
# Basic usage
cody ./path/to/project

# Specify a custom prompt
cody ./path/to/project --prompt "You are an expert Python developer"

# Match multiple file types
cody ./path/to/project --glob "**/*.py" --glob "**/*.md"
```

### Configuration File

Create a `config.yml`:
```yaml
project_path: ./path/to/project
prompt: "You are an expert Python developer"
glob: 
  - "**/*.py"
  - "**/*.md"
```

Then run:
```bash
cody --config config.yml
```

## Configuration Options

| Option | CLI Flag | Config Key | Description | Example |
|--------|----------|------------|-------------|---------|
| Project Path | `project_path` | `project_path` | Directory to analyze | `./my_project` |
| Initial Prompt | `--prompt` | `prompt` | AI chat initialization | `"You are an expert Python developer"` |
| File Matching | `--glob` | `glob` | File type/path patterns to include | `**/*.py` |

## Examples

1. Analyze a Python project:
```bash
cody ./my_python_project --prompt "Analyze this Django project" --glob "**/*.py" --glob "**/*.html"
```

2. Use a configuration file:
```bash
cody --config project_config.yml
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

Project Link: [https://github.com/yourusername/cody](https://github.com/yourusername/cody)
