from core.database import db


async def get_quests(region):

    query = """
    SELECT *
    FROM quests
    WHERE region = $1;
    """

    async with db.acquire() as conn:
        return await conn.fetch(query, region)


async def get_quest(quest_id):

    query = """
    SELECT *
    FROM quests
    WHERE id = $1;
    """

    async with db.acquire() as conn:
        return await conn.fetchrow(query, quest_id)


async def accept_quest(discord_id, quest_id):

    query = """
    INSERT INTO player_quests (
        discord_id,
        quest_id
    )
    VALUES ($1, $2);
    """

    async with db.acquire() as conn:
        await conn.execute(
            query,
            discord_id,
            quest_id
        )


async def get_player_quests(discord_id):

    query = """
    SELECT *
    FROM player_quests
    WHERE discord_id = $1;
    """

    async with db.acquire() as conn:
        return await conn.fetch(
            query,
            discord_id
        )
