import click
from openai import OpenAI
import os

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
)

@click.group()
def main():
    pass

@main.command()
@click.argument("file")
@click.option("--interview", is_flag=True, help="Explain in interview mode")
def explain(file, interview):
    """Explain a code file."""
    try:
        with open(file, "r") as f:
            code = f.read()
    except FileNotFoundError:
        click.echo(f"Error: File '{file}' not found.")
        return

    if interview:
        prompt = f"Explain this code as if I need to defend it in a job interview. Include: how to explain it verbally, time/space complexity, likely follow-up questions, and key concepts to know.\n\n{code}"
    else:
        prompt = f"Explain what this code does in simple terms:\n\n{code}"

    click.echo("Analysing...")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    click.echo(response.choices[0].message.content)