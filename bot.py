import discord
import discord.client
import responses

async def print_response(message, user_message, is_private):
    try:
        response = responses.make_response(user_message)
        
        await message.author.send(response) if is_private else await message.channel.send(response)
        
    except Exception as e:
        print(e)

def run_discord_bot():
    Token = 'MTA4MTMyMzY0NjI0MjU0MTY2OQ.G6j3-T.EyXRdp7NUXkV9KDikF7K19aERFJHr5m_D2MKJw'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents = intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    # return what user said to console
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        # if (?) inputted, send response to user privately
        if user_message[0] == '?':
            user_message = user_message[1:]
            await print_response(message, user_message, is_private=True)
        else:
            await print_response(message, user_message, is_private=False)

    client.run(Token)
