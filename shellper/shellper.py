import os
import click
import openai

API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = API_KEY


@click.command()
@click.option("--query", type=str, prompt="What are you trying to do?")
def search(query):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": f"List Linux shell commands that would accomplish the following: {query}."
                "Do not add an explanation after generating the commands",
            }
        ],
        max_tokens=30,
        temperature=0.3,
    )
    commands = response.choices[0].message.content
    click.echo(f"\nHere are some Linux shell commands that might help:\n\n{commands}\n")
