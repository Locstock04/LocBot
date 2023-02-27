import discord
from discord import app_commands
from discord.ext import commands

#Replace all of slashcogtest with desiered name, use ctrl + f

class slashcogtest(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

        @app_commands.command(
            name = "slashcogtestc",
            description = "This is for a test")

        async def slashcogtestc(
            self,
            ctx: discord.Interaction,
            testvalue : str,
            testvalue2: int) -> None:

            await ctx.response.send_message(f'Bleh {testvalue}, blah, {testvalue2}')

async def setup(client: commands.Bot) -> None:
    await client.add_cog(slashcogtest(client))
