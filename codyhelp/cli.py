import click
from openai import OpenAI
import os

api_key=os.environ.get("GITHUB_TOKEN")
if not api_key:
    raise EnvironmentError("GITHUB_TOKEN environment variable is not set.")

client = OpenAI(base_url="https://models.inference.ai.azure.com", api_key=api_key)

@click.group()
def main():
    pass

#Explain a code file.

@main.command()
@click.argument("file")
@click.option("--interview", is_flag=True, help="Explain in interview mode")

def explain(file, interview):
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

    click.echo("\n ANALYSING...\n")

    try:
        response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}])

        click.echo(response.choices[0].message.content)

    except Exception as e:
        click.echo(f"Error while calling API: {str(e)}")

#Reviews code and suggests improvements

@main.command()
@click.argument("file")

def review(file):
    try:
        with open (file,"r") as f:
            code=f.read()
    except FileNotFoundError:
        click.echo(f"Error: File '{file}' not found.")
        return
    
    prompt = f"Review this code and detect possible bugs. For each bug found, label it with a severity level: [HIGH], [MEDIUM], or [LOW]. Then suggest improvements.\n\n{code}"

    click.echo("\n ANALYSING...\n")

    try:
        response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}])

        click.echo(response.choices[0].message.content)

    except Exception as e:
        click.echo(f"Error while calling API: {str(e)}")