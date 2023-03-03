import discord
import discord.client
import responses

async def print_response(message, user_message, is_private):
    try:
        response = responses.make_response(user_message)
        
        if (is_private):
            await message.author.send(response)
        else:
            await message.channel.send(response)
        
    except Exception as e:
        print(e)

def run_discord_bot():
    Token = 'MTA4MTMyMzY0NjI0MjU0MTY2OQ.G_iYqa.FH6UyZoLWWq2JkJyd0Ohdy8-kuH_Gm4Xxux13I'
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    client.run(Token)