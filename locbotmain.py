import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import os
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = '.',intents=intents)
client.remove_command('help')


#client = discord.Client(intents=intents)
#tree = app_commands.CommandTree(client)




cogs = []
async def load_extensions():
    global cogs
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await client.load_extension(f"cogs.{filename[:-3]}")
            cogs.append(f"cogs.{filename[:-3]}")

MY_GUILD_ID = discord.Object(443290183274856468)
@client.tree.command(name = "test", description = "testing application Command")
@app_commands.guilds(MY_GUILD_ID) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction: discord.Interaction):
    await interaction.response.send_message("Hello!")


@client.tree.command(name = "testing", description = "testing global application Command")
async def second_command(interaction: discord.Interaction):
    await interaction.response.send_message("Hello World!")


@client.command()
async def checkallcogs(ctx, extension):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def load(ctx, extension):
    print(f'Loading {extension}')
    await client.load_extension(f'cogs.{extension}')
    # await client.cog_load(f'cogs.{extension}')
    print(f'Loaded {extension}')


@client.command()
async def unload(ctx, extension):
    print(f'Unloading {extension}')
    await client.unload_extension(f'cogs.{extension}')
    print(f'Unloaded {extension}')

@client.command()
async def reload(ctx, extension):
    print(f'Reloading {extension}')
    await client.unload_extension(f'cogs.{extension}')
    await client.load_extension(f'cogs.{extension}')
    # await client.cog_unload(f'cogs.{extension}')
    # await client.cog_load(f'cogs.{extension}')
    print(f'Reloaded {extension}')

@client.event
async def on_ready():
    print('Bot is nearly ready 1.')
    await client.tree.sync()
    print('Bot is nearly ready 2.')
    await client.tree.sync(guild=discord.Object(id=443290183274856468))
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def testmessage(ctx):
    print(f'Testing message send, hello {ctx.author.name}')
    await ctx.author.send(f'Testing message send, hello {ctx.author.name}')


token = open("..\locbottoken.txt", "r")

async def main():
    async with client:
        # client.loop.create_task(background_task())
        await load_extensions()
        print('Bot has loaded extensions.')
        await client.start(token.read())
        print('Bot has started.')
        #await client.tree.sync()
        #print('Bot synced tree.')
        #await client.tree.sync(guild=discord.Object(id=443290183274856468))
        #print('Bot synced guild app commands.')

asyncio.run(main())

# client.run(token.read())
