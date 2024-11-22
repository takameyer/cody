#!/bin/bash
pyinstaller --hidden-import=pydantic --hidden-import=pydantic-core --hidden-import=pydantic.deprecated.decorator main.py

