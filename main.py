import os
import click
from pathlib import Path
from utils import analyze_file, annotate_code


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.argument("file_path", type=click.Path(exists=True, readable=True), required=True)
@click.option(
    "--annotate",
    is_flag=True,
    help="Add comments to the code explaining its functionality.",
)
@click.option(
    "--output-file", type=click.Path(), help="Write the result to the specified file."
)
def main(file_path, annotate, output_file):
    """
    Analyze a code file and summarize its content. Optionally annotate code with comments

    \b
    USAGE:
      python main.py FILE_PATH [--annotate] [--output-file OUTPUT_FILE]

    ARGUMENTS:
      FILE_PATH     Path to the code file to be analyzed.

    OPTIONS:
      --annotate    Add comments to the code explaining its functionality.
      --output-file OUTPUT_FILE
                    Write the result to the specified file.
    """

    file_path = Path(file_path).resolve()

    with open(file_path, "r") as f:
        code = f.read()

    if annotate:
        result = annotate_code(code)
    else:
        result = analyze_file(code)

    if output_file:
        with open(output_file, "w") as f:
            f.write(result)
        print(f"Result written to {output_file}")
    else:
        print(result.content)


if __name__ == "__main__":
    main()
