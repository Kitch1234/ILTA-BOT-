from core import database



# ==========================
# Создать бой
# ==========================

async def create_battle(
        user_id,
        monster_id
):

    query = """
    INSERT INTO battles
    (
        user_id,
        enemy_id,
        status
    )

    VALUES
    (
        $1,
        $2,
        'active'
    )

    RETURNING id;
    """


    async with database.db.acquire() as conn:

        battle_id = await conn.fetchval(
            query,
            user_id,
            monster_id
        )


    return battle_id



# ==========================
# Завершить бой
# ==========================

async def finish_battle(
        battle_id
):

    query = """
    UPDATE battles

    SET status = 'completed'

    WHERE id = $1;
    """


    async with database.db.acquire() as conn:

        await conn.execute(
            query,
            battle_id
        )



# ==========================
# Получить активный бой
# ==========================

async def get_active_battle(
        user_id
):

    query = """
    SELECT *

    FROM battles

    WHERE user_id = $1

    AND status = 'active'

    LIMIT 1;
    """


    async with database.db.acquire() as conn:

        return await conn.fetchrow(
            query,
            user_id
        )
