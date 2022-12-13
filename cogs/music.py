import discord
from discord.ext import commands
import youtube_dl
import ffmpeg
import os

class music(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog music loaded')

    @commands.command()
    async def play(self, ctx, url : str):
        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing music to end or use the 'stop' command")
            return

        voiceChannel = ctx.author.voice.channel
        await voiceChannel.connect()
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
            if file.endswith(".m4a"):
                os.rename(file, "song.mp3")
            if file.endswith(".webm"):
                os.rename(file, "song.mp3")
        voice.play(discord.FFmpegPCMAudio("song.mp3"))
        # voice.play(discord.FFmpegPCMAudio(executable="D:\ffmpeg-2022-09-19-git-4ba68639ca-full_build\bin\ffmpeg.exe", source="song.mp3"))

    @commands.command()
    async def leave(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()
        else:
            await ctx.send("Not connected to a voice channel.")

    @commands.command()
    async def pause(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("Currently no audio is playing.")

    @commands.command()
    async def resume(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("The audio is not paused.")

    @commands.command()
    async def stop(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        voice.stop()

async def setup(client):
    await client.add_cog(music(client))
