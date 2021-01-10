import discord
from discord.ext import commands

p0 = '🟦'
p1 = '🔴'
p2 = '🟡'
pw = ''

board = [[p0] * 7] * 6
turn = False
lastmove = None
movelist = []


class connect(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog Connectfour ready')

    @commands.command(aliases=['cr'])
    async def cread(self, ctx):

        # IF CHANGING ANYTHING ABOUT THIS FUNCTION
        # BE SURE TO CHANGE IT IN RESET AND PLACE

        pic = '```'
        global board
        print(f'The Board is currently:\n{board}\n')
        for col in range(0, len(board[0])):
            pic += f'{col+1}{pw}'
        pic += '\n'
        for row in range(0, len(board)):
            current = list(board[row])
            print(f'Current is {current}')
            for col in range(0, len(board[row])):

                pic += str(current[col-1])
                pic += pw
            pic += '\n'
        print(f'\n\n{pic}')
        pic += '```'
        await ctx.send(pic)

    @commands.command(aliases=['cp'])
    async def cplace(self, ctx, placement):
        print('Running cplace')
        global board
        global turn
        global movelist
        Movedone = False
        attempt = int(placement)-2
        for row in range(0, len(board)):
            print(f'Checking row number {row}')
            if not Movedone:
                current = board[row]
                if row == len(board)-1:
                    future = ['T'] * len(board[row])
                else:
                    future = board[row+1]
                print(f'Current is: {current}')
                if current[attempt] != p0:
                    await ctx.send(f'Invalid placment! Please choose another row.')
                    print(f'Invalid placment! Please choose another row. Next: {future[attempt]}, This:{current[attempt]}')
                    return
                elif future[attempt] != p0:
                    temp = board[row].copy()
                    if turn:
                        temp[attempt] = p1
                    else:
                        temp[attempt] = p2
                    turn = not turn
                    board[row] = temp.copy()
                    print('Placed Piece')
                    # movelist.append([row, placement])
                    movelist.append(board)
                    Movedone = True
            else:
                print('Move done, skipping')

        # Code from read function

        pic = '```'
        print(f'The Board is currently:\n{board}\n')
        for col in range(0, len(board[0])):
            pic += f'{col+1}{pw}'
        pic += '\n'
        for row in range(0, len(board)):
            current = list(board[row])
            print(f'Current is {current}')
            for col in range(0, len(board[row])):
                pic += str(current[col-1])
                pic += pw
            pic += '\n'
        print(f'\n\n{pic}')
        pic += '```'
        await ctx.send(pic)

        print(movelist)



    @commands.command(aliases=['cu'])
    async def cundo(self, ctx):
        global board
        global movelist
        global turn
        if len(movelist) != 0:
            turn = not turn
            # lastmove = movelist.pop()
            # print(lastmove)
            # temp = board[lastmove[0]].copy()
            # temp[int(lastmove[1])] = p0
            # board[lastmove[0]] = temp.copy()
            board = movelist.pop()
        print(f'Undoing move at {lastmove}')


        # Code from read function

        pic = '``x`'
        print(f'The Board is currently:\n{board}\n')
        for col in range(0, len(board[0])):
            pic += f'{col+1}{pw}'
        pic += '\n'
        for row in range(0, len(board)):
            current = list(board[row])
            print(f'Current is {current}')
            for col in range(0, len(board[row])):
                pic += str(current[col-1])
                pic += pw
            pic += '\n'
        print(f'\n\n{pic}')
        pic += '```'
        await ctx.send(pic)


    @commands.command(aliases=['cs', 'cstart'])
    async def creset(self, ctx):
        pic = '```'
        global board
        global movelist
        board = [[p0] * 7] * 6
        for col in range(0, len(board[0])):
            pic += f'{col+1}{pw}'
        pic += '\n'
        for row in range(0, len(board)):
            current = list(board[row])
            for col in range(0, len(board[row])):
                pic += str(current[col-1])
                pic += pw
            pic += '\n'
        print(f'\n\n{pic}')
        pic += '```'
        movelist = []
        await ctx.send(pic)

    @commands.command()
    async def pingconnect(self, ctx):
        print('Cog connect is running')
        await ctx.send('Cog connect is running')


def setup(client):
    client.add_cog(connect(client))
