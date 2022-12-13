import discord
from discord.ext import commands

class voicecontrol(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog voicecontrol ready')

    @commands.command()
    async def overridejoin(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command()
    async def overrideleave(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command(aliases=['listpeopleincall'])
    async def peopleincall(self, ctx):
        voiceid = ctx.author.voice.channel
        usersincall = voiceid.members
        print(usersincall)
        await ctx.send(usersincall)

    #@commands.has_permissions(mute_members=True)
    @commands.command(aliases=['muteall', 'm'])
    async def mutecall(self, ctx):
        print("Attempting to mute call")
        if ctx.author.voice and ctx.author.voice.channel:
            voiceid = ctx.author.voice.channel
            usersincall = voiceid.members
            print(f"Detected users in call are: {usersincall}")
            for i in range(0, len(usersincall)):
                user = usersincall[i]
                print(f'Muting user {i}: {user}')
                await user.edit(mute = True)
            await ctx.author.edit(mute = True)
        else:
            await ctx.send("You need to be inside a voice channel to use this!")
            return

    @commands.command(aliases=['unmuteall', 'u'])
    async def unmutecall(self, ctx):
        print("Attempting to unmute call")
        if ctx.author.voice and ctx.author.voice.channel:
            voiceid = ctx.author.voice.channel
            usersincall = voiceid.members
            print(usersincall)
            for i in range(0, len(usersincall)):
                user = usersincall[i]
                print(f'Unmuting user {i}: {user}')
                await user.edit(mute = False)
            await ctx.author.edit(mute = False)
        else:
            await ctx.send("You need to be inside a voice channel to use this!")
            return

    #@commands.has_permissions(deafen_members=True)
    @commands.command(aliases=['deafenall', 'd'])
    async def deafencall(self, ctx):
        if ctx.author.voice and ctx.author.voice.channel:
            voiceid = ctx.author.voice.channel
            usersincall = voiceid.members
            for i in range(0, len(usersincall)):
                user = usersincall[i]
                print(f'Deafening user {i}: {user}')
                await user.edit(deafen = True)
            await ctx.author.edit(deafen = True)
        else:
            await ctx.send("You need to be inside a voice channel to use this!")
            return

    @commands.command(aliases=['undeafenall', 'h', 'hear'])
    async def undeafencall(self, ctx):
        if ctx.author.voice and ctx.author.voice.channel:
            voiceid = ctx.author.voice.channel
            usersincall = voiceid.members
            for i in range(0, len(usersincall)):
                    user = usersincall[i]
                    print(f'undeafening user {i}: {usersincall[i]}')
                    await user.edit(deafen = False)
            await ctx.author.edit(deafen = False)
        else:
            await ctx.send("You need to be inside a voice channel to use this!")
            return

    #@commands.has_permissions(move_members=True)
    @commands.command(aliases=['moveall', 'ma, mc, move'])
    async def movecall(self, ctx, *, channel : discord.VoiceChannel):
        for members in ctx.author.voice.channel.members:
            print(f'Movine {members}')
            await members.move_to(channel)

    @commands.command()
    async def pingvoicecontrol(self, ctx):
        print('Cog voicecontrol is running')
        await ctx.send('Cog voicecontrol is running')

    #
    # @commands.command(aliases=['new mute all', 'new mute call', 'n'])
    # async def newmutecall(self, ctx):
    #     if ctx.author.voice and ctx.author.voice.channel:
    #         voiceid = ctx.author.voice.channel
    #         role = discord.utils.get(ctx.guild.roles, name='Kinda Sus')
    #         print(f'Changing voice channel {vocieid} perm of {role} to Speak=False')
    #         await voiceid.set_permissions(role, speak=False)
    #     else:
    #         await ctx.send("You need to be inside a voice channel to use this!")
    #         return
    #
    # @commands.command(aliases=['new unmute all', 'new unmute call', 'un'])
    # async def newunmutecall(self, ctx):
    #     if ctx.author.voice and ctx.author.voice.channel:
    #         voiceid = ctx.author.voice.channel
    #         role = discord.utils.get(ctx.guild.roles, name='Kinda Sus')
    #         print(f'Changing voice channel {vocieid} perm of {role} to Speak=True')
    #         await voiceid.set_permissions(role, speak=True)
    #     else:
    #         await ctx.send("You need to be inside a voice channel to use this!")
    #         return
    #



    # @commands.command(aliases=['vcid','voice'])
    # async def changevoiceid(self, ctx, channelid):
    #     # global voiceid
    #     # voiceid =   client.GetVoiceChannel(channelid)
    #     # print(f'Voice channel ID has been set to: {voiceid}')

    #VoiceUsers = Context. Guild.GetVoiceChannel(ID).Users;



async def setup(client):
    await client.add_cog(voicecontrol(client))
