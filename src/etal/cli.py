import click
import logging
from pathlib import Path
from rich.logging import RichHandler

from .utils import process_file

log = logging.getLogger(__name__)


@click.command()
@click.option("--verbose", "-v", is_flag=True, help="Enables verbose mode.")
@click.option(
    "--output",
    "-o",
    type=str,
    default=None,
    help="Output file. Defaults to input file with the suffix changed to -etal.bib.",
)
@click.argument("input", type=str, required=True)
def main(verbose: bool, output: str | None, input: str):
    if verbose:
        logging.basicConfig(level=logging.INFO, format="%(message)s", handlers=[RichHandler()])
    else:
        logging.basicConfig(level=logging.WARNING, format="%(message)s", handlers=[RichHandler()])

    if not input:
        raise click.BadParameter("No input file given.")

    input_path = Path(input)

    if not input_path.exists():
        raise click.BadParameter(f"File {input_path} does not exist.")

    if output is None:
        output_path = input_path.parent / f"{input_path.stem}-etal.bib"
    else:
        output_path = Path(output)

    if not output_path.parent.exists():
        output_path.parent.mkdir(parents=True)

    log.info(f"Processing {input_path} -> {output_path}")
    process_file(input_path, output_path)
