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
        messages = [{"role": "user", "content": user_message}]
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
            temperature=0
        )
        await message.channel.send(response.choices[0].message['content'])


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


client.run(DC_TOKEN)
