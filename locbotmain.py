import discord
import os
from datetime import datetime
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
async def load(ctx, extension):
    print(f'Loading {extension}')
    client.load_extension(f'cogs.{extension}')
    print(f'Loaded {extension}')

@client.command()
async def unload(ctx, extension):
    print(f'Unloading {extension}')
    client.unload_extension(f'cogs.{extension}')
    print(f'Unloaded {extension}')

@client.command()
async def reload(ctx, extension):
    print(f'Reloading {extension}')
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print(f'Reloaded {extension}')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def testmessage(ctx):
    print(f'Testing message send, hello {ctx.author.name}')
    await ctx.author.send(f'Testing message send, hello {ctx.author.name}')

@client.event
async def on_voice_state_update(member, before, after):
    print(f'\nTime is: {datetime.now()}')
    print(f'Member: {member}')
    print(f'Before: {before}')
    print(f'Afterr: {after}')
    # Joining call
    if before.channel is None and after.channel is not None:
        # print('searching for voice-log')
        gld = after.channel.guild
        for channel in gld.text_channels:
            if channel.name == '｜voice-log':
                await channel.send(f'Hey {member.mention} you joined \'{after.channel}\'')
    # Moving call
    if before.channel is not None and after.channel is not None:
        if before.channel is not after.channel:
            # print('searching for voice-log')
            gld = after.channel.guild
            for channel in gld.text_channels:
                if channel.name == '｜voice-log':
                    await channel.send(f'Cya {member.mention} you moved from \'{before.channel}\' to \'{after.channel}\'')
    # Leaving call
    if before.channel is not None and after.channel is None:
        # print('searching for voice-log')
        gld = before.channel.guild
        for channel in gld.text_channels:
            if channel.name == '｜voice-log':
                await channel.send(f'Bye {member.mention} you left \'{before.channel}\'')


token = open("..\locbottoken.txt", "r")
client.run(token.read())
