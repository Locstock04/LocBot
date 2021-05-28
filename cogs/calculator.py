import discord
from discord.ext import commands

#Replace all of COGTEMPLETE with desiered name, use ctrl + f

def add(nums):
    total = 0
    for num in nums:
        total += num
    return total

def div(nums):
    total = 0
    for num in nums:
        total = total/num
    return total

def mul(nums):
    total = 0
    for num in nums:
        total *= num
    return total

def sub(nums):
    total = 0
    for num in nums:
        total -= num
    return total



class calculator(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog calculator loaded')

    @commands.command()
    async def cal(self, ctx, *, stuffs):
        print('add calc stuff')

def setup(client):
    client.add_cog(calculator(client))
