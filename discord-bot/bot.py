import responses
import discord
import os 


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        if message.channel.name == 'general':
            await message.author.send(response) if is_private else await       message.channel.send(response)

    except Exception as e:
        print(e)


def run():
    TOKEN = os.getenv('TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'Logged in as {client.user}')

    @client.event
    async def on_message(msg):
        if msg.author == client.user:
            return
        username = str(msg.author)
        user_msg = str(msg.content)
        channel = str(msg.channel)
        print(f'{username} said : {user_msg} at channel {channel}')

        await send_message(msg, user_msg, False)

    client.run(TOKEN)
