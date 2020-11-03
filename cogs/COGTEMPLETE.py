import discord
from discord.ext import commands

#Replace all of COGTEMPLETE with desiered name, use ctrl + f

class COGTEMPLETE(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog COGTEMPLETE loaded')

    @commands.command()
    async def COGTEMPLETEFUNCTION(self, ctx):
        print('Why are you calling this?')

def setup(client):
    client.add_cog(COGTEMPLETE(client))
