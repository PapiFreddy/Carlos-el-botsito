import os
from twitchio.ext import commands
import random
import time

uno = 0

dos = 0

tres = 0

#lol

cuatro = 0

cinco = 0

participantes = []

bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

@bot.event
async def event_ready():
    'El Bot ha sido llamado'
    print(f"{os.environ['BOT_NICK']} llego al chat!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me llego al chat!")

@bot.event
async def event_message(ctx):
  global participantes
  if ctx.author.name.lower() == os.environ['BOT_NICK'].lower() or ctx.author.name.lower() == 'Nightbot'.lower():
        return
  global uno,dos,tres,cuatro,cinco
  #Contribución de @PythonBoy123
  await bot.handle_commands(ctx)

    # await ctx.channel.send(ctx.content)

    #if 'hola' in ctx.content.lower():
        #await ctx.channel.send(f"Hola, @{ctx.author.name} bienvenido al MEJOR STREAM 2020 espero te la pases bien!!!")
      #hOLA AA TODOS COMO ESTRAN000

  #if 'chakaflus' in ctx.content.lower():
        #await ctx.channel.send("chakaflus")

  #if 'juan-carlos' in ctx.content.lower():
        #await ctx.channel.send("La mejor combinacion 2020")

  #if 'discord' in ctx.content.lower() and 'sigue a nuestro npc favorito en todas sus redes sociales' not in ctx.content.lower():
        #await ctx.channel.send("Unete al discord mas cool, discord.gg/TWuEDzT ")
    
    #if '?' in ctx.content.lower() and 'youtube.com' not in ctx.content.lower():
        #await ctx.channel.send("Contrata a mario")
        
  #if ' ip' in ctx.content.lower() or 'ip' == ctx.content.lower():
        #await ctx.channel.send("la IP es 51.161.84.224:25717  y la version es la 1.7.2")
        
  if '!source' in ctx.content.lower():
        await ctx.channel.send("quien dijo source?, pues aqui esta el mio carlos.scidroid.live")
          
  if ctx.content.lower() == "1" and ctx.author.name not in participantes:
        uno += 1
        participantes.append(ctx.author.name)

  if ctx.content.lower() == "2" and ctx.author.name not in participantes:
        dos += 1
        participantes.append(ctx.author.name)
  if ctx.content.lower() == "3" and ctx.author.name not in participantes:
        tres += 1
        participantes.append(ctx.author.name)
  if ctx.content.lower() == "4" and ctx.author.name not in participantes:
        cuatro += 1
        participantes.append(ctx.author.name)
  if ctx.content.lower() == "5" and ctx.author.name not in participantes:
        cinco += 1
        participantes.append(ctx.author.name)
#contribucion de christivn.

@bot.command(name="frase")
async def Frase(ctx):
    await ctx.channel.send(random.choice('Te quiero mucho', 'La teoria de la gravedad de Einstein', 'Yo no soy senior, ni mid, ni junior yo soy ingeniero', '¿Todo bien en casa?', 'Mis mods son simps', 'Coño *Inserte persona del chat*') + ' -Freddy 2020.')


@bot.command(name="resultados")
async def resultados(ctx):
    if ctx.author.name.lower() is "freddyfalso" or "scidroid" or "dinosaurio_rar" or "ezequielift" or "pythonlist" or "darkatzzzz" or "emiilrodriguezz": 
      await ctx.channel.send(f"1 tiene {uno} votos, 2 tiene {dos} votos, 3 tiene {tres} votos, 4 tiene {cuatro} votos, 5 tiene {cinco} votos.")



@bot.command(name="reset")
async def resetvots(ctx):
  if ctx.author.name.lower() is "freddyfalso" or "scidroid" or "dinosaurio_rar" or "ezequielift" or "pythonlist" or "darkatzzzz" or "emiilrodriguezz":
    global uno,dos,tres,cuatro,cinco,participantes
    uno = 0
    dos = 0
    tres = 0
    cuatro = 0
    cinco = 0
    participantes = []


if __name__ == "__main__":
    bot.run()
