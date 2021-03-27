import discord
from discord.ext import commands

class moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog moderation loaded')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, * , reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} has been kicked by {ctx.author.mention}')
        print(f'{member.mention} has been kicked by {ctx.author.mention}')
    # @kick.error
    # async def kick_error(self, error, ctx):
    #    if isinstance(error, commands.MissingPermissions):
    #        await ctx.send("You don't have permission to kick!")
    #        print(f'{ctx.author.mention} has attempted to kick')


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, * , reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} has been banned by {ctx.author.mention}')
        print(f'{member.mention} has been kicked by {ctx.author.mention}')


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        if amount > 50:
            amount = 50
        await ctx.channel.purge(limit=amount)

    @commands.command()
    async def sendmessage(self, ctx, channelid: discord.TextChannel, * , message=''):
        await channelid.send(message)



def setup(client):
    client.add_cog(moderation(client))
