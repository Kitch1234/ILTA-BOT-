# auction_queries.py

"""
Запросы для аукциона ILTA RPG
"""





async def create_auction(

        pool,

        seller_id,

        card_id,

        price,

        end_time

):

    """
    Создать новый лот
    """


    query = """

    INSERT INTO auctions

    (
        seller_id,
        card_id,
        start_price,
        current_bid,
        end_time
    )

    VALUES

    ($1,$2,$3,$3,$4);

    """



    async with pool.acquire() as connection:


        return await connection.fetchrow(

            query,

            seller_id,

            card_id,

            price,

            end_time

        )








async def get_active_auctions(

        pool

):

    """
    Получить активные лоты
    """


    query = """

    SELECT *

    FROM auctions

    WHERE active = TRUE

    ORDER BY created_at DESC;

    """



    async with pool.acquire() as connection:


        return await connection.fetch(

            query

        )







async def get_auction(

        pool,

        auction_id

):

    """
    Найти конкретный лот
    """


    query = """

    SELECT *

    FROM auctions

    WHERE id=$1;

    """



    async with pool.acquire() as connection:


        return await connection.fetchrow(

            query,

            auction_id

        )







async def place_bid(

        pool,

        auction_id,

        user_id,

        amount

):

    """
    Сделать ставку
    """



    query = """

    UPDATE auctions


    SET

    current_bid=$1,

    highest_bidder=$2


    WHERE id=$3

    AND current_bid < $1

    AND active=TRUE;

    """



    async with pool.acquire() as connection:


        result = await connection.execute(

            query,

            amount,

            user_id,

            auction_id

        )


        return result







async def finish_auction(

        pool,

        auction_id

):

    """
    Завершить аукцион
    """



    query = """

    UPDATE auctions

    SET active=FALSE

    WHERE id=$1;

    """



    async with pool.acquire() as connection:


        await connection.execute(

            query,

            auction_id

        )







async def get_winner(

        pool,

        auction_id

):

    """
    Получить победителя
    """



    query = """

    SELECT

    highest_bidder

    FROM auctions

    WHERE id=$1;

    """



    async with pool.acquire() as connection:


        return await connection.fetchval(

            query,

            auction_id

        )
