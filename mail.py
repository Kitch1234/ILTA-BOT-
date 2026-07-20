import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv

from core.database import db


# Загружаем .env
load_dotenv()

TOKEN = os.getenv("TOKEN")


# Intents Discord
intents = discord.Intents.default()
intents.message_content = True
intents.members = True


# Создание бота
bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# Когда бот запустился
@bot.event
async def on_ready():
    print("--------------------------------")
    print(f"✅ Бот запущен: {bot.user}")
    print(f"🆔 ID: {bot.user.id}")

    # Подключение к базе
    if db.pool is None:
        await db.connect()

    # Синхронизация slash-команд
    try:
        synced = await bot.tree.sync()
        print(f"✅ Slash команд загружено: {len(synced)}")
    except Exception as e:
        print(f"Ошибка синхронизации: {e}")

    print("--------------------------------")


# Загрузка модулей из cogs
async def load_cogs():

    if not os.path.exists("./cogs"):
        os.makedirs("./cogs")

    for file in os.listdir("./cogs"):

        if file.endswith(".py") and not file.startswith("_"):

            try:
                await bot.load_extension(
                    f"cogs.{file[:-3]}"
                )

                print(f"✅ Загружен модуль: {file}")

            except Exception as e:
                print(f"❌ Ошибка загрузки {file}: {e}")


# Запуск
async def main():

    async with bot:

        await load_cogs()

        await bot.start(TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
