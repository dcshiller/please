### Plain English bash commands via OpenAI's API.


##### Setup

Note, you need an API key for OpenAI's GPT3 to use this.

Add the following to your bash profile:
```
export OPENAI_API_KEY=your-key-here
alias please="python3 ~/path/to/please.py"
```

#### Usage

```
please list all my files by file size
please sed replace 'jacket' with 'coat' in file.txt
please use rails to create a answers table with a link to questions and completions
please get the current time of day in Tokyo
please get the current temperature in LA
please list all postgres databases
please kill slack if it is running
```

![screenshot.png](screenshot.png)


