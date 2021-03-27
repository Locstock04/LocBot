import discord
from discord.ext import commands
from random import randint

class dnd(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog dnd loaded')

    @commands.command()
    async def roll(self, ctx, sides: int = 20, times: int = 1):
        land = ''
        for dice in range(0, times):
            land += str(randint(1, sides))+'\n'
        await ctx.send(land)

def setup(client):
    client.add_cog(dnd(client))
