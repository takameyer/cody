import os
import click
from pathlib import Path
from utils import open_chat
import yaml


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.argument(
    "project_path", type=click.Path(exists=True, readable=True), required=False
)
@click.option(
    "--prompt",
    type=click.STRING,
    help="Provide the initial prompt for the LLM. For example: You are an expert Python developer",
)
@click.option(
    "--glob",
    multiple=True,  # Allow multiple glob patterns
    type=click.STRING,
    help="Provide glob strings to match files. Can be used multiple times. For example: **/*.py **/*.md",
)
@click.option(
    "--config",
    type=click.Path(file_okay=True, path_type=Path, exists=True, readable=True),
    help="Configuration YAML that contains the project_dir, prompt, and glob patterns",
)
@click.pass_context
def main(ctx, project_path, prompt, glob, config):
    """
    Open a chat with an LLM to discuss a project, given an initial prompt and the path of the project.
    \b
    USAGE:
      cody ./project/dir PROJECT_DIR [--prompt PROMPT] [--glob PATTERN1] [--glob PATTERN2]
      cody --config ./path/to/config.yml
    ARGUMENTS:
      PROJECT_PATH     Path to the project being discussed.
    OPTIONS:
      --prompt    Initial prompt for the LLM
      --glob      Glob string(s) to determine which files to match (can be used multiple times)
      --config    CONFIG_PATH
                  Path to a config that contains the prompt and project_dir
    Example config.yml:
      project_dir: ./project/dir
      prompt: "You are an expert Python developer"
      glob:
        - "**/*.py"
        - "**/*.md"
        - "**/*.html"
    """
    if config:
        with open(config, "r") as config_stream:
            config_yaml = yaml.safe_load(config_stream)

        # Check for required keys in the config
        required_keys = ["project_path", "prompt", "glob"]
        for key in required_keys:
            if key not in config_yaml:
                click.echo(f"Missing required '{key}' in config file.", err=True)
                click.echo(ctx.get_help())
                ctx.exit(1)

        prompt = config_yaml["prompt"]
        project_path = config_yaml["project_path"]
        glob = config_yaml["glob"]

    # Validate inputs
    if not project_path:
        click.echo("Error: Missing required argument for PROJECT_PATH.", err=True)
        click.echo(ctx.get_help())
        ctx.exit(1)

    if not prompt:
        click.echo("Error: Missing required argument for PROMPT", err=True)
        click.echo(ctx.get_help())
        ctx.exit(1)

    if not glob:
        click.echo("Error: Missing required argument for GLOB", err=True)
        click.echo(ctx.get_help())
        ctx.exit(1)

    # Convert glob to a list if it's not already
    glob_list = list(glob) if isinstance(glob, (list, tuple)) else list(glob)

    open_chat(project_path, prompt, glob_list=glob_list)


if __name__ == "__main__":
    main()
