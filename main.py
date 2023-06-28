import discord
from discord.ext import commands
from transformers import pipeline, set_seed

# Initialize the chatbot
class Chatbot:
    def __init__(self):
        self.generator = pipeline('text-generation', model='gpt2')
        set_seed(42)

    def generate_text(self, prompt, max_length=30, num_return_sequences=1):
        return self.generator(prompt, max_length=max_length, num_return_sequences=num_return_sequences)

chatbot = Chatbot()

# Create the Discord bot instance
bot = commands.Bot(command_prefix=";")

# Event: Bot is ready and connected to Discord
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

# Event: Bot receives a message
@bot.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == bot.user:
        return

    if message.content.lower() == "!wave":
        # Send the "wave.gif" file
        with open("wave.gif", "rb") as file:
            wave_gif = discord.File(file)
            await message.channel.send(file=wave_gif)
    elif message.content.lower() == "!bubble":
        # Send the "wave.gif" file
        with open("bubble.gif", "rb") as file:
            wave_gif = discord.File(file)
            await message.channel.send(file=wave_gif)
    elif message.content.lower() == "!help":
        help_message = "Hello! I'm Nebula. You can use the `;` prefix to communicate with me. Here are some commands you can try:\n\n" \
                       "-` Disclaimer: We are not responsible for what the bot produces. ` \n\n"
        await message.channel.send(help_message)
        with open("bubble.gif", "rb") as file:
            wave_gif = discord.File(file)
            await message.channel.send(file=wave_gif)
    else:
        # Process other commands and events
        await bot.process_commands(message)

    # Check if the message starts with the prefix ;
    if message.content.startswith(';'):
        user_input = message.content[1:]  # Remove the prefix from the user's message

        if user_input.lower() == "exit":
            await message.channel.send("Goodbye!")
        else:
            response = chatbot.generate_text(user_input)
            mention = message.author.mention
            print(str(response))
            respond=((str(response[0])))
            respond=(respond.replace("{'generated_text': ",""))
            respond=(respond.replace('"}',""))
            respond=(respond.replace('"',''))
            await message.channel.send( mention + ", " + respond)

# Run the Discord bot

bot.run('MTA3MzA0MDA1Njg2NjA1NDE3Ng.G3eG2M.9kSA836IZ8cwJrfApQ_KTZKnzuduYwqQzFRBfA')

