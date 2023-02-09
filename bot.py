

from nltk.corpus import words
from random_word import RandomWords
from tokens import *
import time
from paragraphs import paragraphs
from userFuncs import *
from urban import urbanFind
from lol import lol
from gif import getGIF
from findX import findX
from art import text2art
import random
from discord.ext import commands
import discord
from unicodedata import name
import re
from datetime import date
from xo import Board
import nltk
nltk.download('words')

help_command = commands.DefaultHelpCommand(
    no_category='Commands'
)


def isGIF(inp):
    x = inp.lower()
    pattern = re.compile(r"n!gif [a-zA-Z]+", re.IGNORECASE)
    return pattern.match(x) != None


def requestGIF(inp):
    newString = inp
    if getGIF(newString) != None:
        return getGIF(newString)


def isBatchest(inp):
    x = inp.lower()
    pattern = re.compile(r"i( hecking)? love [a-zA-Z]+")
    return pattern.match(x) != None


def wack(x):
    new = ''
    for i in range(len(x)):
        if i % 2 != 0:
            new += x[i].upper()
        else:
            new += x[i]
    return new


intents = discord.Intents.all()
client = commands.Bot(command_prefix='>',
                      help_command=help_command, intents=intents)


channel1 = client.get_channel(channelIdOld)


def generateXp():
    return 1


@client.command
async def test(ctx, arg):
    await ctx.send(arg)


@client.event
async def on_ready():
    print('Server moderator is now active')
    # await client.get_channel(channelIdnew).send("CMD is now online")


@client.event
async def on_message(message):
    # print(message)
    # if message.author.id == 430892547523608596:
    #     print(message.author)
    #     print(message.content)
    # await message.channel.send(wack(message.content))
    if message.author.id == 393614489649676289:
        await message.channel.send(wack(message.content))
    if message.content.lower() == 'another day':
        another_day()
    if isBatchest(message.content):
        x = random.uniform(0, 1)
        if x < 0.5:
            await message.channel.send("<:batchest:906314613312872448> <:batchest:906314613312872448> <:batchest:906314613312872448> <:batchest:906314613312872448>")
        else:
            await message.channel.send(requestGIF("batchest"))
    if message.content.lower() in ["why is my code broken", 'why doesnt my code work', 'my code is broken', 'my code doesnt work']:
        await message.channel.send("Its prolly written in JS")

    if message.author.bot:
        return
    if message.content.lower() == '?help':
        pass
    elif message.content.lower() == '?addrole':
        pass
    else:
        pass
    await client.process_commands(message)


@client.command(name='gif', help='Sends the top Tenor GIF search result of the inputed text')
async def gif(ctx, *words):
    print((words))
    print(' '.join(words))
    await ctx.channel.send(requestGIF(' '.join(words)))


@client.command(name='calc', help="Solves for a variable 'x' in basic linear mathematical equations")
async def calc(ctx, *formula):
    await ctx.channel.send(f"x = {findX(' '.join(formula))}")


@client.command(
    name="ping",
    help="Uses come crazy logic to determine if pong is actually the correct value or not.",

    brief="Prints pong back to the channel."
)
async def ping(ctx):
    print("pong")
    await ctx.channel.send("pong")


@client.command(name="inv", aliases=["inventory"], help='Shows user inventory')
async def inventory(ctx):
    embd = discord.Embed(title=f"{ctx.author.name}'s inventory", description=showInventory(
        ctx.author.id), color=discord.Color.blue())
    await ctx.channel.send(embed=embd)


@client.command(name="vault", help="Shows user's vault")
async def showVaultt(ctx):
    embd = discord.Embed(title=f"{ctx.author.name}'s vault", description=showVault(
        ctx.author.id), color=discord.Color.blue())
    await ctx.channel.send(embed=embd)


@client.command(name='mine', help="Mines a given amount of blocks")
@commands.cooldown(1, 10, commands.BucketType.user)
async def mine(ctx, depth: str):
    print(depth)
    print("MINED")
    val = ''
    if depth.isdigit():
        depth = int(depth)
        print(type(depth))
        if depth > 70:
            await ctx.channel.send("Maximum depth is 70 blocks")
        elif depth < 20:
            await ctx.channel.send("Minimum depth is 20 blocks")
        else:
            cobblestone = "cobblestone"
            diamond = "diamond"
            emerald = "emerald"
            gold = "gold"
            iron = "iron"
            gravel = "gravel"
            rand = random.randint(1, 1000)
            print(rand)
            if rand == 1000:
                newItem(ctx.message.author.id, diamond, depth - 20)
                newItem(ctx.message.author.id, cobblestone, depth - 20)
                val = f"You mined 20 diamond and {depth - 20} cobblestone"
            elif rand == 999:
                newItem(ctx.message.author.id, cobblestone, depth - 2)
                newItem(ctx.message.author.id, "platinum", 2)
                val = f"You mined {2} platinum ore and {depth - 2} cobblestone"
            elif rand in range(70):
                death(ctx.message.author.id)
                val = "RIP. You fell in lava and lost all your items"
            elif rand in range(70, 200):
                newItem(ctx.message.author.id, cobblestone, depth)
                val = "You only mined cobblestone. Sad."
            elif rand in range(200, 350):
                ironCount = random.randint(1, depth // 3)
                newItem(ctx.message.author.id,
                        cobblestone, (depth - ironCount))
                newItem(ctx.message.author.id, iron, ironCount)
                val = f"You mined {ironCount} iron ore and {depth - ironCount} cobblestone"
            elif rand in range(350, 600):
                ironCount = random.randint(1, depth//5)
                goldCount = random.randint(1, (depth - ironCount)//4)
                newItem(ctx.message.author.id, iron, ironCount)
                newItem(ctx.message.author.id, gold, goldCount)
                newItem(ctx.message.author.id, (cobblestone),
                        depth - ironCount - goldCount)
                val = f"You mined {ironCount} iron ore,{goldCount} gold ore and {depth - ironCount - goldCount} cobblestone"
            elif rand in range(600, 700):
                newItem(ctx.message.author.id, gravel, depth)
                val = f"What a loser. You somehow managed to find {depth} gravel..."
            elif rand in range(700, 840):
                ironCount = random.randint(1, depth//5)
                goldCount = random.randint(1, (depth - ironCount)//4)
                emeraldCount = random.randint(
                    1, (depth - ironCount - goldCount)//2)
                newItem(ctx.message.author.id, iron, ironCount)
                newItem(ctx.message.author.id, gold, goldCount)
                newItem(ctx.message.author.id, emerald, emeraldCount)
                newItem(ctx.message.author.id, cobblestone,
                        (depth - ironCount - goldCount - emeraldCount))
                val = f'you mined {ironCount} iron ore, {goldCount} gold ore, {emeraldCount} emerald ore and {depth - ironCount - goldCount - emeraldCount} cobblestone. Not Bad. '
            elif rand in range(840, 920):
                ironCount = random.randint(1, depth // 3)
                newItem(ctx.message.author.id, (gravel), depth - ironCount)
                newItem(ctx.message.author.id, iron, ironCount)
                val = f'You mined {ironCount} iron ore and {depth - ironCount} gravel'
            elif rand in range(920, 950):
                diamondCount = random.randint(1, 5)
                ironCount = random.randint(1, (depth - 6)//3)
                goldCount = random.randint(1, 5)
                newItem(ctx.message.author.id, iron, ironCount)
                newItem(ctx.message.author.id, gold, goldCount)
                newItem(ctx.message.author.id, diamond, diamondCount)
                newItem(ctx.message.author.id, cobblestone, depth -
                        ironCount - goldCount - diamondCount)
                val = f'Jeeez, you mined {ironCount} iron ore, {goldCount} gold ore, {diamondCount} diamonds, and {depth - ironCount - goldCount - diamondCount} gravel'
            else:
                diamondCount = random.randint(5, 8)
                goldCount = random.randint(3, 5)
                emeraldCount = 1
                ironCount = random.randint(
                    1, (depth - diamondCount - goldCount - emeraldCount)//3)
                newItem(ctx.message.author.id, iron, ironCount)
                newItem(ctx.message.author.id, gold, goldCount)
                newItem(ctx.message.author.id, diamond, diamondCount)
                newItem(ctx.message.author.id, emerald, emeraldCount)
                newItem(ctx.message.author.id, cobblestone, depth -
                        ironCount - goldCount - diamondCount - 1)
                val = f'SHEEEESH. You mined {ironCount} iron ore, {goldCount} gold ore, {diamondCount} diamonds, 1 emeralds and {depth - ironCount - goldCount - diamondCount - 1} gravel'
            embed = discord.Embed(
                title=f"{ctx.message.author.name}'s Mining Session", description=val, color=discord.Color.blue())
            await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(
            title=f"You can only mine a whole number of blocks...", description="Now wait for your next turn 😡", color=discord.Color.blue())
        await ctx.channel.send(embed=embed)


@mine.error
async def mine_error(ctx, error):

    if isinstance(error, commands.CommandOnCooldown):
        timeLeft: int = error.retry_after
        msg = f'Try again in {round(timeLeft)}s'
        embd = discord.Embed(title="Slow down there bro",
                             description=msg, color=discord.Color.red())
        await ctx.send(embed=embd)
    else:
        raise error


@client.command(name='wpm', help="Quick built in typing speed tester")
async def wpm(ctx):
    author = ctx.message.author
    sentence = random.choice(paragraphs)
    embd = discord.Embed(title="Typing speed test",
                         description="In 7 seconds, a paragraph will be send. Type it out and send it as fast as you can. Goodluck", color=discord.Color.green())
    await ctx.send(embed=embd)

    def check(m):
        return m.author == author
    time.sleep(7)
    await ctx.send(embed=discord.Embed(title="GO!", description=sentence))
    t = time.time()
    msg = await client.wait_for('message', check=check)
    totalTime = (time.time() - t)/60
    words = sentence.split(' ')
    msgWords = msg.content.split(' ')
    correctCount = 0
    for i in msgWords:
        if i in words:
            correctCount += 1
    print(f'correct = {correctCount}')
    print(f'len of words = {len(words)}')
    accuracy = (correctCount / len(words)) * 100
    wpm = correctCount // totalTime
    await ctx.send(embed=discord.Embed(title="Result", description=f"You have a typing speed of {wpm} wpm with an accuracy of {accuracy}% "))


@client.command(name='store', help="Sends a given amount of items to the user's vault")
async def store(ctx, item, amount):
    vaulting = vault(ctx.message.author.id, item.lower(), amount)
    if vaulting == None:
        embd = discord.Embed(title="Items moved to fault",
                             description=f'{amount} of your {item.lower()} have successfully vaulted.')
    else:
        embd = discord.Embed(title="Oops",
                             description=vaulting)

    await ctx.send(embed=embd)


@client.command(name='unvault', help="Returns given amount of vaulted items to the user's inventory")
async def unvaulter(ctx, item, amount):
    vaulting = unvault(ctx.message.author.id, item.lower(), amount)
    if vaulting == None:
        embd = discord.Embed(title="Items moved to inventory",
                             description=f'{amount} of your {item.lower()} have successfully unvaulted.')
    else:
        embd = discord.Embed(title="Oops",
                             description=vaulting)

    await ctx.send(embed=embd)


@client.command(name='sell', help="Sells a given amount of items")
async def sellCommand(ctx, item, amount='1'):
    prices = {'diamond': 20, 'emerald': 20, 'gold': 15,
              'cobblestone': 0, 'gravel': 0, 'iron': 5, 'platinum': 10000}
    transaction = sell(ctx.message.author.id, item.lower(), amount)
    if transaction == None:
        embd = discord.Embed(title='Your items have been sold',
                             description=f'You sold {amount} {item.lower()} for ${prices[item] * int(amount)} ')
    else:
        embd = discord.Embed(title="Oops",
                             description=transaction)
    await ctx.send(embed=embd)


@client.command(name='prices', help="Displays the prices of sellable items")
async def showPrice(ctx):
    prices = {'diamond': 20, 'emerald': 20, 'gold': 15,
              'cobblestone': 0, 'gravel': 0, 'iron': 5, 'platinum': 10000}
    val = ''
    for x, y in prices.items():
        val += f'{x}: {y}\n'

    embd = discord.Embed(title="Prices of sellable items",
                         description=val)
    await ctx.send(embed=embd)


@client.command(name='coinflip', aliases=['cf'], help="Bets a given amount of money on a simulated coin toss")
async def coin(ctx, guess, amount='1'):
    flip = coinFlip(ctx.message.author.id, guess, amount)
    if flip[1] == False:
        embd = discord.Embed(title='Oops', description=f'{flip[0]}')
    else:
        won = 'won' in flip[0].split(' ')
        if won:
            embd = discord.Embed(title='You won!', description=f'{flip[0]}')
        else:
            embd = discord.Embed(title='You lost:/', description=f'{flip[0]}')
    await ctx.send(embed=embd)


@client.command(name='balance', aliases=['bal', 'wallet'], help="Shows user's balance")
async def bal(ctx):
    embd = discord.Embed(title=f"{ctx.message.author.name}'s balance",
                         description=showBal(ctx.message.author.id))
    await ctx.send(embed=embd)


@client.command(name='stash', aliases=['money', 'hidden'], help="Shows user's hidden stash of money")
async def bal(ctx):
    embd = discord.Embed(title=f"{ctx.message.author.name}'s bank balance",
                         description=showBank(ctx.message.author.id))
    await ctx.send(embed=embd)


@client.command(name='steal', aliases=['STEAL,rob,ROB,st'], help="Robs the mentioned users balance")
@commands.cooldown(1, 10, commands.BucketType.user)
async def steal(ctx):
    users = ctx.message.mentions
    if len(users) == 0:
        embd = discord.Embed(title='No victim was mentioned <:monkaW:906311628637765642>',
                             description='Tag the person you want to rob')
    elif len(users) > 1:
        embd = discord.Embed(title='Bro...',
                             description='You can only rob one person at a time')
    else:

        rob = robbery(ctx.message.author.id, users[0].id)
        if type(rob) == str:
            embd = discord.Embed(title='Hmmm',
                                 description=rob)
        else:
            if rob[0]:
                embd = discord.Embed(title='Your heist was successful',
                                     description=f'You stole ${rob[1]} from {users[0].name}')
            else:
                embd = discord.Embed(title='Karma is a not very nice lady',
                                     description=f'Your heist failed... and you payed {users[0]} ${rob[1]}')
    await ctx.send(embed=embd)


@steal.error
async def steal_error(ctx, error):

    if isinstance(error, commands.CommandOnCooldown):
        timeLeft: int = error.retry_after
        msg = f'Try again in {round(timeLeft)}s'
        embd = discord.Embed(title="Slow down there bro",
                             description=msg, color=discord.Color.red())
        await ctx.send(embed=embd)
    else:
        raise error


@client.command(name="rich", aliases=['rankings', 'ranks', 'ladder', 'richest'], help="Displays order of wealth on the server")
async def rich(ctx):
    ranks = rankings()[::-1]
    val = ''
    for i in range(len(ranks)):
        usr = await client.fetch_user(ranks[i][0])
        userName = usr.name
        val += f"{i+1} - {userName} : {ranks[i][1]}\n"
    embd = discord.Embed(title="Current ladder",
                         description=val, color=discord.Color.blurple())
    await ctx.send(embed=embd)


@client.command(name='urban', help="Shows definition of a word in the urban dictionary")
async def urban(ctx, *names):
    embd = discord.Embed(
        title=f'{" ".join(names)}:', description=urbanFind(' '.join(names))['definition'])
    await ctx.send(embed=embd)


@client.command(name='bank', help="Deposits a given amount of money into a user's hidden stash of cahs")
async def bank(ctx, amount):
    transfer = bankHelp(ctx.message.author.id, amount)
    if transfer == None:
        embd = discord.Embed(title="Transfer success",
                             description=f'You have successfully deposited {amount} into the bank')
    else:
        embd = discord.Embed(title='Oops', description=transfer)
    await ctx.send(embed=embd)


@client.command(name='league', help="Shows base stats about a given champ")
async def league(ctx, name):
    info = lol(name)
    if info != "Invalid champion name":
        stats = ''
        for x, y in info.items():
            stats += f'{x}: {y} \n'
            embd = discord.Embed(
                title=f"{info['Name']}'s base stats", description=stats)

    else:
        stats = "Invalid champion name"
        embd = discord.Embed(
            title="Invalid champion name", description='Oops')
    await ctx.send(embed=embd)


@client.command(name='art', help="turns a message into ascii art")
async def art(ctx, *guess):
    sentence = ' '.join(guess)

    message = text2art(sentence)
    message = message.replace('|', 'I')
    message = message.replace('`', "'")
    await ctx.message.delete()
    await ctx.send("`" + message + "`")


@client.command(name='another', help='Counts how many times okok123 has said "Another day"')
async def another(ctx, *guess):
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    embd = discord.Embed(
        title="Another day count", description=f'As of {d2}, okok123 has said another day {another_count()} times')
    await ctx.send(embed=embd)


@client.command(name='donate', help='Donates a certain amount of moeny to another use')
async def give(ctx, reciever, amount):
    users = ctx.message.mentions
    x = donate(ctx.message.author, users[0].id, amount)
    if type(x) == str:
        await ctx.send(embed=discord.Embed(title="Oops", description=x))
    else:
        await ctx.send(embed=discord.Embed(title="What a generous soul", description=f"You've donated ${amount} to {users[0].id} "))


@client.command(name='wordle', help='Wordle.... but for discord')
async def wordle(ctx, guess):
    if len(guess) != 5:
        await ctx.reply(embed=discord.Embed(
            title=f'Bossman', description='The word must be 5 letters long'))
    elif guess not in words.words():
        await ctx.reply(embed=discord.Embed(
            title=f'Bossman', description='The word needs to actually be a word'))
    else:
        number = get_current_player_wordle()
        if get_word_wordle() == "":
            r = RandomWords()
            word = r.get_random_word(
                minLength=5, maxLength=5, hasDictionaryDef=True)
            word = word.lower()
            set_word_wordle(word)
        else:
            word = get_word_wordle()
        if guess == word:
            set_word_wordle("")
            await ctx.send(embed=discord.Embed(title="You win!", description="You guessed the word correctly"))
            set_current_player_wordle(6)
        else:
            if number > 1:
                reply = ""
                for i in range(len(guess)):
                    if word[i] == guess[i]:
                        reply += '🟩 '
                    elif guess[i] in word:
                        reply += '🟨 '
                    else:
                        reply += '🟥 '
                await ctx.reply(embed=discord.Embed(title=f'Guess number {7 - number}', description=reply))
                number -= 1
                set_current_player_wordle(number)
            else:
                await ctx.reply(embed=discord.Embed(title='You lose:(', description=f"The word was {word} :/"))
                set_word_wordle("")
                set_current_player_wordle(6)

        print(word)

players = []
board = Board()


@client.command(name='xo', aliases=['tictactoe', 'ttt'],  help='TicTacToe on discord')
async def xo(ctx, *guess):
    global players
    global board
    if players == [] and len(guess) != 2:
        await ctx.reply(embed=discord.Embed(title='Invalid command', description="Please tag someon you wish to play against followed by your initial play (ex. >xo @JohnDoe b3)"))
        return
    elif players != [] and ctx.message.author.id not in players:
        await ctx.reply(embed=discord.Embed(title='Wait your turn', description=f"A match is currently ongoing between { client.fetch_user(players[0])} and { client.fetch_user(players[0])}"))
        return
    elif players != [] and len(guess) != 1:
        await ctx.reply(embed=discord.Embed(title='Invalid command', description="Please enter the position you wish to play at (ex. >xo b3)"))
        return
    else:
        if players == []:
            users = ctx.message.mentions
            if len(users) == 0:
                await ctx.reply(embed=discord.Embed(title='Invalid command', description="Please tag someon you wish to play against followed by your initial play (ex. >xo @JohnDoe b3)"))
                return

            players.append(ctx.message.author.id)
            players.append(users[0].id)

        else:
            if len(guess) == 2:
                board.move(guess[1])
            else:
                board.move(guess[0])

            await ctx.reply(f'`{str(board)}`')
            if board.hasTie():
                await ctx.reply(embed=discord.Embed(title='Tie Game', description="The game ended in a draw"))
                players = []
            elif board.hasWin()[0]:
                if board.hasWin()[1] == 'X':
                    winner = await client.fetch_user(players[0])
                else:
                    winner = await client.fetch_user(players[1])
                await ctx.reply(embed=discord.Embed(title='WOO', description=f"The winner is {winner}!"))
                players = []
client.run(tokenNew)
