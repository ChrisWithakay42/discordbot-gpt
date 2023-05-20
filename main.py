from environs import Env
import discord

env = Env()
env.read_env()

TOKEN = env.str('DISCORD_TOKEN')

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

    if message.content.startswith('@Tyrion Lannister'):
        await message.channel.send('Hello!')


client.run(TOKEN)
