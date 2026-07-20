-- =====================================
-- ILTA RPG DATABASE SCHEMA
-- PostgreSQL
-- =====================================


-- Игроки

CREATE TABLE IF NOT EXISTS players (

    id SERIAL PRIMARY KEY,

    discord_id BIGINT UNIQUE NOT NULL,

    username VARCHAR(100),

    level INTEGER DEFAULT 1,

    xp INTEGER DEFAULT 0,

    gold INTEGER DEFAULT 1000,

    health INTEGER DEFAULT 100,

    max_health INTEGER DEFAULT 100,

    attack INTEGER DEFAULT 10,

    defense INTEGER DEFAULT 5,

    region VARCHAR(100)
        DEFAULT 'Демасия',

    created_at TIMESTAMP DEFAULT NOW()

);



-- =====================================
-- Карты чемпионов
-- =====================================


CREATE TABLE IF NOT EXISTS cards (

    id SERIAL PRIMARY KEY,

    owner_id BIGINT NOT NULL,

    champion VARCHAR(100),

    skin VARCHAR(100),

    rarity VARCHAR(50),

    attack INTEGER DEFAULT 0,

    defense INTEGER DEFAULT 0,

    health INTEGER DEFAULT 0,

    created_at TIMESTAMP DEFAULT NOW()

);





-- =====================================
-- Инвентарь
-- =====================================


CREATE TABLE IF NOT EXISTS inventory (

    id SERIAL PRIMARY KEY,

    user_id BIGINT NOT NULL,

    item VARCHAR(100),

    amount INTEGER DEFAULT 1

);





-- =====================================
-- Квесты игроков
-- =====================================


CREATE TABLE IF NOT EXISTS player_quests (

    id SERIAL PRIMARY KEY,

    user_id BIGINT NOT NULL,

    quest_id VARCHAR(100),

    progress INTEGER DEFAULT 0,

    target INTEGER DEFAULT 1,

    completed BOOLEAN DEFAULT FALSE,

    claimed BOOLEAN DEFAULT FALSE

);





-- =====================================
-- Регионы карты
-- =====================================


CREATE TABLE IF NOT EXISTS regions (

    id SERIAL PRIMARY KEY,

    name VARCHAR(100),

    description TEXT,

    level_required INTEGER DEFAULT 1

);





-- =====================================
-- Позиция игрока на карте
-- =====================================


CREATE TABLE IF NOT EXISTS player_position (

    user_id BIGINT PRIMARY KEY,

    region_id INTEGER,

    x INTEGER DEFAULT 0,

    y INTEGER DEFAULT 0

);





-- =====================================
-- Монстры
-- =====================================


CREATE TABLE IF NOT EXISTS monsters (

    id SERIAL PRIMARY KEY,

    name VARCHAR(100),

    region VARCHAR(100),

    level INTEGER DEFAULT 1,

    health INTEGER,

    attack INTEGER,

    defense INTEGER,

    reward_xp INTEGER,

    reward_gold INTEGER

);





-- =====================================
-- Навыки
-- =====================================


CREATE TABLE IF NOT EXISTS skills (

    id SERIAL PRIMARY KEY,

    name VARCHAR(100),

    description TEXT

);





CREATE TABLE IF NOT EXISTS player_skills (

    user_id BIGINT,

    skill_id INTEGER,

    level INTEGER DEFAULT 1

);





-- =====================================
-- Аукцион
-- =====================================


CREATE TABLE IF NOT EXISTS auctions (

    id SERIAL PRIMARY KEY,

    seller_id BIGINT,

    card_id INTEGER,

    start_price INTEGER,

    current_bid INTEGER DEFAULT 0,

    highest_bidder BIGINT,

    end_time TIMESTAMP,

    active BOOLEAN DEFAULT TRUE

);





-- =====================================
-- Экономика
-- =====================================


CREATE TABLE IF NOT EXISTS economy_logs (

    id SERIAL PRIMARY KEY,

    user_id BIGINT,

    action VARCHAR(100),

    amount INTEGER,

    created_at TIMESTAMP DEFAULT NOW()

);





-- =====================================
-- Достижения
-- =====================================


CREATE TABLE IF NOT EXISTS achievements (

    id SERIAL PRIMARY KEY,

    name VARCHAR(100),

    description TEXT,

    reward INTEGER DEFAULT 0

);



CREATE TABLE IF NOT EXISTS player_achievements (

    user_id BIGINT,

    achievement_id INTEGER,

    unlocked BOOLEAN DEFAULT FALSE

);





-- =====================================
-- Магазин
-- =====================================


CREATE TABLE IF NOT EXISTS shop_items (

    id SERIAL PRIMARY KEY,

    name VARCHAR(100),

    type VARCHAR(50),

    price INTEGER

);





-- =====================================
-- Логи боёв
-- =====================================


CREATE TABLE IF NOT EXISTS battle_logs (

    id SERIAL PRIMARY KEY,

    user_id BIGINT,

    enemy VARCHAR(100),

    result VARCHAR(50),

    reward INTEGER,

    created_at TIMESTAMP DEFAULT NOW()

);
