# Bot for Discord by Mjkey
# Ключик - Суккуб (Meru's twin sister)
# Комерческое использование запрещено и бла.. бла.. бла..
# ────────────────────────── ••• ☆ ••• ────────────────────────── #
#    ▄█   ▄█▄    ▄████████ ▄██   ▄   
#   ███ ▄███▀   ███    ███ ███   ██▄ 
#   ███▐██▀     ███    █▀  ███▄▄▄███ 
#  ▄█████▀     ▄███▄▄▄     ▀▀▀▀▀▀███ 
# ▀▀█████▄    ▀▀███▀▀▀     ▄██   ███ 
#   ███▐██▄     ███    █▄  ███   ███ 
#   ███ ▀███▄   ███    ███ ███   ███ 
#   ███   ▀█▀   ██████████  ▀█████▀  
#   ▀                                
# ██████╗ ██╗   ██╗    ███╗   ███╗     ██╗██╗  ██╗███████╗██╗   ██╗
# ██╔══██╗╚██╗ ██╔╝    ████╗ ████║     ██║██║ ██╔╝██╔════╝╚██╗ ██╔╝
# ██████╔╝ ╚████╔╝     ██╔████╔██║     ██║█████╔╝ █████╗   ╚████╔╝ 
# ██╔══██╗  ╚██╔╝      ██║╚██╔╝██║██   ██║██╔═██╗ ██╔══╝    ╚██╔╝  
# ██████╔╝   ██║       ██║ ╚═╝ ██║╚█████╔╝██║  ██╗███████╗   ██║   
# ╚═════╝    ╚═╝       ╚═╝     ╚═╝ ╚════╝ ╚═╝  ╚═╝╚══════╝   ╚═╝                                                               
# ────────────────────────── ••• ☆ Зависимости | Библиотеки ☆ ••• ────────────────────────── #
import discord
import time
import os
import random
from discord.ext import tasks, commands
from discord.utils import get
from bin.conf import sk

# ────────────────────────── ••• ☆ Переменные и Функции ☆ ••• ────────────────────────── #
global own, ver
own = sk['Own'] # ID Админа
ver = sk['ver'] # Версия бота
imgExtension = ["png", "jpeg", "jpg", "gif"] #расширение
allImages = list()

def log(e):
    e = f"\033[1;33m[LOG.{e}]\033[0m"
    return e # Цветной Лог в консоль

def err(e):
    e = f"\033[0;31m[ERROR.{e}]\033[0m"
    return e # Цветная Ошибка в консоль

def is_channel():
    def predicate(ctx):
        return ctx.message.channel.id == 1#ДУма.ю
    return commands.check(predicate)

def is_owner():
    async def predicate(ctx):
        return ctx.author.id == own
    return commands.check(predicate) # Проверка на Админа

def chooseRandomImage(directory): 
    for img in os.listdir(directory): #Lists all files
        ext = img.split(".")[len(img.split(".")) - 1]
        if (ext in imgExtension):
            allImages.append(img)
    choice = random.randint(0, len(allImages) - 1)
    chosenImage = allImages[choice]
    return chosenImage #Рандом картинка

# ────────────────────────── ••• ☆ Основа ☆ ••• ────────────────────────── #
key = commands.Bot(command_prefix=sk['Pref'])
key.remove_command('help')

@key.event
async def on_ready():
    await key.change_presence(status=discord.Status.invisible) #DEL
    print(f'{log("Info")} Бот {sk["N"]} успешно запущен! • Версия: {ver}')

# ────────────────────────── ••• ☆ Пинг | Состояние ☆ ••• ────────────────────────── #
@key.command(aliases = ['Ping', 'PING', 'pING', 'Пинг', 'ПИНГ', 'пИНГ', 'ping', 'Понг', 'ПОНГ', 'пОНГ', 'понг'])
#@is_channel()
async def пинг(ctx):
    print(f'{log("Info")} Был запрошен пинг')
    ping = key.ws.latency 
    pingT = '🟩🟩🟩🟩🟩'
    if ping > 0.14500000000000000:
        pingT = '🟩🟩🟩🟩🟧'
    if ping > 0.20000000000000000:
        pingT = '🟩🟩🟩🟧🟧'
    if ping > 0.25000000000000000:
        pingT = '🟩🟩🟧🟧🟧'
    if ping > 0.30000000000000000:
        pingT = '🟩🟧🟧🟧🟥'
    if ping > 0.35000000000000000:
        pingT = '🟧🟧🟥🟥🟥'
    if ping > 0.40000000000000000:
        pingT = '🟥🟥🟥🟥🟥'
    message = await ctx.send('Анализ...')
    time.sleep(1)
    await message.edit(content = f'Состояние: {pingT} `{ping * 1000:.0f}мс` :ping_pong:')
    print(f'{log("Ping")} {pingT} • {ping * 1000:.0f}мс') 

# ────────────────────────── ••• ☆ Картинки ☆ ••• ────────────────────────── #
@key.command(aliases = ['покажи','скинь'])
@commands.cooldown(1, 30, commands.BucketType.user)
async def дай(ctx, *args):
    author = ctx.message.author
    await ctx.message.add_reaction('✨')
    await ctx.message.delete(delay=90)
    dlya = 'Для '
    desc = dlya + author.mention
    #
    res = ''
    n = 0
    ls = 0
    #
    for arg in args:
        if n == 0:
            g = arg # какая картинка
        res = res + " " + arg
        n += 1
    if "лс" in res: # в лс?
        ls = 1
    # проверка последнего аргумента на цифру
    try:
        arg = int(arg)
    except ValueError:
        arg = 1

    if arg <= 5:
        for x in range(arg):
            if g in ('тян', 'тяночку', 'тянку', 'тянучку', 'дефку'):
                fold = "images"
                z = chooseRandomImage(fold)
                a = f"{fold}/{z}"
                print(f'{log("Info/IMG")} Запрошено {g} - {a} | {ls}')
                file = discord.File(a)
                embed = discord.Embed(title="Тяночка от Ключика 😈", description=desc, color = 0xff2b2b)
                embed.set_image(url=f"attachment://{z}")
            elif g in ('хент', 'хентай', 'hentai', 'хуйтай', 'хентаи', 'порнушку', 'хентайчик'):
                fold = "images/H"
                z = chooseRandomImage(fold)
                a = f"{fold}/{z}"
                print(f'{log("Info/IMG")} Запрошено {g} - {a} | {ls}')
                file = discord.File(a)
                embed = discord.Embed(title="Хентай от Ключика 😈", description=desc, color = 0xff2b2b)
                embed.set_image(url=f"attachment://{z}")
            elif g in ('демона', 'демонису', 'демонис', 'demons', 'demon'):
                fold = "images/D"
                z = chooseRandomImage(fold)
                a = f"{fold}/{z}"
                print(f'{log("Info/IMG")} Запрошено {g} - {a} | {ls}')
                file = discord.File(a)
                embed = discord.Embed(title="Демон от Ключика 😈", description=desc, color = 0xff2b2b)
                embed.set_image(url=f"attachment://{z}")
            elif g in ('тент', 'тентакли', 'щупальца', 'tentacle', 'тунтукли'):
                fold = "images/T"
                z = chooseRandomImage(fold)
                a = f"{fold}/{z}"
                print(f'{log("Info/IMG")} Запрошено {g} - {a} | {ls}')
                file = discord.File(a)
                embed = discord.Embed(title="Тентакли от Ключика 😈", description=desc, color = 0xff2b2b)
                embed.set_image(url=f"attachment://{z}")
            elif g in ('лолю', 'лоли', 'запрещёнку', 'запрещенку', 'loli', 'этти', 'эччи'):
                fold = "images/L"
                z = chooseRandomImage(fold)
                a = f"{fold}/{z}"
                print(f'{log("Info/IMG")} Запрошено {g} - {a} | {ls}')
                file = discord.File(a)
                embed = discord.Embed(title="Этти от Ключика 😈", description=desc, color = 0xff2b2b)
                embed.set_image(url=f"attachment://{z}")
            #
            else:
                print(f'{err("ERROR/IMG")} Запрошено {g} | {ls} - не найдено')
                err = await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}, не знаю я таких картинок..** `{g}`', color=0x0c0c0c))
                await err.delete(delay=160)

            #отправка картинки
            if ls == 0:
                #message = await ctx.send(res)
                embed.set_footer(text=f"Всем изображённым тяночкам и не только, есть 18 лет!\nВерсия: {ver}")
                embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/421817905152393258/ccdb006f062b75ad776ba7e236ef4dfa.png")
                await ctx.send(embed=embed, file=file)
            elif ls == 1: 
                #message = await ctx.author.send(res)
                embed.set_footer(text=f"Всем изображённым тяночкам и не только, есть 18 лет!\nВерсия: {ver}")
                embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/421817905152393258/ccdb006f062b75ad776ba7e236ef4dfa.png")
                await ctx.author.send(embed=embed, file=file)
    else:
        print(f'{err("ERROR/IMG")} Запрошено {g} больше 5')
        err = await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}, я не могу дать тебе больше 5 картинок за раз!**', color=0x0c0c0c))
        await err.delete(delay=160)
# ────────────────────────── ••• ☆ Удаление сообщения ☆ ••• ────────────────────────── #
@key.event
async def on_raw_reaction_add(payload):
    if payload.user_id == own:
        if payload.emoji.name == "❌":
            chan = key.get_channel(payload.channel_id)
            message = await chan.fetch_message(payload.message_id)
            reaction = get(message.reactions, emoji=payload.emoji.name)
            if reaction:
                await message.delete(delay=1)
                await message.add_reaction('❌')

# ────────────────────────── ••• ☆ Обработка ошибок ☆ ••• ────────────────────────── #
@key.event 
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}, я тебя не понимаю.**', color=0x0c0c0c))
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}, я не такая быстрая!! Попроси через {error.retry_after:.0f} сек.**', color=0x0c0c0c))
    print(f'{err("Command")} {error}')
@key.event
async def on_error(event, *args, **kwargs):
    print(f'{err("ERROR")} {event}')

# ────────────────────────── ••• ☆ Включение ☆ ••• ────────────────────────── #
key.run(sk['tkn'])