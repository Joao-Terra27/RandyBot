import discord
from discord.ext import commands
import random
#este comando criará um arquivo config.ini. Insira o token e se necessário o IP do seu server. Logo em seguida, insira o seu token no bot.run()
from settings.settings import config

bot = commands.Bot(command_prefix= '~', case_insensitive = True, status=discord.Status.idle,
                    activity= discord.Game('Randomizing...'))

@bot.event
async def on_ready():
  print('Bot randomizing...')

@bot.command(pass_context = True)
async def randfact(ctx, *msg):
  f = 'random1.txt'
  r = open(f, 'r', encoding="utf8").read()
  array = eval(r)  
  random_number = random.randint(0, len(array))
  
  await ctx.send(array[random_number])

TOKEN = config['CONEXAO']['Discord_Token']

bot.run(TOKEN)