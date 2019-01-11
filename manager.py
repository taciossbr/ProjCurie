import click

from app import app


@click.group()
def c():
    ...


@c.command()
def runserver():
    """
    Inicia o servidor

    """
    app.run(debug=True)


c()
