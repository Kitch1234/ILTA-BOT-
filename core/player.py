from core.database import db


async def create_player(discord_id, username):
    query = """
    INSERT INTO users (
        discord_id,
        username
    )
    VALUES ($1, $2)
    ON CONFLICT (discord_id)
    DO NOTHING;
    """

    await db.execute(
        query,
        discord_id,
        username
    )


async def get_player(discord_id):
    query = """
    SELECT *
    FROM users
    WHERE discord_id = $1;
    """

    player = await db.fetchrow(
        query,
        discord_id
    )

    return player


async def update_coins(discord_id, amount):
    query = """
    UPDATE users
    SET coins = coins + $1
    WHERE discord_id = $2;
    """

    await db.execute(
        query,
        amount,
        discord_id
    )


async def add_xp(discord_id, amount):
    query = """
    UPDATE users
    SET xp = xp + $1
    WHERE discord_id = $2;
    """

    await db.execute(
        query,
        amount,
        discord_id
    )
