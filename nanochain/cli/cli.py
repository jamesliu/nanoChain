# cli.py

import click
from nanochain import App

app = App()

@click.group()
def cli():
    pass

@cli.command()
@click.argument('url')
def add(url):
    """Add a resource to the nanochain app."""
    app.add(url)
    click.echo(f"Added resource: {url}")

@cli.command()
@click.argument('query')
def query(query):
    """Query the nanochain app."""
    result = app.query(query)
    click.echo(f"Result: {result}")

if __name__ == "__main__":
    cli()

