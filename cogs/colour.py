import discord
from discord.ext import commands
from PIL import Image #, ImageDraw, ImageFont

savepath = open("..\coloursavepath.txt", "r")
savepath = (savepath.read()+'\colour.png').replace('\\\\', '\\')

class colour(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog Colour loaded')

    @commands.command()
    async def colour(self, ctx, *, info = '#36393E'):
        rgb = [0, 0, 0]
        if info[0] == '#': info = info[1:]
        if info.count(' ') == 2:
            rgb = info.split()
            for c in range(0, len(rgb)): rgb[c] = int(rgb[c])
        elif len(info) == 6:
            for c in range(len(rgb)): rgb[c] = int(info[c*2] + info[c*2+1], 16)
        elif len(info) == 3:
            for c in range(len(rgb)): rgb[c] = int(2*info[c], 16)
        img = Image.new('RGB', (128, 128), color = (rgb[0], rgb[1], rgb[2]))
        img.save(savepath)

        colourembed = discord.Embed(colour = discord.Colour.from_rgb(rgb[0], rgb[1], rgb[2]))
        colourembed.set_thumbnail(url = "attachment://colour.png")
        colourembed.add_field(name='Hex', value=f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}', inline=False)
        colourembed.add_field(name='RGB', value=f'{rgb[0]}, {rgb[1]}, {rgb[2]}', inline=False)

        file = discord.File(savepath, filename = 'colour.png')
        await ctx.send(file=file, embed=colourembed)

async def setup(client):
    await client.add_cog(colour(client))
