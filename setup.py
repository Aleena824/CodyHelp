from setuptools import setup, find_packages

setup(
    name="codyhelp",
    version="1.0.1",
    description="An AI-powered CLI tool that helps developers understand and improve their code",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "click",
        "openai",
    ],
    entry_points={
        "console_scripts": [
            "codyhelp=codyhelp.cli:main",
        ],
    },
)