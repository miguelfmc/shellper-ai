# Shellper

Shellper is a Python command-line tool that leverages the power of OpenAI's GPT language model to help you find the right Linux shell commands while you are using the command line.

## Installation

For now, the only way to use `shellper` is to clone this repository and install via `pip`:

```bash
git clone https://github.com/miguelfmc/shellper-ai.git
cd shellper-ai
pip install .
```

I will make the package available on PyPI shortly!

Before using Shellper AI, you will need to set up an OpenAI API key as an environment variable. You can do this by adding the following line to your shell configuration file (e.g. `.bashrc`, `.zshrc`, etc.):

```bash
export OPENAI_API_KEY=YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your actual OpenAI API key. If you don't have an API key yet, you can [sign up for OpenAI](https://beta.openai.com/signup/) to get one.

## Quickstart

To get started with Shellper AI, simply run the `shellper` command followed by your natural language command. 

```bash
shellper "Remove all JPG files older than 1 month from the tmp folder"
```

You can also specify the number of options you want GPT-3.5 to retrieve for you using the optional argument `--num`

```bash
shellper "Remove all JPG files older than 1 month from the tmp folder" --num 3
```

## Known Issues

This is just a toy example that I built quickly to play around with OpenAI's API and GPT models, so expect it to be hacky!