import discord
import sys
import os
from jacket_collect import*
from ritext import img_txt
from meumeuthonk import meumeu
from song_collector import remy_links, titles
from jacketcollage import collager, images
from discord.ext import commands

#grequests will get angry if you don't prioritize it first in the import calls!
bot = commands.Bot(command_prefix = '$', description = 'A DDR bot that generates memes and songs')
channel = bot.get_channel(594197266668191768)



@bot.event
async def on_ready():
    print('{0.user} is now online'.format(bot))
    await bot.change_presence(activity = discord.Game(name = '19s with no-bar'))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    user = message.author.name
    msg = message.content
    print(f"{user} said {msg}")

    await bot.process_commands(message)

@bot.command()
async def rinonsays(ctx,*,arg):
    #channel = bot.get_channel(594197266668191768)

    img_txt(arg)
    if len(arg) >= 20:
        await channel.send(file = discord.File('l.png'))
        os.remove('l.png')

    else:
        await channel.send(file = discord.File('s.png'))
        os.remove('s.png')

@bot.command()
async def meuthink(ctx, arg):
    #channel = bot.get_channel(594197266668191768)

    meumeu(arg)

    await channel.send(file = discord.File('m.png'))
    os.remove('m.png')

@bot.command()
async def randomset(ctx):

    channel = bot.get_channel(594197266668191768)

    index_num = []
    final_set = []
    stage_num = 1

    song_set = random.sample(img_jacket, k = 3)

    for song in song_set:
        final_set.append(song)
        song_num = img_jacket.index(song)
        index_num.append(song_num)

    print(song_set)
    print(index_num)
    print(final_set)

    collager(final_set)

    await channel.send(file = discord.File('e.png'))
    os.remove('e.png')

    embed = discord.Embed(title = "Random Set", description = "Good luck", color = discord.Color.magenta())
    
    for index in index_num:
        name = titles[index]
        link = remy_links[index]
        embed.add_field(name = f"Stage #{stage_num}", value = f"[{name}]({link})", inline = False)
        stage_num += 1
    
   
    images.clear()
    final_set.clear()
    index_num.clear()
    await ctx.send(embed = embed) 

bot.run('NTk0MTYzNDMwMjc4MTY4NjA2.XRYb-Q.NQYcdn8Lc2uLrQeGHzLlNbYf3dk')