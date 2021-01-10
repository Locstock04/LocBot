import random
import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
client.remove_command('help')
#quotes = ['I did not forgot where the body was', 'Kimy is kind of sus']
#quotes.append('*Comms get sabotaged* You all know who to vote')
quotes = ['#Tessaragequit']

activity = discord.Game(name=random.choice(quotes))

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print(f'Loading {extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    print(f'Unloading {extension}')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print(f'Reloading {extension}')

@client.command()
async def changestatusto(ctx, *newstatus):
    activity = discord.Game(name=' '.join(newstatus))
    await client.change_presence(status=discord.Status.online, activity=activity)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
    print('Bot is ready.')

    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Some Custom Beats'))

    await client.change_presence(status=discord.Status.online, activity=activity)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def testmessage(ctx):
    print(f'Testing message send, hello {ctx.author.name}')
    await ctx.author.send(f'Testing message send, hello {ctx.author.name}')

@client.command(aliases=['listpeopleincall'])
async def peopleincall(ctx):
    voiceid = ctx.author.voice.channel
    usersincall = voiceid.members
    print(usersincall)
    await ctx.send(usersincall)

@client.event
async def on_voice_state_update(member, before, after):
    print(f'Member: {member}')
    print(f'Before: {before}')
    print(f'Afterr: {after}')
    if before.channel is None and after.channel is not None:
        print('searching for voice-log')
        for channel in client.get_all_channels():
            if channel.name == 'voice-log':
                await channel.send(f'Hello {member.mention} you joined a voice channel ')

    if before.channel is not None and after.channel is None:
        print('searching for voice-log')
        for channel in client.get_all_channels():
            if channel.name == 'voice-log':
                await channel.send(f'Bye {member.mention} you left a voice channel ')

token = open("..\locbottoken.txt", "r")
client.run(token.read())
