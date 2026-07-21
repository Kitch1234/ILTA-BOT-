from core.database import db


async def get_quests(region):

    query = """
    SELECT *
    FROM quests
    WHERE region = $1;
    """

    async with db.acquire() as conn:
        return await conn.fetch(
            query,
            region
        )


async def get_quest(quest_id):

    query = """
    SELECT *
    FROM quests
    WHERE id = $1;
    """

    async with db.acquire() as conn:
        return await conn.fetchrow(
            query,
            quest_id
        )
