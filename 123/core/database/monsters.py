from core import database


# Получить монстра по региону

async def get_monster(region):

    query = """
    SELECT *
    FROM monsters
    WHERE region = $1
    ORDER BY RANDOM()
    LIMIT 1;
    """


    async with database.db.acquire() as conn:

        return await conn.fetchrow(
            query,
            region
        )
