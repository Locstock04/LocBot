import discord
from discord.ext import commands

class shufflecall(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog shufflecall loaded')

    @commands.command(aliases=['shuffleall', 's all', 'sall'])
    async def shufflecall(self, ctx):
        print('Calling Shuffle call')
        if ctx.author.voice and ctx.author.voice.channel:
            voiceid = ctx.author.voice.channel
            print(f'Voice ID is: {voiceid}')
            usersincall = voiceid.members
            print(f'Members in call are {usersincall}')
            shuffledusers = random.shuffle(usersincall)
            print(f'Shuffled users are: {shuffledusers}')
            for i in range(0, len(usersincall)):
                user = usersincall[i]
                shuffleuser = shuffledusers[i]
                print(f'Sending a message to user {i}: {user}, They are playing as {shuffleuser}')
                await user.send(f'You will be playing as: {shuffleuser}')
            await ctx.author.edit(mute = False)
        else:
            await ctx.send("You need to be inside a voice channel to use this!")
            return

    @commands.command(aliases=['shuffle', 's'])
    async def suffle(self, ctx, number):
        if ctx.author.voice and ctx.author.voice.channel:
            voiceid = ctx.author.voice.channel
            usersincall = voiceid.members
            random.shuffle(usersincall)
            shuffledusers = random.shuffle(usersincall[:number])
            print(f'Shuffled users are: {shuffledusers}')
            shuffledusers.append(usersincall[number:])
            for i in range(0, len(usersincall)):
                user = usersincall[i]
                shuffleuser = shuffledusers[i]
                print(f'Sending a message to user {i}: {user}, They are playing as {shuffleuser}')
                await user.send(f'You will be playing as: {shuffleuser}')
            # await ctx.author.edit(mute = False)
        else:
            await ctx.send("You need to be inside a voice channel to use this!")
            return

def setup(client):
    client.add_cog(shufflecall(client))
