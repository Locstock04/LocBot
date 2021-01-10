import discord
from discord.ext import commands


turn = False
movelist = []
c0 = '⬛'
c1 = '🟢'
c2 = '🟣'
cw = ''
board = [c0, c0, c0, c0, c0, c0, c0, c0, c0]
lastmove = None


class Tictactoe(commands.Cog):


    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog Tictactoe loaded')

    @commands.command()
    async def tread(self, ctx):
        global board
        print(f'```{board[0]}{cw}{board[1]}{cw}{board[2]}\n{board[3]}{cw}{board[4]}{cw}{board[5]}\n{board[6]}{cw}{board[7]}{cw}{board[8]}```')
        await ctx.send(f'```{board[0]}{cw}{board[1]}{cw}{board[2]}\n{board[3]}{cw}{board[4]}{cw}{board[5]}\n{board[6]}{cw}{board[7]}{cw}{board[8]}```')

    @commands.command()
    async def tplace(self, ctx, placement):
        global board
        global turn
        global movelist
        placement = int(placement)
        if board[placement-1] == c0:
            if turn:
                board[placement-1] = c1
            else:
                board[placement-1] = c2
            turn = not turn
            movelist.append(board)
            print(f'```{board[0]}{cw}{board[1]}{cw}{board[2]}\n{board[3]}{cw}{board[4]}{cw}{board[5]}\n{board[6]}{cw}{board[7]}{cw}{board[8]}```')
            await ctx.send(f'```{board[0]}{cw}{board[1]}{cw}{board[2]}\n{board[3]}{cw}{board[4]}{cw}{board[5]}\n{board[6]}{cw}{board[7]}{cw}{board[8]}```')
        else:
            print('Error, piece already placed there. Type .tundo to undo a move')
            await ctx.send('Error, piece already placed there. Type .tundo to undo a move')

    @commands.command()
    async def treset(self, ctx):
        global board
        board = [c0, c0, c0, c0, c0, c0, c0, c0, c0]
        global movelist
        print(f'```{board[0]}{cw}{board[1]}{cw}{board[2]}\n{board[3]}{cw}{board[4]}{cw}{board[5]}\n{board[6]}{cw}{board[7]}{cw}{board[8]}```')
        await ctx.send(f'```{board[0]}{cw}{board[1]}{cw}{board[2]}\n{board[3]}{cw}{board[4]}{cw}{board[5]}\n{board[6]}{cw}{board[7]}{cw}{board[8]}```')
        movelist = []

    @commands.command()
    async def tundo(self, ctx):
        global board
        global movelist
        global turn
        if len(movelist) != 0:
            turn = not turn
            board = movelist.pop()
        print(f'```{board[0]}{cw}{board[1]}{cw}{board[2]}\n{board[3]}{cw}{board[4]}{cw}{board[5]}\n{board[6]}{cw}{board[7]}{cw}{board[8]}```')
        await ctx.send(f'```{board[0]}{cw}{board[1]}{cw}{board[2]}\n{board[3]}{cw}{board[4]}{cw}{board[5]}\n{board[6]}{cw}{board[7]}{cw}{board[8]}```')



    @commands.command()
    async def pingtictactoe(self, ctx):
        print('Cog Tictactoe is running')
        await ctx.send('Cog Tictactoe is running')

def setup(client):
    client.add_cog(Tictactoe(client))
