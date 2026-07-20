# movement.py

"""
Система перемещения ILTA RPG
"""


from game.world import (

    get_region,

    can_move

)





async def get_player_location(

        pool,

        user_id

):

    """
    Получить текущую позицию игрока
    """

    query = """

    SELECT *

    FROM player_position

    WHERE user_id=$1;

    """



    async with pool.acquire() as connection:


        return await connection.fetchrow(

            query,

            user_id

        )








async def set_player_location(

        pool,

        user_id,

        region_id

):

    """
    Сохранить новую позицию
    """

    query = """

    INSERT INTO player_position

    (

        user_id,

        region_id

    )

    VALUES

    ($1,$2)


    ON CONFLICT(user_id)

    DO UPDATE SET

    region_id=$2;

    """



    async with pool.acquire() as connection:


        await connection.execute(

            query,

            user_id,

            region_id

        )









async def move_player(

        pool,

        user_id,

        target_region

):

    """
    Попытка перемещения
    """



    current = await get_player_location(

        pool,

        user_id

    )



    if not current:


        return {

            "success": False,

            "message":
            "Нет текущей позиции"

        }






    current_region = current["region_id"]



    if not can_move(

        current_region,

        target_region

    ):


        return {

            "success": False,

            "message":
            "Этот путь закрыт"

        }






    region = get_region(

        target_region

    )



    if not region:


        return {

            "success": False,

            "message":
            "Регион не найден"

        }






    await set_player_location(

        pool,

        user_id,

        target_region

    )



    return {


        "success": True,


        "region": region["name"],


        "description":
        region["description"]

    }
