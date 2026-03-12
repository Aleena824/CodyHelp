from setuptools import setup, find_packages

setup(
    name="codyhelp",
    version="1.0.0",
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