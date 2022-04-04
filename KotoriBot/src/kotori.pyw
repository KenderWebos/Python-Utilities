import discord
from discord.ext import commands
from discord.utils import get
import datetime
from random import randint
import random
import urllib
import json

bot = commands.Bot(command_prefix='k!', description="The definitive ADMIN.")
key = "AIzaSyAcfSvFKW5uSaVFAbKBkKt8UW_nLYVlq6c"

@bot.command()
async def rand(ctx):
    await ctx.send( randint(0, 100) )

@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@bot.command(name='subs') #Funcion que mostrara los suscriptores de un canal de Youtube que le pasemos como parametro
async def subscriptores(ctx,username):
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + username + "&key=" + key).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    response = username + " tiene " + "{:,d}".format(int(subs)) + " suscriptores!"
    await ctx.send(response)

@bot.command()
async def say(ctx, *, arg):
    await ctx.channel.purge(limit=1)
    await ctx.send(str(arg))

@bot.command(aliases=["8ball", "test"])
async def pregunta(ctx, *, question):
    #responses=["Si.","No.", "Intenta preguntar de nuevo"]
    response=[
        "Es correcto.",
        "Sin duda.",
        "Sí, definitivamente.",
        "Puedes confiar en ello.",
        "Si.",
        "Las señales apuntan a que sí.",
        "Pregunta de nuevo más tarde.",
        "Mejor no decirte ahora.",
        "No se puede predecir ahora.",
        "No cuentes con eso",
        "Mi respuesta es no.",
        "Mis fuentes dicen que no.",
        "No lo creo",
        "Muy dudoso.",
        "No."]
    await ctx.send( str(question + "\n" + random.choice(response)) )

@bot.command()
async def kenderweb(ctx):
    await ctx.send('https://kenderman.github.io/new_KenderWeb/index.html')
    ctx.channel.purge(limit=1)

@bot.command()
async def games(ctx):
    await ctx.send('https://drive.google.com/drive/u/0/folders/1Sebljj898ttuSCcSLePBCH8-d81Fnfay')
    ctx.channel.purge(limit=1)

@bot.command()
async def cubu(ctx):
    await ctx.send('https://simmer.io/@KenderMan/cubu')
    ctx.channel.purge(limit=1)

@bot.command()
async def cuandoSeUnio(ctx, member : discord.Member):
    await ctx.send(str(member.joined_at))

@bot.command()
async def funar(ctx, member : discord.Member):
    await member.send("Te voy a funarte si, tai claro")
"""
@bot.command(pass_context = True)
async def conectar(ctx):
    canal = ctx.message.author.voice.channel
    if not canal:
        await ctx.send("no estas conectado a un canal de voz...")
        return
    voz = get(bot.voice_clients, guild=ctx.guild)
    if voz and voz.is_connected():
        await voz.move_to(canal)
    else:
        voz = await canal.connect()
"""
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="hola soy la descripcion", 
    timestamp=datetime.datetime.utcnow() , color=discord.Color.purple())
    embed.add_field(name="El servidor fue creado en: ", value=f"{ctx.guild.created_at}")
    embed.add_field(name="El admin supremo es: ", value=f"{ctx.guild.owner}")
    embed.add_field(name="El servidor es de la region: ", value=f"{ctx.guild.region}")
    embed.set_thumbnail(url="https://i.pinimg.com/564x/3a/68/d5/3a68d52acc836c6560f36d24a769557f.jpg")
    await ctx.send(embed = embed)

@bot.command()
async def saludar(ctx):
    await ctx.send('Buenos dias estrellitas , la Tierra les dice hola !!!!!!!!!! :D')

@bot.command()
async def despedirse(ctx):
    await ctx.send('Nos vemos amigos, fue un gran dia, que duerman bien y hasta la proximaa!')    

@bot.command()
async def ayuda(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Esta es la lista de comandos", 
    timestamp=datetime.datetime.utcnow() , color=discord.Color.purple())
    embed.add_field(name = "k!saludar", value = "Envia un saludo a los usuarios del discord")
    embed.add_field(name = "k!despedirse", value = "Se despide de los usuarios del discord")
    embed.add_field(name = "k!pregunta esViernes?", value = "Adivina el futuro y responde tu pregunta (si/no)")
    embed.add_field(name = "k!info", value = "Da informacion general")
    embed.add_field(name = "k!rand", value = "Da un numero al azar entre 1 y 100")
    embed.add_field(name = "k!kenderweb", value = "Da un link con la mejor pagina de la galaxia")
    embed.add_field(name = "k!funar", value = "Prepara una funa para un usuario")
    embed.add_field(name = "k!cuandoSeUnio", value = "Muestra cuando se unio un usuario al discord")
    embed.add_field(name = "k!suscriptores", value = "Muestra cuantos suscriptores tiene un canal de youtube")

    embed.add_field(name = "k!ayuda", value = "Te muestra los comandos disponibles")
    embed.set_thumbnail(url="https://ih1.redbubble.net/image.1071086047.4283/bg,f8f8f8-flat,750x,075,f-pad,750x1000,f8f8f8.jpg")
    await ctx.send(embed = embed)

#EVENTOS
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Stream", 
    url="https://www.twitch.tv/kendermanlive"))
    print("Hola chicos, estoi activo!")
    print("4CT1V4T3D...")

@bot.event
async def on_member_join(ctx, member):
    await print("se a unido")

bot.run('Nzc3MzUwNjE5ODAzMjg3NTgy.X7CKLg.ly618ffPsocjjRxkmqs7LVaRinM')