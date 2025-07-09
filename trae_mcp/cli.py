import click
from .agents.orchestrator import Orchestrator

@click.command()
@click.argument("spec_file", type=click.Path(exists=True, dir_okay=False))
def main(spec_file):
    """Runs the Trae MCP project from a single terminal."""
    try:
        orchestrator = Orchestrator(spec_path=spec_file)
        orchestrator.run()
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
