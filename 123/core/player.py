from datetime import datetime

from core.database import db


async def create_player(discord_id: int, username: str):

    query = """
    INSERT INTO users (
        discord_id,
        username
    )
    VALUES ($1, $2)
    ON CONFLICT (discord_id)
    DO NOTHING;
    """

    async with db.acquire() as conn:
        await conn.execute(
            query,
            discord_id,
            username
        )


async def get_player(discord_id: int):

    query = """
    SELECT *
    FROM users
    WHERE discord_id = $1;
    """

    async with db.acquire() as conn:
        return await conn.fetchrow(
            query,
            discord_id
        )


async def add_coins(discord_id: int, amount: int):

    query = """
    UPDATE users
    SET coins = coins + $1
    WHERE discord_id = $2;
    """

    async with db.acquire() as conn:
        await conn.execute(
            query,
            amount,
            discord_id
        )


async def add_xp(discord_id: int, amount: int):

    query = """
    UPDATE users
    SET xp = xp + $1
    WHERE discord_id = $2;
    """

    async with db.acquire() as conn:
        await conn.execute(
            query,
            amount,
            discord_id
        )


async def set_last_work(discord_id: int):

    query = """
    UPDATE users
    SET last_work = $1
    WHERE discord_id = $2;
    """

    async with db.acquire() as conn:
        await conn.execute(
            query,
            datetime.utcnow(),
            discord_id
        )


async def level_up(discord_id: int):

    player = await get_player(discord_id)

    if not player:
        return False

    level = player["level"]
    xp = player["xp"]

    need_xp = level * 100

    if xp < need_xp:
        return False


    query = """
    UPDATE users
    SET 
        level = level + 1,
        xp = xp - $1
    WHERE discord_id = $2;
    """

    async with db.acquire() as conn:
        await conn.execute(
            query,
            need_xp,
            discord_id
        )

    return True


async def change_region(discord_id: int, region: str):

    query = """
    UPDATE users
    SET region = $1
    WHERE discord_id = $2;
    """

    async with db.acquire() as conn:
        await conn.execute(
            query,
            region,
            discord_id
        )
