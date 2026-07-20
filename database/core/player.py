from core.database import db


async def create_player(discord_id, username):

    print("CREATE PLAYER START")

    query = """
    INSERT INTO users (
        discord_id,
        username,
        level,
        xp,
        coins
    )
    VALUES ($1, $2, 1, 0, 100)
    ON CONFLICT (discord_id)
    DO NOTHING;
    """

    async with db.acquire() as conn:
        await conn.execute(
            query,
            discord_id,
            username
        )

    print("CREATE PLAYER OK")


async def get_player(discord_id):

    print("GET PLAYER START")

    query = """
    SELECT *
    FROM users
    WHERE discord_id = $1;
    """

    async with db.acquire() as conn:
        player = await conn.fetchrow(
            query,
            discord_id
        )

    print("GET PLAYER OK")

    return player
