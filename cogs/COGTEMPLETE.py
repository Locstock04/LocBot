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

async def setup(client):
    await client.add_cog(COGTEMPLETE(client))



'''

cogs = []
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        cogs.append(f"cogs.{filename[:-3]}")

print(cogs)
async def load_extensions():
    for i in range(len(cogs)):            # cut off the .py from the file name
        await client.load_extension(f"cogs.{cogs[i]}")

'''
