import os
import click
import openai

API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = API_KEY


def generate_prompt(query, num=None):
    return f"""
            List Linux shell commands that would accomplish the task described by the text enclosed by triple backticks:\n"
            ```{query}```.\n"
            Output the shell commands in the following format:\n"
            $ <command 1>\n"
            $ <command 2>\n"
            $ ...\n"
            $ <command n>\n"
            Limit your output to {str(num)} options or less.\n
            If the described task does not correspond to any command line action, simply output:\n"
            'The task your described cannot be accomplished through the command line'\n"
            Do not add an explanation after generating the commands.
            """


@click.command()
@click.argument("query", type=str)
@click.option("--num", type=int, default=3)
def search(query, num):
    prompt = generate_prompt(query, num)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        max_tokens=64,
        temperature=0.0,
    )
    commands = response.choices[0].message.content
    click.echo(f"\nHere are some Linux shell commands that might help:\n\n{commands}\n")
