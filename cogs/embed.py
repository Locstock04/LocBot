import discord
import math
from discord.ext import commands

boticon = 'https://cdn.discordapp.com/avatars/473818153663594497/237f64801e57651cb979672563761626.webp?size=128'
locicon = 'https://cdn.discordapp.com/avatars/327690857027207189/7002dda5b0824df4753bd3eb415c9c59.png?size=128'

emptyembed = discord.Embed(description = 'This text is required')

nofieldembed = discord.Embed(
    title = 'The title goes here'  ,
    description = 'A description can go here',
    colour = discord.Colour.green()
)
nofieldembed.set_author(name='This is for an author, but not only so, a picture can also be next to this', icon_url = locicon)
nofieldembed.set_thumbnail(url = locicon)
nofieldembed.set_image(url = boticon)
nofieldembed.set_footer(text='Heres some text at the bottom  ')

exampleembed = discord.Embed(
    title = 'The title goes here'  ,
    description = 'A description can go here',
    colour = discord.Colour.green()
)
exampleembed.set_author(name='This is for an author, but not only so, a picture can also be next to this', icon_url = locicon)
exampleembed.set_thumbnail(url = locicon)
exampleembed.set_image(url = boticon)
exampleembed.set_footer(text='Heres some text at the bottom  ')
exampleembed.add_field(name='here is a field', value='with a value over here', inline=False)
exampleembed.add_field(name='here is another field', value='which says this!', inline=False)

class embed(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog embed loaded')

    @commands.command()
    async def exampleembed(self, ctx):
        await ctx.send(embed=exampleembed)
        await ctx.send(embed=emptyembed)

    @commands.command()
    async def embed(self, ctx):
        await ctx.send(embed=embed)

    @commands.command()
    async def emptyembed(self, ctx):
        await ctx.send(embed=emptyembed)

    @commands.command()
    async def createembed(self, ctx, title, description, colour, author, authorimg, thumbnail, image, footer, *, fields):
        if (title != 'null'):
            tempembed = discord.Embed(
                title = title,
                description = description
                # Add code in the future for colours,
            )
        else:
            tempembed = discord.Embed(
                description = description
                # Add code in the future for colours,
            )

        if (authorimg == 'null'):
            if (author == 'null'):
                print()
            else:
                tempembed.set_author(name=author)
        else:
            if (author == 'null'):
                print()
            else:
                tempembed.set_author(name=author, icon_url=authorimg)

        if (thumbnail != 'null'):
            tempembed.set_thumbnail(url = thumbnail)
        if (image != 'null'):
            tempembed.set_image(url=image)
        if (footer != 'null'):
            tempembed.set_footer(text=footer)
        if (fields != 'null'):
            for i in range (0,(math.ceil(len(fields.split('^'))/2))):
                tempembed.add_field(name=fields.split('^')[2*i], value=fields.split('^')[(2*i)+1], inline=False)
        await ctx.send(embed=tempembed)


async def setup(client):
    await client.add_cog(embed(client))
