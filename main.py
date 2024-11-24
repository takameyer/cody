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
    help="Provide the intial prompt for the LLM.  For example: You are an expert Python developer",
)
@click.option(
    "--config",
    type=click.Path(file_okay=True, path_type=Path, exists=True, readable=True),
    help="Configuration YAML that contains the project_dir and the prompt",
)
@click.pass_context
def main(ctx, project_path, prompt, config):
    """
    Open a chat with an LLM to discuss a project, given an initial prompt and the path of the project.

    \b
    USAGE:
      cody ./project/dir PROJECT_DIR [--prompt PROMPT]
      cody --config ./path/to/config.yml

    ARGUMENTS:
      PROJECT_PATH     Path to the project being discussed.

    OPTIONS:
      --prompt    Initial prompt for the LLM
      --config    CONFIG_PATH
                  Path to a config that contains the prompt and project_dir
    Example config.yml:
      project_dir: ./project/dir
      prompt: "You are an expert Python developer"
    """

    if config:
        config_stream = open(config, "r")
        config_yaml = yaml.load(config_stream, Loader=yaml.Loader)

        # Check for required keys in the config
        if "project_path" not in config_yaml:
            click.echo("Missing required 'project_path' in config file.", err=True)
            click.echo(ctx.get_help())
            ctx.exit(1)

        if "prompt" not in config_yaml:
            click.echo("Missing required 'prompt' in config file.", err=True)
            click.echo(ctx.get_help())
            ctx.exit(1)
        prompt = config_yaml["prompt"]
        project_path = config_yaml["project_path"]

    if not project_path:
        click.echo("Error: Missing required argument for PROJECT_PATH.", err=True)
        click.echo(ctx.get_help())
        ctx.exit(1)

    if not prompt:
        click.echo("Error: Missing required argument for PROMPT", err=True)
        click.echo(ctx.get_help())
        ctx.exit(1)

    open_chat(project_path, prompt)


if __name__ == "__main__":
    main()
