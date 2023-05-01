import openai
import sys
import os
from termcolor import colored, cprint

# Make sure you have the OpenAI API key set as an environment variable
api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    print("Please set the OPENAI_API_KEY environment variable.")
    sys.exit(1)

openai.api_key = api_key

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=len(prompt) + 100,
        n=1,
        stop=None,
        temperature=0.0,
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        cprint("Please provide a prompt as a command line argument.", 'red')
        sys.exit(1)
    prompt = " ".join(sys.argv[1:])
    prompt = f"""The following is a line of bash code that will {prompt}."""
    print(colored(prompt, 'cyan'))
    command = generate_response(prompt)
    print(colored("--> ", 'cyan') + colored(command, 'magenta'))
    query = colored("Should I run this? (y/n): ", 'cyan')
    should_run = input(query)
    if should_run == 'y':
        cprint('----------------------------', 'cyan')
        os.system(command)
        print('')
        cprint('----------------------------', 'cyan')

