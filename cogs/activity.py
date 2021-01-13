import discord
import random
from discord.ext import commands

#quotes = ['I did not forgot where the body was', 'Kimy is kind of sus']
#quotes.append('*Comms get sabotaged* You all know who to vote')
quotes = ['#Tessaragequit']

currentactivity = discord.Game(name=random.choice(quotes))
currentpresence = discord.Status.online

class activity(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog activity loaded')
        await self.client.change_presence(presence=currentpresence,activity=currentactivity)

    @commands.command()
    async def status(self, ctx, mode, *newstatus):
        global currentactivity

        mode.lower()
        if newstatus == ():
            newstatus = ('', mode, ' ')
            mode = 'playing'

        print(f'Changed status to {mode} ' + ' '.join(newstatus))

        if mode == 'playing':
            activity = discord.Game(name=' '.join(newstatus))
        elif mode == 'listening':
            activity = discord.Activity(type=discord.ActivityType.listening, name=' '.join(newstatus))
        elif mode == 'watching':
            activity = discord.Activity(type=discord.ActivityType.watching, name=' '.join(newstatus))
        elif mode == 'streaming':
            activity = discord.Streaming(name='something ', url=newstatus)
        else:
            activity = discord.Game(name=str(mode)+' '+' '.join(newstatus))
            # activity = discord.Streaming(name=' '.join(newstatus), url=my_twitch_url)

        currentactivity = activity
        await self.client.change_presence(status=currentpresence,activity=activity)


    @commands.command()
    async def presence(self, ctx, presence):
        global currentpresence

        oldpresence = currentpresence
        
        if presence == 'online':
            newpresence = discord.Status.online
        elif presence == 'idle' or presence == 'away' or presence == 'afk':
            newpresence = discord.Status.idle
        elif presence == 'busy' or presence == 'dnd':
            newpresence = discord.Status.dnd
        else:
            newpresence = oldpresence
        currentpresence = newpresence
        await self.client.change_presence(status=newpresence,activity=currentactivity)

def setup(client):
    client.add_cog(activity(client))
