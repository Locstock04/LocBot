import discord
from discord.ext import commands
from datetime import datetime

'''
https://discordpy.readthedocs.io/en/stable/api.html?highlight=on_voice_state_update#voicestate
'''

class voiceactivity(commands.Cog):


    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog voiceactivity loaded')

    '''
    @commands.Cog.listener()
    async def on_message(self, message):
        print(message)
    '''



    @commands.Cog.listener()
    async def on_voice_state_update(self, member, b, a):
        # print(f'\nTime is: {datetime.now()}')
        '''
        b_afk = b.afk
        b_channel = b.channel
        b_deaf = b.deaf
        b_mute = b.mute
        b_requested_to_speak_at = b.requested_to_speak_at
        b_self_deaf = b.self_deaf
        b_self_mute = b.self_mute
        b_self_stream = b.self_stream
        b_self_video = b.self_video
        b_supress = b.suppress
        '''
        VcAts = {
            0: 'afk',
            1: 'channel',
            2: 'deaf',
            3: 'mute',
            4: 'requested_to_speak_at',
            5: 'self_deaf',
            6: 'self_mute',
            7: 'self_stream',
            8: 'self_video',
            9: 'supress'}

        b_ = [b.afk, b.channel, b.deaf, b.mute, b.requested_to_speak_at, b.self_deaf, b.self_mute, b.self_stream, b.self_video, b.suppress]
        a_ = [a.afk, a.channel, a.deaf, a.mute, a.requested_to_speak_at, a.self_deaf, a.self_mute, a.self_stream, a.self_video, a.suppress]

        #print(b_)

        #print(VcAts[1])
        print('\n')
        print(member)
        for i in range(0, len(b_)):
            if(not b_[i]==a_[i]):
                print(VcAts[i])
                print(b_[i])
                print(a_[i])

        temp = str(b).replace('<VoiceState ','')
        temp = temp.replace('self_mute=','Self mute=')
        temp = temp.replace(' self_deaf=', '\nSelf Deafen=')
        temp = temp.replace(' self_stream=', '\nStreaming=')
        temp = temp.replace(' suppress=', '\nSurpressed=')
        temp = temp.replace(' requested_to_speak_at=', '\nRequested to speak at=')
        temp = temp.replace(' channel=', '\nVoice Channel=')

        beforetext = temp.split('\n')


        temp = str(a).replace('<VoiceState ','')
        temp = temp.replace('self_mute=','Self mute=')
        temp = temp.replace(' self_deaf=', '\nSelf Deafen=')
        temp = temp.replace(' self_stream=', '\nStreaming=')
        temp = temp.replace(' suppress=', '\nSurpressed=')
        temp = temp.replace(' requested_to_speak_at=', '\nRequested to speak at=')
        temp = temp.replace(' channel=', '\nVoice Channel=')

        aftertext = temp.split('\n')

        '''
        print()
        print(f'Member: {member}')
        for i in range(0, len(beforetext)):
            if not beforetext[i]==aftertext[i]:
                print(f'{beforetext[i]}\n{aftertext[i]}')
        '''

        # print(f'Afterr: {a}')
        # Joining call
        if b.channel is None and a.channel is not None:
            # print('searching for voice-log')
            gld = a.channel.guild
            for channel in gld.text_channels:
                if channel.name == '｜voice-log':
                    await channel.send(f'Hey {member.mention} you joined \'{a.channel}\'')
        # Moving call
        if b.channel is not None and a.channel is not None:
            if b.channel is not a.channel:
                # print('searching for voice-log')
                gld = a.channel.guild
                for channel in gld.text_channels:
                    if channel.name == '｜voice-log':
                        await channel.send(f'Cya {member.mention} you moved from \'{b.channel}\' to \'{a.channel}\'')
        # Leaving call
        if b.channel is not None and a.channel is None:
            # print('searching for voice-log')
            gld = b.channel.guild
            for channel in gld.text_channels:
                if channel.name == '｜voice-log':
                    await channel.send(f'Bye {member.mention} you left \'{b.channel}\'')


async def setup(client):
    await client.add_cog(voiceactivity(client))



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
