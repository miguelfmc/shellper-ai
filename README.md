# Shellper AI

Shellper AI is a Python command-line tool that leverages the power of OpenAI's GPT language model to help you find the right Linux shell commands while you are using the command line.

## Installation

You can install Shellper AI using pip:

```bash
pip install shellper-ai
```

Before using Shellper AI, you will need to set up an OpenAI API key as an environment variable. You can do this by adding the following line to your shell configuration file (e.g. `.bashrc`, `.zshrc`, etc.):

```bash
export OPENAI_API_KEY=YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your actual OpenAI API key. If you don't have an API key yet, you can [sign up for OpenAI](https://beta.openai.com/signup/) to get one.

## Quickstart

To get started with Shellper AI, simply run the `shellper` command followed by your natural language command. 

```
shellper --query "Remove all JPG files older than 1 month from the tmp folder"
```

## Known Issues

- 