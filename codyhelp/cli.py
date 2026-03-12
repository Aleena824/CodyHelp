#CODYHELP V1

import click
from openai import OpenAI
import os

from codyhelp.prompts import explain_prompt, interview_prompt, review_prompt, stacktrace_prompt

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
        prompt = interview_prompt(code)
    else:
        prompt = explain_prompt(code)

    click.echo("\n ANALYSING...\n")

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

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
    
    prompt = review_prompt(code)

    click.echo("\n ANALYSING...\n")

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        click.echo(response.choices[0].message.content)

    except Exception as e:
        click.echo(f"Error while calling API: {str(e)}")

#Error explanation through stacktraces

@main.command()
@click.argument("file")

def stacktrace(file):
    try:
        with open(file,"r") as f:
            error=f.read()
    except FileNotFoundError:
        click.echo(f"Error: File '{file}' not found. ")
        return
    
    prompt= stacktrace_prompt(error)

    click.echo("\n ANALYSING...\n")

    try:
        response=client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"user", "content":prompt}]
        )
        
        click.echo(response.choices[0].message.content)

    except Exception as e:
        click.echo(f"Error while calling API: {str(e)}")
    