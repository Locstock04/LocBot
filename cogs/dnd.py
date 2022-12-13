import discord
from discord.ext import commands
from random import randint

class dnd(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog dnd loaded')

    @commands.command(aliases=['dice'])
    async def roll(self, ctx, sides: int = 20, times: int = 1):
        land = ''
        for dice in range(0, times):
            land += str(randint(1, sides))+'\n'
        await ctx.send(land)

    @commands.command(aliases=['coinflip', 'flipcoin'])
    async def coin(self, ctx, times: int = 1):
        land = ''
        for flip in range(0, times):
            if randint(0,1) == 0:
                land += f'{flip+1}: Tails\n'
            else:
                land += f'{flip+1}: Heads\n'
        await ctx.send(land)

async def setup(client):
    await client.add_cog(dnd(client))
