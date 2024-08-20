import sys
import os
import json
import re
from termcolor import colored, cprint
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_KEY")

def extract_back_ticks(string):
    if '```' not in string:
        return string

    code_block = False
    code = ''
    lines = string.split('\n')
    for line in lines:
        if line.startswith('```'):
            code_block = True
        elif code_block:
            if line.startswith('```'):
                code_block = False
                break
            else:
                code += line + '\n'
    return code.strip()


def generate_response(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer " + OPENROUTER_API_KEY,
    }
    payload = {
        #  "model": "mistralai/mistral-tiny",  # Optional
        #  "model": "neversleep/noromaid-mixtral-8x7b-instruct",
        #  "model": "meta-llama/codellama-70b-instruct",
        "model": "perplexity/llama-3.1-sonar-huge-128k-online",
        "messages": [{"role": "user", "content": prompt}],
        "top_k": 1,
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response_data = response.json()

    return response_data["choices"][0]["message"]["content"]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        cprint("Please provide a prompt as a command line argument.", "red")
        sys.exit(1)
    prompt = " ".join(sys.argv[1:])
    prompt = f"""The following is a line of bash code that will {prompt}. Just give the answer, no context or backticks."""
    print(colored(prompt, "cyan"))
    command = generate_response(prompt)
    code = extract_back_ticks(command)
    print('code', code)
    print(colored("--> ", "cyan") + colored(code, "magenta"))
    query = colored("Should I run this? (y/n): ", "cyan")
    should_run = input(query)
    if should_run == "y":
        cprint("----------------------------", "cyan")
        os.system(code)
        print("")
        cprint("----------------------------", "cyan")
