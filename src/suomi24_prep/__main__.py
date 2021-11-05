"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Suomi24 Prep."""


if __name__ == "__main__":
    main(prog_name="suomi24-prep")  # pragma: no cover
