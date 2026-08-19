Ты работаешь над существующим проектом ILTA BOT.

ТВОЯ ЗАДАЧА — НЕ ПИСАТЬ НОВЫЙ КОД СРАЗУ.

Сначала проведи ПОЛНЫЙ АУДИТ ВСЕГО ПРОЕКТА.

============================================================
ГЛАВНОЕ ПРАВИЛО
============================================================

НЕ ИЗМЕНЯЙ НИ ОДИН ФАЙЛ НА ЭТАПЕ АУДИТА.

НЕ УДАЛЯЙ КОД.

НЕ ПЕРЕПИСЫВАЙ МОДУЛИ.

НЕ СОЗДАВАЙ НОВУЮ АРХИТЕКТУРУ.

НЕ ИСПРАВЛЯЙ ПРОБЛЕМЫ МОЛЧА.

Сначала исследуй проект полностью и составь отчёт.

После отчёта дождись моего разрешения на исправления.

============================================================
1. ПОЛНОСТЬЮ ИССЛЕДУЙ РЕПОЗИТОРИЙ
============================================================

Просмотри весь проект:

- main.py
- cogs/
- core/
- database/
- generators/
- data/
- assets/
- utils/
- config/
- migrations/
- scripts/
- tests/
- requirements.txt
- .env.example
- README
- все конфигурационные файлы

Также найди любые другие директории и файлы,
которые используются приложением.

Не ограничивайся только очевидными файлами.

============================================================
2. ПОСТРОЙ КАРТУ ПРОЕКТА
============================================================

Определи:

ENTRY POINT
↓
BOT INITIALIZATION
↓
DATABASE
↓
COGS
↓
SERVICES
↓
GENERATORS
↓
ASSETS
↓
DISCORD UI
↓
USER ACTIONS

Для каждого основного модуля объясни:

- зачем он нужен;
- кто его вызывает;
- какие модули он вызывает;
- какие данные получает;
- какие данные возвращает;
- какие database tables использует;
- какие assets использует.

============================================================
3. ПРОАНАЛИЗИРУЙ DEPENDENCIES
============================================================

Проверь:

requirements.txt

imports

version compatibility

unused dependencies

duplicate libraries

potential conflicts

circular imports

dead imports

missing imports

runtime-only dependencies

Также проверь Python version compatibility.

============================================================
4. ПРОАНАЛИЗИРУЙ DATABASE
============================================================

Найди все:

CREATE TABLE

ALTER TABLE

INSERT

SELECT

UPDATE

DELETE

transactions

database pools

queries

repositories

database helpers.

Определи все таблицы.

Для каждой таблицы показать:

- columns;
- primary keys;
- foreign keys;
- unique constraints;
- indexes;
- defaults;
- relationships.

Особенно проверить:

players

cards

inventory

packs

chests

rewards

collection

quests

economy

shop

purchases

если такие таблицы существуют.

НЕ ПРЕДПОЛАГАЙ существование таблиц.
Смотри фактический код.

============================================================
5. ПРОАНАЛИЗИРУЙ CARD SYSTEM
============================================================

Полностью проследи:

card data

↓

champion data

↓

skin data

↓

rarity

↓

region

↓

lore

↓

card generator

↓

PNG

↓

collection

↓

inventory

↓

pack opening

↓

battle

↓

profile

Найди все места,
где карта создаётся,
хранится,
показывается
и передаётся пользователю.

============================================================
6. ПРОАНАЛИЗИРУЙ CARD GENERATOR
============================================================

Особенно внимательно проверить:

card_generator.py

Проверить:

- canvas;
- frame;
- art;
- art mask;
- transparency;
- fonts;
- icons;
- ATK;
- DEF;
- HP;
- Lore;
- rarity;
- region;
- card number;
- output path;
- return value.

Определить:

Что функция generate_card()
фактически возвращает:

Path?

str?

PIL.Image?

bytes?

Найти ВСЕ места,
где результат этой функции используется.

Проверить совместимость
return value с вызывающим кодом.

============================================================
7. ПРОАНАЛИЗИРУЙ ASSETS
============================================================

Просканируй assets/.

Создай карту:

ASSET TYPE
↓
DIRECTORY
↓
FILES
↓
CODE REFERENCES

Особенно:

cards

frames

packs

chests

champions

skins

regions

icons

backgrounds

profile

shop

inventory

battle.

Проверить:

- существование файлов;
- расширения;
- регистр имён;
- дубликаты;
- отсутствующие assets;
- неправильные пути;
- assets, которые существуют,
  но никогда не используются;
- code references на несуществующие assets.

============================================================
8. ОСОБЕННО ПРОВЕРЬ ИЗОБРАЖЕНИЯ
============================================================

Найди ВСЕ места,
где изображения отправляются в Discord.

Ищи:

discord.File

Embed

set_image

set_thumbnail

attachment://

send

reply

followup.send

edit_message

interaction.response

interaction.followup

message.edit

message.reply

Также найти:

BytesIO

PIL.Image

Image.open

save

temporary files.

Для каждого image pipeline
построить цепочку:

SOURCE
↓
PATH
↓
PIL
↓
FILE
↓
DISCORD ATTACHMENT
↓
EMBED
↓
MESSAGE

============================================================
9. ОСОБЕННО ПРОВЕРИТЬ ТЕКУЩУЮ ПРОБЛЕМУ
============================================================

Сейчас есть проблемы:

1. Pack images не показываются.

2. Chest images не показываются.

3. Generated card images внутри Pack
   перестали показываться.

4. Inventory/Shop могут использовать
   разные image mechanisms.

Найди ОБЩУЮ ПРИЧИНУ.

Не просто исправляй отдельный Pack.

Нужно определить,
где ломается общий image pipeline.

============================================================
10. PACK SYSTEM
============================================================

Полностью проследи:

Shop

↓

Pack details

↓

Purchase

↓

Confirmation

↓

Inventory

↓

Open Pack

↓

Reward generation

↓

Card generation

↓

Card image

↓

Card reveal

↓

Navigation

Проверить каждую функцию
в этой цепочке.

============================================================
11. CHEST SYSTEM
============================================================

То же самое:

Shop

↓

Chest

↓

Purchase

↓

Inventory

↓

Open

↓

Rewards

↓

Images

↓

Result.

============================================================
12. INVENTORY
============================================================

Полностью проанализировать:

/inventory

/menu → inventory

categories

pagination

buttons

select menus

item details

packs

chests

cards

cosmetics

items

boosters.

Определить:

- какие данные берутся из DB;
- какие assets используются;
- как формируется UI;
- как обрабатываются buttons;
- как проверяется user ID.

============================================================
13. SHOP
============================================================

Проверить:

item registry

prices

currencies

purchase

confirmation

transaction

inventory insertion

purchase history.

Особенно проверить:

можно ли:

- повторно нажать Confirm;
- купить при недостатке денег;
- подменить item ID;
- подменить price;
- совершить race condition;
- купить предмет дважды.

============================================================
14. DISCORD INTERACTIONS
============================================================

Найти ВСЕ:

commands

buttons

select menus

modals

views

callbacks.

Проверить:

- interaction timeout;
- defer;
- response already used;
- followup;
- message edit;
- ephemeral;
- permissions;
- ownership checks.

Особенно проверить,
что пользователь A не может нажать
кнопки меню пользователя B.

============================================================
15. /MENU
============================================================

Полностью проследить:

/menu

↓

Profile

Collection

Inventory

Shop

Battle

Kingdom

LFG

Events

Achievements

Settings

и другие реально существующие разделы.

Проверить navigation graph.

Найти dead buttons.

Найти кнопки,
которые вызывают несуществующие функции.

Найти функции,
которые невозможно вызвать из UI.

============================================================
16. LOCALIZATION
============================================================

Проверить RU / EN.

Найти:

hardcoded Russian text

hardcoded English text

missing translations

unused translations

duplicate keys

missing keys.

Проверить,
что UI действительно использует
выбранный пользователем язык.

============================================================
17. ECONOMY
============================================================

Проверить:

Gold

Crystals

Card Shards

XP

другие валюты.

Найти все источники валюты.

Найти все sinks.

Построить:

SOURCE → CURRENCY → SINK

Проверить:

- возможные infinite money exploits;
- duplicate rewards;
- повторную выдачу rewards;
- race conditions;
- отрицательные balances;
- integer overflow;
- bypass cooldown;
- alt-account abuse.

============================================================
18. REWARD SYSTEM
============================================================

Полностью проследить:

reward generation

↓

cards

↓

gold

↓

shards

↓

items

↓

packs

↓

chests

↓

duplicates.

Проверить,
может ли одна награда
выдаваться несколько раз
из-за повторного interaction.

============================================================
19. BATTLE
============================================================

Если Battle уже существует:

полностью проанализировать.

Если Battle частично реализован:

показать текущую архитектуру.

Проверить:

cards

stats

ATK

DEF

HP

damage

turns

rewards

cooldowns.

Не писать новую боёвку.

============================================================
20. LFG
============================================================

Проверить существующую LFG систему:

create

search

join

leave

close

expiration

notifications.

Проверить race conditions
и старые sessions.

============================================================
21. KINGDOM
============================================================

Проверить:

server

kingdom

level

buildings

treasury

events

server progression.

Понять,
как Discord server ID связан
с игровым Kingdom.

============================================================
22. SECURITY AUDIT
============================================================

Проверить:

SQL injection

unsafe SQL construction

permission bypass

button ownership

admin commands

user input

path traversal

file path manipulation

arbitrary file access

unsafe eval

exec

subprocess

pickle

secrets exposure

.env usage

token exposure.

НЕ выводить реальные secrets
в отчёте.

Если найден secret:

написать только:

SECRET FOUND

без значения.

============================================================
23. ASYNC / CONCURRENCY AUDIT
============================================================

Проверить:

await

asyncio

database pool

transactions

race conditions

concurrent interactions

double clicks

double rewards

double purchases

simultaneous pack opening.

Особенно проверить места:

balance update

inventory update

reward claim

purchase

card generation.

============================================================
24. ERROR HANDLING
============================================================

Найти:

bare except

except Exception

silent failures

pass

missing logging

unhandled exceptions.

Особенно Discord errors:

NotFound

Forbidden

HTTPException

InteractionResponded

NotFound message

Unknown interaction.

============================================================
25. DEAD CODE
============================================================

Найти:

unused files

unused functions

unused classes

unused imports

old implementations

duplicate systems

legacy code

temporary debug code.

НЕ удалять.

Только перечислить.

============================================================
26. DUPLICATE SYSTEMS
============================================================

Найти дубли:

multiple asset loaders

multiple inventory implementations

multiple reward systems

multiple card generators

multiple shop systems

multiple translation systems

multiple database helpers

multiple image send helpers.

Если несколько систем делают
одно и то же:

показать их.

============================================================
27. IMPORT GRAPH
============================================================

Построить dependency graph.

Особенно проверить circular imports:

main
↓
cogs
↓
database
↓
generators
↓
data.

============================================================
28. FILE PATH AUDIT
============================================================

Найти все:

os.path

Path

join

dirname

__file__

cwd

relative paths

absolute paths.

Проверить,
что проект одинаково работает
при запуске:

python main.py

и из другой working directory.

============================================================
29. CONFIGURATION AUDIT
============================================================

Проверить:

.env

environment variables

database URL

Discord token

API keys

asset root

debug flags.

НЕ выводить secrets.

============================================================
30. PERFORMANCE
============================================================

Найти:

- повторную загрузку PNG;
- повторное открытие fonts;
- повторные DB queries;
- N+1 queries;
- слишком большие images;
- блокирующий код внутри async;
- requests вместо aiohttp;
- unnecessary API calls.

============================================================
31. TEST COVERAGE
============================================================

Найти существующие tests.

Определить критические функции,
которые вообще не тестируются.

Особенно:

purchase

reward

pack opening

card generation

inventory

database transactions

image sending.

============================================================
32. СОЗДАЙ AUDIT REPORT
============================================================

После полного анализа НЕ ИЗМЕНЯЙ КОД.

Создай подробный отчёт.


ФОРМАТ:

# ILTA FULL PROJECT AUDIT


## 1. PROJECT HEALTH

Overall:
CRITICAL / BAD / FAIR / GOOD / EXCELLENT


## 2. ARCHITECTURE

Описание архитектуры.


## 3. CRITICAL BUGS

P0 — критические

P1 — серьёзные

P2 — средние

P3 — мелкие


Для каждого:

BUG

FILE

FUNCTION

ROOT CAUSE

IMPACT

RECOMMENDED FIX


## 4. CURRENT IMAGE PIPELINE

Показать реальную цепочку:

Pack asset
→
Asset loader
→
Path
→
discord.File
→
attachment
→
Embed
→
Message


И отдельно:

Card Generator
→
PNG
→
Discord


Обязательно указать,
на каком этапе происходит проблема.


## 5. PACK PROBLEM

Почему Pack image
не отображается.


## 6. CHEST PROBLEM

Почему Chest image
не отображается.


## 7. GENERATED CARD PROBLEM

Почему generated cards
перестали отображаться.


## 8. CARD GENERATOR

Состояние:

WORKING / BROKEN / PARTIAL


## 9. DATABASE

Tables

Relations

Potential problems.


## 10. INVENTORY

Current implementation

Missing features

Problems.


## 11. SHOP

Current implementation

Problems.


## 12. /MENU

Navigation problems.


## 13. ECONOMY

Sources

Sinks

Exploits.


## 14. SECURITY

Critical vulnerabilities.


## 15. PERFORMANCE

Problems.


## 16. DEAD CODE

List.


## 17. DUPLICATE SYSTEMS

List.


## 18. TECHNICAL DEBT

List.


## 19. RECOMMENDED FIX ORDER

Например:


PHASE 1
Critical bugs


PHASE 2
Image pipeline


PHASE 3
Database


PHASE 4
Inventory


PHASE 5
Shop


PHASE 6
UI


PHASE 7
Optimization


============================================================
33. MOST IMPORTANT
============================================================

НЕ ПРЕДЛАГАЙ 100 РАЗНЫХ
ПЕРЕПИСЫВАНИЙ ПРОЕКТА.

Сначала определить:

ЧТО СЛОМАНО

ПОЧЕМУ СЛОМАНО

ГДЕ СЛОМАНО

КАКОЙ МИНИМАЛЬНЫЙ FIX НУЖЕН.


============================================================
34. AFTER AUDIT
============================================================

После отчёта остановись.

НЕ ИЗМЕНЯЙ ФАЙЛЫ,
ПОКА Я НЕ НАПИШУ:

"НАЧИНАЙ ИСПРАВЛЯТЬ"


============================================================
END OF AUDIT
============================================================
