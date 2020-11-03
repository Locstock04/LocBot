import discord
from discord.ext import commands

boticon = 'https://cdn.discordapp.com/avatars/473818153663594497/237f64801e57651cb979672563761626.webp?size=128'
locicon = 'https://cdn.discordapp.com/avatars/327690857027207189/7002dda5b0824df4753bd3eb415c9c59.png?size=128'

# Default help help
helpembed = discord.Embed(
    title = 'This is Loc Bot; A Bot by Loc'  ,
    description = 'This bot can do many things, and even more are planned.\nTo get help with commands please be more specific and use one of the help commands below',
    colour = discord.Colour.green()
)
helpembed.set_author(name='LocBot', icon_url = boticon)
helpembed.set_thumbnail(url = locicon)
helpembed.set_image(url = boticon)
helpembed.set_footer(text='This bot was made by Locstock04  ')

helpembed.add_field(name='.ping', value='Returns the latency', inline=False)
helpembed.add_field(name='.help', value='Displays this!', inline=False)
helpembed.add_field(name='.help voice', value='Displays help for voice chat', inline=False)
helpembed.add_field(name='.help tictactoe', value='Displays help for Tic Tac Toe', inline=False)


# Voice help
vcembed = discord.Embed(
    title = 'This is Loc Bot; A Bot by Loc',
    colour = discord.Colour.green(),
    description = 'Below are commands that affect all the users within a Voice chat'
)
vcembed.set_author(name='LocBot', icon_url = boticon)
vcembed.set_thumbnail(url = locicon)
vcembed.set_image(url = boticon)
vcembed.set_footer(text='This bot was made by Locstock04  ')

vcembed.add_field(name='MUTE COMMANDS', value='For vc', inline=False)

vcembed.add_field(name='.mutecall', value='Mutes all in call Also: \n.m', inline=True)
vcembed.add_field(name='.unmutecall', value='Unmutes all in call Also: \n.u', inline=True)

vcembed.add_field(name='DEAFEN COMMMANDS', value='Make people deaf!\n', inline=False)

vcembed.add_field(name='.deafencall', value='Deafens all in call Also: \n.d', inline=True)
vcembed.add_field(name='.undeafencall', value='Undeafens all in call Also: \n.h', inline=True)

vcembed.add_field(name='OTHER VC COMMANDS', value='Other Stuff', inline=False)

vcembed.add_field(name='movecall', value='Moves all to another calll Also: \n.mc \n.move', inline=True)


# Tic Tac Toe help
tttembed = discord.Embed(
    title = 'This is Loc Bot; A Bot by Loc',
    colour = discord.Colour.green(),
    description = 'Here are commands for playing tic tac toe'
)
tttembed.set_author(name='LocBot', icon_url = boticon)
tttembed.set_thumbnail(url = locicon)
tttembed.set_image(url = boticon)
tttembed.set_footer(text='This bot was made by Locstock04  ')

tttembed.add_field(name='.tread', value='View the board without making a move', inline=False)
tttembed.add_field(name='.tplace <place>', value='Place a piece somewhere on the board, place counts from 1-9 top-left to right (Eg for x middle: .tplace x 5)', inline=False)
tttembed.add_field(name='.treset', value='Resets the game board', inline=False)



# Tic Tac Toe help
connectembed = discord.Embed(
    title = 'This is Loc Bot; A Bot by Loc',
    colour = discord.Colour.green(),
    description = 'Here are commands for playing tic tac toe'
)
connectembed.set_author(name='LocBot', icon_url = boticon)
connectembed.set_thumbnail(url = locicon)
connectembed.set_image(url = boticon)
connectembed.set_footer(text='This bot was made by Locstock04  ')

connectembed.add_field(name='.cread', value='View the board without making a move', inline=False)
connectembed.add_field(name='.cplace <piece> <place>', value='Place a piece somewhere on the board, place counts from 1-9 top-left to right (Eg for x middle: .tplace x 5)', inline=False)
connectembed.add_field(name='.treset', value='Resets the game board', inline=False)






class help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog help loaded')

    @commands.command()
    async def help(self, ctx, helptopic='none'):
        author = ctx.message.author

        if helptopic == 'voice' or helptopic == 'vc':
            await ctx.send(embed=vcembed)
        elif helptopic == 'tictactoe':
            await ctx.send(embed=tttembed)
        else:
            await ctx.send(embed=helpembed)

        # await author.send(embed=helpembed)
        # await ctx.send('A help message has been sent to your private messages')


def setup(client):
    client.add_cog(help(client))
