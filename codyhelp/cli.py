#CODYHELP FEATURES

import click
from openai import OpenAI
import os

from codyhelp.prompts import explain_prompt, interview_prompt, review_prompt, stacktrace_prompt, leetcode_prompt, gitdiff_prompt, repo_prompt
import subprocess #for gitdiff command

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
    """Explain a code file."""
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
    """Review code and detect bugs with severity levels."""
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
    """Explain errors and suggest fixes from a stack trace file."""
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

#Suggesting leetcode questions based on concept

@main.command()
@click.argument("file")

def leetcode(file):
    """Suggests leetcode questions based on the concepts used in the code"""
    try:
        with open(file,"r") as f:
            code=f.read()
    except FileNotFoundError:
        click.echo(f"Error: File {file} not found.")
        return
    
    prompt = leetcode_prompt(code)

    click.echo("\nANALYSING..\n")

    try:
        response=client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"user", "content": prompt}]
        )

        click.echo(response.choices[0].message.content)
    
    except Exception as e:
        click.echo(f"Error while calling API: {str(e)}")

#gitdiff feature compares old file to new file and makes suggestions on the changes made before pushing to GitHub

@main.command()

def gitdiff():
    """Review your uncommitted changes before pushing to GitHub."""
    result = subprocess.run(["git", "diff"], capture_output=True, text=True, encoding="utf-8")#utf-8 is windows default encoding
    diff = result.stdout

    if diff=="":
        click.echo(f"No changes have been made to the file.")
    else:
        prompt = gitdiff_prompt(diff)
        click.echo("\n ANALYSING...\n")
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            click.echo(response.choices[0].message.content)
        except Exception as e:
            click.echo(f"Error while calling API: {str(e)}")

#Analyses all files in the project to give a high-level understanding of the whole code in the repository

extensions = (".py", ".js", ".java", ".cpp", ".c", ".ts", ".m", ".ml")

@main.command()
def repo():
    """All files in the repository are analysed and a full description is given"""
    combined_code = ""
    for root, dirs, files in os.walk("."):
        filtered = []
        for d in dirs:
            if d not in ["venv", "__pycache__", ".git", "build", "dist"]:
                filtered.append(d)
        dirs[:] = filtered #this ensures that only necessary code is analysed by the API model by skipping folders in the list 'filtered'
        for file in files:
            if file.endswith(extensions):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    combined_code += f"\n\n File: {filepath}\n{f.read()}"
    
    if combined_code=="":
        click.echo(f"The repository is empty.")
    else:
        prompt = repo_prompt(combined_code)
        click.echo("\n ANALYSING...\n")
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            click.echo(response.choices[0].message.content)
        except Exception as e:
            click.echo(f"Error while calling API: {str(e)}")