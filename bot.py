
from os import name
import re
import discord
from discord.ext import commands
import random
from findX import findX
import gif
import random
from urban import urbanFind
from userFuncs import *
from paragraphs import paragraphs
import time
from tokens import *


help_command = commands.DefaultHelpCommand(
    no_category='Commands'
)


def isGIF(inp):
    x = inp.lower()
    pattern = re.compile(r"n!gif [a-zA-Z]+", re.IGNORECASE)
    return pattern.match(x) != None


def requestGIF(inp):
    newString = inp[6::]
    if gif.getGIF(newString) != None:
        return gif.getGIF(newString)


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


client = commands.Bot(command_prefix='>',
                      help_command=help_command)


channel1 = client.get_channel(channelIdOld)


def generateXp():
    return 1


@client.command
async def test(ctx, arg):
    await ctx.send(arg)


@client.event
async def on_ready():
    print('Server moderator is now active')
    await client.get_channel(channelIdnew).send("CMD is now online")


@client.event
async def on_message(message):
    # if message.author.id == 430892547523608596:
    #     print(message.author)
    # if message.author.id == 393614489649676289:
    #     await message.channel.send(wack(message.content))
    if isBatchest(message.content):
        x = random.uniform(0, 1)
        if x < 0.5:
            await message.channel.send("<:batchest:906314613312872448> <:batchest:906314613312872448> <:batchest:906314613312872448> <:batchest:906314613312872448>")
        else:
            await message.channel.send(requestGIF("n!gif batchest"))
    if isGIF(message.content):
        await message.channel.send(requestGIF(message.content))
    if message.content.split(' ')[0].lower() == 'calc':
        await message.channel.send(findX(message.content[5::]))
    if message.content.lower() == "why is my code broken":
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
                val = f'You a real YRN. You mined {ironCount} iron ore, {goldCount} gold ore, {diamondCount} diamonds, 1 emeralds and {depth - ironCount - goldCount - diamondCount - 1} gravel'
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
async def urban(ctx, name):
    embd = discord.Embed(
        title=f'{name}:', description=urbanFind(name)['definition'])
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

client.run(tokenNew)
