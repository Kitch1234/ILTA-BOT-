# models.py


CREATE_TABLES = """


CREATE TABLE IF NOT EXISTS players (

    id BIGINT PRIMARY KEY,

    username TEXT,

    level INTEGER DEFAULT 1,

    experience INTEGER DEFAULT 0,

    gold INTEGER DEFAULT 0,


    health INTEGER DEFAULT 100,

    attack INTEGER DEFAULT 10,

    defense INTEGER DEFAULT 5,


    location TEXT DEFAULT 'Демасия'

);



CREATE TABLE IF NOT EXISTS cards (

    id SERIAL PRIMARY KEY,

    owner_id BIGINT REFERENCES players(id),

    champion TEXT,

    skin TEXT,

    rarity TEXT,

    level INTEGER DEFAULT 1

);



CREATE TABLE IF NOT EXISTS inventory (

    id SERIAL PRIMARY KEY,

    owner_id BIGINT REFERENCES players(id),

    item TEXT,

    amount INTEGER DEFAULT 1

);



CREATE TABLE IF NOT EXISTS quests (

    id SERIAL PRIMARY KEY,

    owner_id BIGINT REFERENCES players(id),

    quest TEXT,

    completed BOOLEAN DEFAULT FALSE

);


"""
