import discord
import os
import random 
from discord.ext import commands
import math
from asyncio import sleep
from keepAlive import keepAlive
from discord.utils import get
import asyncio
from discord import user
import json
from discord import guild
from discord import client
import praw
from praw.reddit import Subreddit
import aiohttp


client = commands.Bot(command_prefix='ayo ', help_command=None)

#welcome
@client.event
async def on_member_join(member): 
  if member.guild.name == "Gregz's Greenhouse":
    hibed=discord.Embed(description=f'Hi {member.mention} :wave:!!!' , colour = discord.Colour.purple())
    await client.get_channel(861632717820264511).send(embed=hibed)
    


#purge/clear command
@client.command(aliases=['purge' , 'CLEAR' , 'PURGE' , 'Clear' , 'Purge'])
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)

#Kick
@client.command()
async def kick(self, ctx, member:discord.member, * , reason=None):
  await member.kick(reason = reason)
  await ctx.channel.send(f"{member}'s been kicked from the server for {reason}")



@client.command()
async def hi(ctx):
  message = await ctx.send("hello")
  await asyncio.sleep(0.2)
  await message.edit(content="hi")
  await asyncio.sleep(0.2)
  await message.edit(content="wassup")
  await asyncio.sleep(0.2)
  await message.edit(content=":wave:")
  await asyncio.sleep(0.2)
  await message.edit(content="how're ya doin'?")
  await asyncio.sleep(0.2)
  await message.edit(content="I'm not doin' too bad myself")
  await asyncio.sleep(0.2)
  await message.edit(content="Sorry if the messages are too fast to read")
  await asyncio.sleep(0.2)
  await message.edit(content="k gtg")
  await asyncio.sleep(0.2)
  await message.edit(content="peace bro")
  await asyncio.sleep(0.2)
  await message.edit(content=":wave:")
  await asyncio.sleep(0.2)
  await message.edit(content='bye `lol`')


@client.command()
async def die(ctx):
  message = await ctx.send('u wanna kill ur `lmao`?')
  await asyncio.sleep(0.1)
  await message.edit(content='DIEEEEEEE')
  await asyncio.sleep(0.2)
  await message.edit(content='BURNNNNNNNN')
  await asyncio.sleep(0.2)
  await message.edit(content=':fire:')
  await asyncio.sleep(0.2)
  await message.edit(content='DO EVERYTHINGGG')
  await asyncio.sleep(0.2)
  await message.edit(content='You manage to kill urself Good job! :clap:')
  await asyncio.sleep(0.2)
 

@client.command()
async def poo(ctx):
  await ctx.message.reply('ewww why would you even tryy')

mainshop = [{"name":"Wtap","price":1000,"description":'dont buy'},
            {"name":"Circle strafe Comboes","price":1000,"description":"dont buy"},
            {"name":"E tap","price":10000,"description":"Only the best of the best can get learn such a inanse skill...(or you can by it here for 10k :eyes:)"},
            {"name":"Untouchable Movements","price":99999,"description":"Stupidly insane movements. Strafing so good that the enemy's mouse is SPINNING!!!"}]




fishing = ['big fish [:fish:]',
           'big screaming salmon [:blowfish:]',
           'chopstick cheap fishes [:tropical_fish:]',
           "pufferfish which somehow didn't kill you :face_with_spiral_eyes:[:blowfish:] ",
           "fried fish which somehow came from the **OCEAN** `lol` [:fish:]",
           'useless cans [:canned_food:]' , 
           'useless fishpoles woooooo! `lol`[🎣]',
           'shrips [:shrimp:]',
           'FlOPpeRs fRoM fORtNUt [:fish:]',
           'of your own brain cells which was lost here for all this time `lol` [:brain:]',
           'two cans of salt [:salt:]']

jobsell = ['your mom lmao',
           'you',
           'your co-worker',
           'your best friend',
           "that guy who want's to be like you",
           'ur dad lol' ,
           'your fellow fisherman Frank',
           'Joe Dickson',
           'that fortnut sweat who one-pumped you lol',
           'C h a r l i e',
           'that guy who 4 potted you on luanr lol',
           'your boss' ,
           "Charli D'Amelio" ,
           'Luke Davidson',
           'Bella Porch',
           'your discord moderator' ,
           'LimedFox(sub to him for cookie fr)',
           'your doctor`',
           'your peanut',
           'your left-over :pizza: slice lol',
           'your plumber',
           'god',
           'JuStIn fORtNItE',
           'Ph1LzA Minecraft']

begprefix = ['you were given',
             'you were awarded',
             'you were smacked',
             'you were praised']

begmain = ['by your dad who finally came back after all these years',
           'by your mom who finally felt pity on you',
           'by Joe Biden',
           'by your rich brother',
           'by MrBeast',
           'by Juan',
           'by that guy who you hate `lol`',
           'by the universe :flushed:',
           'by that rich guy who brags around your neighborhood',
           'by that anonymous generous guy']

huntmain = ['rabbits [:rabbit2:]',
            'foxes [:fox:]',
            'eagles [:eagle:]',
            'lions [:lion:]',
            'tigers [:tiger2:]',
            'sparrows [:dove:]',
            'wild lizards [:lizard:]',
            'bears [:bear:]',
            'mice [:mouse:]',
            'koalas [:koala:]',
            'cows [:cow:]',
            'wild hogs [:pig:]',
            'frogs [:frog:]',
            'bugs [:cockroach:]',
            'snakes [:snake:]', 
            'crocodiles [:crocodile:]',
            'squids [:squid:]',
            'sharks [:shark:]',
            'deer [:deer:]',
            'peacock [:peacock:]',
            ]

poop = ['nice cash broooo :moneybag:',
        'haha pee pee poo poo :money_with_wings:',
        'money seems to be growing on trees',
        ":smirk: Hah, hi I'm balance command",
        'heyyo',
        ':wave:',
        'calculating x/y^(2+a) it seems like your bank account is very likely to explode']






@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandOnCooldown):  
       return await ctx.send("u can't {} until ur **`{:.2f}`** second cooldown ends. Ok bro?".format(ctx.command.name, error.retry_after))



    

  
 

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(1000)
    
    message = await ctx.send("begging")
    await message.edit(content="begging.")
    await asyncio.sleep(0.1)
    await message.edit(content="begging..")
    await asyncio.sleep(0.1)
    await message.edit(content="begging...")
    await asyncio.sleep(0.2)
    await message.edit(content="begging....")
    await asyncio.sleep(0.2)
    await message.edit(content=f"{ctx.author.mention} {random.choice(begprefix)}, :coin: **{earnings}**, {random.choice(begmain)}.")

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json",'w') as f:
        json.dump(users,f)


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def fish(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(500)

    fishcount = random.randrange(30)

    fishbed = discord.Embed(title = f'and found `{fishcount}` {random.choice(fishing)} which he sold for :coin: **{earnings}**')
   
    
    
    if fishcount < 1:
      earnings = 0
      await ctx.send('your poor soul tried to fish but found nothing! How sadge')
      return

    if fishcount > 1:
      message = await ctx.send("fishing")
      await asyncio.sleep(0.1)
      await message.edit(content="fishing.")
      await asyncio.sleep(0.1)
      await message.edit(content="fishing..")
      await asyncio.sleep(0.1)
      await message.edit(content="fishing...")
      await asyncio.sleep(0.2)
      await message.edit(content="fishing....")
      await asyncio.sleep(0.2)
      await message.edit(content = f"{ctx.author.name} fished")
      await ctx.send(embed=fishbed)
      return
  
    

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json",'w') as f:
        json.dump(users,f)

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def hunt(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(999)

    huntcount = random.randrange(15)

    if huntcount < 1:
      earnings = 0

    if huntcount < 1:
      await ctx.send('`You went hunting and got nothing lol`')
      return

    if huntcount > 1:
      message =  await ctx.send('hunting')
      await asyncio.sleep(0.1)
      await message.edit(content="hunting.")
      await asyncio.sleep(0.1)
      await message.edit(content="hunting..")
      await asyncio.sleep(0.1)
      await message.edit(content="hunting...")
      await asyncio.sleep(0.1)
      await message.edit(content="hunting...")
      await asyncio.sleep(0.1)
      await message.edit(content= (f"{ctx.author.mention} hunted down `{huntcount}` {random.choice(huntmain)} which you sold for :coin: {earnings}"))
      return
  

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json",'w') as f:
        json.dump(users,f)


@client.command(aliases=['wd'])
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter to withdraw")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[1]:
        await ctx.send("Impossible child")
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,'bank')
    await ctx.send(f'{ctx.author.mention} You withdrew {amount} coins. finally brooo.')


@client.command(aliases=['dep'])
async def deposit(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,'bank')
    await ctx.send(f'{ctx.author.mention} You deposited {amount} coins')


@client.command(aliases=['sendmoney'])
async def give(ctx,member : discord.Member,amount = None):
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        await ctx.send("`You need to withdraw more money to gift doofus or you just don't even have that much money **lmao**`")
        return

    bal = await update_bank(ctx.author)
    if amount == 'max':
        amount = bal[0]

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,-1*amount,'bank')
    await update_bank(member,amount,'bank')
    await ctx.send(f'{ctx.author.mention} You gave {member} {amount} coins')


@client.command(aliases=['rb'])
@commands.cooldown(1,300, commands.BucketType.user)
async def rob(ctx,member : discord.Member):
    await open_account(ctx.author)
    await open_account(member)
    bal = await update_bank(member)


    if bal[0]<100:
        await ctx.send(f"You're robbing a poor dude who has basically no money, try robbing someone else who actually has money lol or wait until **{member.name}** earns more cash :money_mouth:")
        return

    earning = random.randrange(0,bal[0])

    await update_bank(ctx.author,earning)
    await update_bank(member,-1*earning)
    await ctx.send(f'{ctx.author.mention} robbed {member.name} and got :coin: {earning} :money_with_wings: ')


@client.command
async def roast(ctx):
  roasts	= ['You’re the reason God created the middle finger.',
           ' Your secrets are always safe with me. I never even listen when you tell me them.',
           'You bring everyone so much joy when you leave the room.',
           ' I may love to shop but I will never buy your bull.',
           'I’d give you a nasty look but you’ve already got one.',
           ' Someday you’ll go far. I hope you stay there.',
            'Were you born this stupid or did you take lessons?',
            'The people who tolerate you on a daily basis are the real heroes.',
            'You should really consider coming with a warning label smh',
            'You look like something that came out of a slow cooker.',
            'I don’t know what your problem is, but I’m guessing it’s hard to pronounce.',
            'If I wanted to hear from a moron, I’d fart and come to you.',
            'It’s kind of hilarious watching you try to fit your entire vocabulary into one sentence.',
            'You look like something that came out of a slow cooker',
            'I will ignore you so hard you will start doubting your existence.',
            'Feed your own ego. I’m busy.',
            ' I’ll never forget the first time we met. But I’ll keep trying.',
            'You’re a grey sprinkle on a rainbow cupcake.',
            ' I thought of you today. It reminded me to take out the trash.',
            ' You are so full of poop, the toilet’s jealous.',
            'I love what you’ve done with your hair. How do you get it to come out of the nostrils like that?',
            'Stupidity isn’t a crime, so you’re free to go.',
            'I’ve been called worse by better.',
            'Don’t you get tired of putting makeup on your two faces every morning?',
            'Too bad you can’t Photoshop your ugly personality.',
            'Do your parents even realize they’re living proof that two wrongs don’t make a right?',
            'Jesus might love you, but everyone else definitely thinks you’re an idiot.',
            'Please just tell me you don’t plan to home-school your kids.',
            'You see that door? I want you on the other side of it.',
            'You’re like the end pieces of a loaf of bread. Everyone touches you, but nobody wants you.',
            'If you’re going to act like a turd, go lay on the yard.',
            'You are more disappointing than an unsalted pretzel.',
            'Your face makes onions cry.',
            'Don’t worry about me. Worry about your eyebrows.',
            'Where’d you get your clothes, girl, American Apparently Not?',
            'If laughter is the best medicine, your face must be curing the world.',
            'You’re not stupid! You just have bad luck when you’re thinking.',
            'Isn’t there a bullet somewhere you could be jumping in front of?',
            'I’d slap you but I don’t want to make your face look any better.',
            ' Have a nice day, ||somewhere else||.',
            'Everyone’s entitled to act stupid once in a while, but you really abuse the privilege.',
            'If ignorance is bliss, you must be the happiest person on the planet.',
            "I got too weak to roast you this time bud, but imma get you next time you hearin' me?",
            "Your family tree must be a cactus ‘cause you’re all a bunch of pricks.",
            'If I threw a stick, you’d leave, right?',
            'Somewhere out there, there’s a tree working very hard to produce oxygen so that you can breathe. I think you should go and apologize to it.',
            'You look like a ‘before’ picture.',
            'Light travels faster than sound which is why you seemed bright until you spoke.',
            'Hold still. I’m trying to imagine you with personality.',
            'You are the human version of period cramps.',
            'Don’t get bitter, just get better" - your very mom',
            '50. What doesn’t kill you, disappoints me.',
            'Aww, it’s so cute when you **try** to talk about things you don’t understand.',
            'Hey, your village called – they want their idiot back.',
            'Calling you an idiot would be an insult to all stupid people.',
            'I am returning your nose. I found it in my business.',
            'Good story, but in what chapter do you shut up?',
            'There are some remarkably dumb people in this world. Thanks for helping me understand that.',
            'You’re about as useful as an ashtray on a motorcycle.',
            'You’ll never be the man your mom is',
            'You need a kiss on the neck from a crocodile.',
            'May both sides of your pillow be uncomfortably warm.',
            'Your kid is so annoying, he makes his Happy Meal cry.',
            'Oh, I’m sorry. Did the middle of my sentence interrupt the beginning of yours?',
            'Oops, my bad. I could’ve sworn I was dealing with an adult.',
            'Did I invite you to the barbecue? Then why are you all up in my grill?'
            'I’m an acquired taste. If you don’t like me, acquire some taste.',
            'Somewhere out there is a tree tirelessly producing oxygen for you. You owe it an apology.',
            'Yeah? Well, you smell like hot dog water.',
            'Beauty is only skin deep, but ugly goes clean to the bone.',
            'Oh, you don’t like being treated the way you treat me? That must suck.',
            'Pierre Trudeau, a Canadian politician, used this clap back after learning that Richard Nixon had insulted him. The political shade!',
            'Well, the jerk store called. They’re running out of you.',
            '“What, like it’s hard?” — Elle Woods, Legally Blonde',
            'Sorry, not sorry bwo',
            'I’m busy right now; can I ignore you another time?',
            'If you have a problem with me, write the problem on a piece of paper, fold it, and shove it into your brain `lol`.',
            'You have an entire life to be an idiot. Why not take today off?',
            'No matter how much a snake sheds its skin, it’s still a snake.',
            'Some people are like slinkies — not really good for much, but they bring a smile to your face when pushed down the stairs.',
            'You’re the reason this country has to put directions on shampoo.',
            'Of course I’m talking like an idiot… how else could you understand me?',
            'Are you almost done with all of this drama? Because I need an intermission.'
            'I’d give you a nasty look, but you’ve already got one.',
            'I’d agree with you, but then we’d both be wrong.',
            'Since you know it all, you should know when to shut up.',
            ' Life is full of disappointments, and I just added you to the list.',
            'I treasure the time I don’t spend with you.',
            'I was going to make a joke about your life, but I see life beat me to the punch.',
            'The last time I saw something like you… I flushed.',
            'The only work-life balance I want is being away from you.',
            "When you start talking, I'd rather go `deaf`."]
  await ctx.send(f"{random.choice(huntmain)}")

@client.command(aliases=['BALANCE', 'BAL', 'Balance' , 'balance'])
async def bal(ctx, member:discord.Member= None):
        if member != None:
            await open_account(member)
            users = await get_bank_data()

            wallet_amt = users[str(member.id)]["wallet"]
            bank_amt = users[str(member.id)]["bank"]

            embed = discord.Embed(
                title = f"`{member.name}`'s balance",
             )
          
            embed.add_field(name=f'`wallet`: :coin: {wallet_amt}', value=(f"_ _"), inline=False)
            embed.add_field(name=f'`bank`: :coin: {bank_amt}', value=(f"_ _"), inline=False)
            await ctx.message.reply(embed=embed)
        else:
            user = ctx.author
            await open_account(user)
            users = await get_bank_data()

            wallet_amt = users[str(user.id)]["wallet"]
            bank_amt = users[str(user.id)]["bank"]

            embed = discord.Embed(
                title = f"`{ctx.author.name}`'s balance",
              
            )
            embed.add_field(name=f'`wallet`: :coin: {wallet_amt}', value=(f"_ _") , inline=False)
            embed.add_field(name=f'`bank`: :coin: {bank_amt}', value= (f"_ _"), inline=False)
            await ctx.message.reply(embed=embed)  



@client.command()
async def gamble(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("`enter the amount you wanna use bruh`")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send("`you don't even have that much money lmao`")
        return
    if amount < 0:
        await ctx.send('`the amount must be positive number nerd`')
        return
    final = []
    for i in range(3):
        a = random.choice([':regional_indicator_x:',':regional_indicator_o:',':regional_indicator_q:'])

        final.append(a)

    await ctx.send(str(final))

    if final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
        await update_bank(ctx.author,2*amount)
        await ctx.send(f'{ctx.author.mention} `wins yay`')
    else:
        await update_bank(ctx.author,-1*amount)
        await ctx.send(f'{ctx.author.mention}`loses smh`')


@client.command()
async def shop(ctx):
    em = discord.Embed(title = "Shop")

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name = name, value = f":coin: {price} | {desc}")

    await ctx.send(embed = em)





@client.command()
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
            return


    await ctx.send(f"You just bought {amount} {item}")


@client.command()
async def inv(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []


    em = discord.Embed(title = f"**{ctx.author.name}'s Inventory**")
    for item in bag:
        name = item["item"]
        amount = item["amount"]
      

        em.add_field(name =(f'{name} - {amount}') , value =(f'`Sellable`'), inline = False)   

    await ctx.send(embed = em)


async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]
    

@client.command()
async def sell(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have {amount} {item} in your bag.")
            return
        if res[1]==3:
            await ctx.send(f"You don't have {item} in your bag.")
            return  

    await ctx.send(f"You just sold {amount} {item}.")

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.7* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]


@client.command(aliases = ["lb" , "rich"])
async def leaderboard(ctx,x = 1):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)    

    em = discord.Embed(title = f"Top {x} Richest People" , description = "This is decided on the basis of raw money in the bank and wallet",color = discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        name = member
        em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)


async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open('mainbank.json','w') as f:
        json.dump(users,f)

    return True


async def get_bank_data():
    with open('mainbank.json','r') as f:
        users = json.load(f)

    return users


async def update_bank(user,change=0,mode = 'wallet'):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open('mainbank.json','w') as f:
        json.dump(users,f)
    bal = users[str(user.id)]['wallet'],users[str(user.id)]['bank']
    return bal

@client.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0,25)]['data']['url'])
            await ctx.send(embed=embed)

@client.command()
async def cookie(ctx):
    cookiebed=discord.Embed(
        title = "You want a cookie boi?" ,
        description = f"Alright, here's a :cookie:" ,
        colour = discord.Colour.orange())
    await ctx.send(embed=cookiebed)

@client.command(aliases=['Magic8ball','8ball' , '8bal'])
async def _8ball(ctx, *, question):
  responses =  ["It is certain.",
                  "It is decidedly so.",
                  "Without a doubt.",
                  "Yes - definitely.",
                  "You may rely on it.",
                  "As I see it, yes.",
                  "Most likely.",
                  "Outlook good.",
                  "Yes.",
                  "Signs point to yes.",
                  "Reply hazy, try again.",
                  "Ask again later.",
                  "Better not tell you now.",
                  "Cannot predict now.",
                  "Concentrate and ask again.",
                  "Don't count on it.",
                  "My reply is no.",
                  "My sources say no.",
                  "Outlook not so good.",
                  "Very doubtful."]
  await ctx.send(f'ur question: {question}\n my answer: {random.choice(responses)}')



#help cmd

@client.group(invoke_without_command=True)
async def help(ctx):
  h = discord.Embed(title= "Command List")
  h.add_field(name=':yen: Currency', value = '`ayo help currency`')
  h.add_field(name=':gear: Moderation', value = '`ayo help moderation`')
  h.add_field(name=':golf: Games', value = '`ayo help games`')
  h.add_field(name=':golf: Fun', value = '`ayo help fun`')
  await ctx.send(embed=h) 


@help.command()
async def moderation(ctx):
  u = discord.Embed(title = ':tools: Moderation Commands' , description = ':hammer: Utility Commands')
  u.add_field(name=':neutral_face: Mute', value = '`ayo mute`')
  u.add_field(name=':link: Kick', value = '`ayo kick`')
  u.add_field(name=':lock: ban', value = '`ayo ban`')
  u.add_field(name=':closed_lock_with_key: tempban', value = '`ayo tempban`')
  u.add_field(name=':wrench: cooldown', value = '`ayo cooldown set`')
  u.set_footer(text='banhammer time bois')
  await ctx.send(embed=u)

@help.command()
async def currency(ctx):
  c = discord.Embed(title = ':money_with_wings: Currency ' , description = 'Earn moneh big boi')
  c.add_field(name=':fingers_crossed: beg', value = '`ayo beg`')
  c.add_field(name=':sewing_needle: hunt', value = '`ayo hunt`')
  c.add_field(name=':fish: fish', value = '`ayo fish`')
  c.add_field(name=':moneybag: rob', value = '`ayo rob`')
  c.add_field(name='hack', value = '`ayo hack`')
  c.add_field(name=':bank: balance', value = '`ayo bal`')
  c.add_field(name=':shopping_bags: shop', value = '`ayo shop`')
  
  c.set_footer(text='more trash commands coming soon')
  
  await ctx.send(embed=c)

@help.command()
async def fun(ctx):
  f = discord.Embed(title = ':smile: fun' , description = 'Plays some games that the bot features brotha')
  f.add_field(name=':joy: meme', value = '`ayo meme`')
  f.add_field(name=':grimacing: roast', value = '`ayo roast <person>`')
  f.set_footer(text='more trash commands coming soon')
  
  await ctx.send(embed=f)


@help.command()
async def games(ctx):
  g = discord.Embed(title = ':golf: Games' , description = 'gameeengg yas yas')
  g.add_field(name=':8ball: 8ball', value = '`ayo 8ball`')
  g.add_field(name=':grimacing: roast', value = '`ayo roast <person>`')
  g.set_footer(text='more trash commands coming soon')
  
  await ctx.send(embed=g)



client.run('TOKEN')
