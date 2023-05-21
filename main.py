import openai
from environs import Env
import discord

env = Env()
env.read_env()

DC_TOKEN = env.str('DISCORD_TOKEN')
openai.api_key = env.str('OPEN_API_KEY')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(client.user.mention):
        user_message = message.content.replace(client.user.mention, '')
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=user_message.strip(),
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.2
        )
        await message.channel.send(response.choices[0].text.strip())


client.run(DC_TOKEN)
