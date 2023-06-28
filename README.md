
# Python Chatbot Template

This is a Python chatbot template using the Discord library and the Hugging Face Transformers library. The chatbot is based on the GPT-2 model and can generate text responses to user messages.

## Setup
To use this chatbot template, you need to follow these steps:

Install the required dependencies. You can install them using pip:

pip install discord transformers
Obtain a bot token from the Discord Developer Portal. This token will be used to authenticate your bot with Discord. Replace 'YOUR-BOT-TOKEN' in the code with your actual bot token.
Customization
To customize the chatbot, you can modify the code in the provided Python script. Here are some areas you might want to customize:

## Chatbot Model
The chatbot uses the GPT-2 model from the Hugging Face Transformers library. If you want to use a different model, you can change the model name or replace it with another model from the Hugging Face model hub.


class Chatbot:
    def __init__(self):
        self.generator = pipeline('text-generation', model='gpt2')
        set_seed(42)

    def generate_text(self, prompt, max_length=30, num_return_sequences=1):
        return self.generator(prompt, max_length=max_length, num_return_sequences=num_return_sequences)

###Command Prefix
The bot uses ; as the command prefix by default. You can change it by modifying the command_prefix parameter when creating the commands.Bot instance.

bot = commands.Bot(command_prefix=";")
