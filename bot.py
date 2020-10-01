import os
from twitchio.ext import commands
import random
import time



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

@bot.command(name="votar")
async def poll(ctx):
  numero_maximo = ctx.content
  if numero_maximo == "2" and ctx.author.name.lower() is "freddyfalso" or "scidroid" or "dinosaurio_rar" or "ezequielift" or "pythonlist" or "darkatzzzz" or "emiilrodriguezz":
    uno = 0
    dos = 0
    ctx.channel.send("Todos voten poniendo en el chat 1 o 2.")
  elif numero_maximo == "3" and ctx.author.name.lower() is "freddyfalso" or "scidroid" or "dinosaurio_rar" or "ezequielift" or "pythonlist" or "darkatzzzz" or "emiilrodriguezz":
    uno = 0
    dos = 0
    tres = 0
    ctx.channel.send("Todos voten poniendo en el chat 1, 2 o 3.")
  elif numero_maximo == "4" and ctx.author.name.lower() is "freddyfalso" or "scidroid" or "dinosaurio_rar" or "ezequielift" or "pythonlist" or "darkatzzzz" or "emiilrodriguezz":
    uno = 0
    dos = 0
    tres = 0
    cuatro = 0
    ctx.channel.send("Todos voten poniendo en el chat 1, 2, 3 y 4.")
  elif numero_maximo == "5" and ctx.author.name.lower() is "freddyfalso" or "scidroid" or "dinosaurio_rar" or "ezequielift" or "pythonlist" or "darkatzzzz" or "emiilrodriguezz":
    uno = 0
    dos = 0
    tres = 0
    cuatro = 0
    cinco = 0
    ctx.channel.send("Todos voten poniendo en el chat 1, 2, 3, 4 o 5.")
  else:
    if ctx.author.name.lower() is "freddyfalso" or "scidroid" or "dinosaurio_rar" or "ezequielift" or "pythonlist" or "darkatzzzz" or "emiilrodriguezz":
      uno = 0
      dos = 0
      ctx.channel.send("Todos voten poniendo en el chat 1 o 2.")
    
    
@bot.command(name="resultados")
async def resultados(ctx):
  global numero_maximo
  if numero_maximo == "2" and ctx.author.name.lower() is "freddyfalso" or "scidroid" or "dinosaurio_rar" or "ezequielift" or "pythonlist" or "darkatzzzz" or "emiilrodriguezz":
    total = uno + dos
    calculo_porcentaje = total / 100
    if dos > uno:
      ganador = 2
      porcentaje = calculo_porcentaje * dos
      empate = "no"
    elif uno > dos:
      ganador = 1
      porcentaje = calculo_porcentaje * uno
      empate = "no"
    elif uno == dos:
      empate = "si"
    
    if empate == "no": 
      ctx.channel.send(f"Gano la opcion {ganador} con el {porcentaje}% de los votos con un total de {total} votos.")
    elif empate == "si":
      ctx.channel.send(f"Hay un empate, con un total de {total} votos")
      
  elif numero_maximo == "3" and ctx.author.name.lower() is "freddyfalso" or "scidroid" or "dinosaurio_rar" or "ezequielift" or "pythonlist" or "darkatzzzz" or "emiilrodriguezz":
    total = uno + dos + tres
    calculo_porcentaje = total / 100
    if dos > uno and dos > tres:
      ganador = 2
      porcentaje = calculo_porcentaje * dos
      empate = "no"
    elif uno > dos and uno > tres:
      ganador = 1
      porcentaje = calculo_porcentaje * uno
      empate = "no"
    elif tres > dos and tres > uno:
      ganador = 3
      porcentaje = calculo_porcentaje * tres
      empate = "no"
    elif uno == dos and uno == tres:
      empate = "si"
    
    if empate == "no": 
      ctx.channel.send(f"Gano la opcion {ganador} con el {porcentaje}% de los votos con un total de {total} votos.")
    elif empate == "si":
      ctx.channel.send(f"Hay un empate, con un total de {total} votos")
  
  elif numero_maximo == "4" and ctx.author.name.lower() is "freddyfalso" or "scidroid" or "dinosaurio_rar" or "ezequielift" or "pythonlist" or "darkatzzzz" or "emiilrodriguezz":
    total = uno + dos + tres + cuatro
    calculo_porcentaje = total / 100
    if dos > uno and dos > tres and dos > cuatro:
      ganador = 2
      porcentaje = calculo_porcentaje * dos
      empate = "no"
    elif uno > dos and uno > tres and uno > cuatro:
      ganador = 1
      porcentaje = calculo_porcentaje * uno
      empate = "no"
    elif tres > dos and tres > uno and tres > cuatro:
      ganador = 3
      porcentaje = calculo_porcentaje * tres
      empate = "no"
    elif cuatro > dos and cuatro > uno and cuatro > tres:
      ganador = 3
      porcentaje = calculo_porcentaje * tres
      empate = "no"
    elif uno == dos and uno == tres and tres == cuatro:
      empate = "si"
    
    if empate == "no": 
      ctx.channel.send(f"Gano la opcion {ganador} con el {porcentaje}% de los votos con un total de {total} votos.")
    elif empate == "si":
      ctx.channel.send(f"Hay un empate, con un total de {total} votos")
  else:
    if ctx.author.name.lower() is "freddyfalso" or "scidroid" or "dinosaurio_rar" or "ezequielift" or "pythonlist" or "darkatzzzz" or "emiilrodriguezz":
      total = uno + dos
      calculo_porcentaje = total / 100
      if dos > uno:
        ganador = 2
        porcentaje = calculo_porcentaje * dos
        empate = "no"
      elif uno > dos:
        ganador = 1
        porcentaje = calculo_porcentaje * uno
        empate = "no"
      elif uno == dos and uno == tres and tes == cuatro:
        empate = "si"
      
      if empate == "no": 
        ctx.channel.send(f"Gano la opcion {ganador} con el {porcentaje}% de los votos con un total de {total} votos.")
      elif empate == "si":
        ctx.channel.send(f"Hay un empate, con un total de {total} votos")

@bot.command(name="reset")
async def resetvots(ctx):
  if ctx.author.name.lower() is "freddyfalso" or "scidroid" or "dinosaurio_rar" or "ezequielift" or "pythonlist" or "darkatzzzz" or "emiilrodriguezz":
    global uno,dos,tres,cuatro,cinco,participantes
    del uno
    del dos
    del tres
    del cuatro
    del cinco
    participantes = []


if __name__ == "__main__":
    bot.run()
