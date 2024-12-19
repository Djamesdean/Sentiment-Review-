"""Console script for Sentiment_review_IPhone."""
import Sentiment_review_IPhone

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for Sentiment_review_IPhone."""
    console.print("Replace this message by putting your code into "
               "Sentiment_review_IPhone.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
