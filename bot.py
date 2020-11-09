import os
from twitchio.ext import commands
import urllib.request
import json

# declaramos las variables del .ENV
bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

# Muestra un mensaje de que el bot esta activo


@bot.event
async def llegada():
    'El Bot ha sido llamado'
    print(f"{os.environ['BOT_NICK']} llego al chat!")
    ws = bot._ws
    await ws.send_privmsg(os.environ['SCI'], "/me llego al chat!")


# declaramos para que el bot ea los mensajes
@bot.event
async def event_message(ctx):
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return

    await bot.handle_commands(ctx)

# declaramos como variable la clave de la Youtube Api
KEY = os.environ['API']

# Comando para saber la cantidad de subs en youtube


@bot.command(name='subs')
async def subscriptores(ctx, username):
    data = urllib.request.urlopen(
        "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + username + "&key=" + KEY).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    response = username + " tiene " + \
        "{:,d}".format(int(subs)) + " suscriptores!"
    await ctx.send(response)

# comando para probar que este activo


@bot.command(name='test')
async def test(ctx):
    await ctx.send('test completado!')

# comando para iniciar las votaciones


@bot.command(name="vot")
async def vot(ctx, maximo):
    try:
        int(maximo)
    except:
        await ctx.send("Ingrese un valor numerico")
    await ctx.send("Comando ejecutado")
    if maximo == 2:
        vot_1 = 0
        vot_2 = 2
        await ctx.send("La votacion se ha establecido en 2")
    elif maximo == 3:
        vot_1 = 0
        vot_2 = 0
        vot_3 = 0
        await ctx.send("La votacion se ha establecido en 3")
    elif maximo == 4:
        vot_1 = 0
        vot_2 = 0
        vot_3 = 0
        vot_4 = 0
        await ctx.send("La votacion se ha establecido en 4")
    else:
        await ctx.send("el numero maximo de opciones es 4, ingresa un numero del 2 al 4, EJ: !vot 3")

# instruccion de ejecutar el bot
if __name__ == "__main__":
    bot.run()
