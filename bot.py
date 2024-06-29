import discord
from discord.ext import commands
from config.json import token

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.attachments:
        attachment = message.attachments[0]
        if attachment.url.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            await attachment.save(attachment.filename)

            # Envia a imagem para outro canal
            channel_id = #id_do_destinatário
            channel = bot.get_channel(channel_id)
            await channel.send(f'Imagem de {message.author}:', file=discord.File(attachment.filename))

    await bot.process_commands(message)

bot.run(token)