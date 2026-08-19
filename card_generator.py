============================================================
ILTA — URGENT IMAGE PIPELINE DEBUG
PACK / CHEST / GENERATED CARD IMAGES
============================================================

КРИТИЧЕСКАЯ ПРОБЛЕМА
============================================================

После последних изменений изображения перестали
отображаться в Discord.

Проблемы одновременно:

1. Не отображаются изображения Pack.
2. Не отображаются изображения Chest.
3. В открытии Pack перестали отображаться
   сгенерированные изображения карт.
4. PNG assets физически существуют в проекте.
5. Card Generator существует и должен продолжать
   генерировать карты.

НЕ ПЕРЕПИСЫВАТЬ SHOP И INVENTORY ЗАНОВО.

Сначала найти точную причину.


============================================================
1. STOP — DO NOT MODIFY YET
============================================================

Перед любыми изменениями провести диагностику.

Найти и показать:

- где загружается Pack image;
- где загружается Chest image;
- где вызывается card_generator;
- где сохраняется generated card;
- какой путь возвращает card_generator;
- где generated card передаётся в Discord;
- где создаётся discord.File;
- где создаётся Embed;
- где вызывается embed.set_image();
- где вызывается message.reply();
- где вызывается interaction.response.send_message();
- где вызывается followup.send();
- где вызывается edit_message();
- где формируется attachment:// URL.

НЕ менять код, пока эти точки не найдены.


============================================================
2. IMPORTANT DISCORD RULE
============================================================

Проверить все места, где используется:

embed.set_image(
    url=...
)


Если URL имеет:

attachment://filename.png


то этот файл ОБЯЗАТЕЛЬНО должен быть
передан в тот же Discord message
как attachment.


Например правильная схема:


file = discord.File(
    image_path,
    filename="rare_pack.png"
)


embed.set_image(
    url="attachment://rare_pack.png"
)


await interaction.followup.send(
    embed=embed,
    file=file
)


НЕ делать:


embed.set_image(
    url="attachment://rare_pack.png"
)


await interaction.followup.send(
    embed=embed
)


Потому что attachment отсутствует.


============================================================
3. MULTIPLE IMAGES
============================================================

Особенно проверить Pack Opening.

Если одновременно показываются:

Pack image

+
несколько generated card images


Discord должен получить все необходимые
attachments в одном сообщении либо система
должна корректно отправлять их отдельно.


Например:


files = [
    discord.File(pack_path, filename="pack.png"),
    discord.File(card1_path, filename="card_1.png"),
    discord.File(card2_path, filename="card_2.png")
]


НЕЛЬЗЯ создавать:

file = discord.File(...)


затем:

await send(file=file)


а после этого пытаться использовать
тот же file object снова.


Каждый Discord File object
должен использоваться корректно.


============================================================
4. PACK IMAGE DEBUG
============================================================

Для каждого Pack перед отправкой
добавить DEBUG LOG:


PACK IMAGE DEBUG

pack_id:
pack_name:
asset_key:
resolved_path:
exists:
is_file:
size:
format:


Пример:


PACK IMAGE DEBUG
pack_id=rare_pack
asset_key=rare_pack
resolved_path=/project/assets/packs/rare.png
exists=True
is_file=True
size=182934
format=PNG


Если exists=False:

НЕ продолжать отправку.


Показать точный path,
который система пытается открыть.


============================================================
5. CHEST IMAGE DEBUG
============================================================

То же самое:


CHEST IMAGE DEBUG

chest_id:
asset_key:
resolved_path:
exists:
is_file:
size:
format:


============================================================
6. GENERATED CARD DEBUG
============================================================

КРИТИЧЕСКИ ВАЖНО.

Найти:

card_generator.py


и место, где Pack Opening
генерирует карты.


После каждой генерации
выводить:


GENERATED CARD DEBUG

champion:
skin:
rarity:
output_path:
exists:
is_file:
size:


Например:


GENERATED CARD DEBUG

champion=Ahri
skin=Ultimate
rarity=Ultimate
output_path=/project/generated/cards/ahri_ultimate.png
exists=True
is_file=True
size=734221


============================================================
7. DO NOT ASSUME CARD GENERATOR IS BROKEN
============================================================

Проверить отдельно:


card_generator


→ generate card


→ save PNG


→ verify PNG


→ Discord send


Если PNG существует и открывается,
Card Generator считать исправным.


Проблему искать после генерации.


============================================================
8. OPEN GENERATED CARD FILE
============================================================

Для каждой generated card проверить
фактически:


os.path.exists(path)


os.path.isfile(path)


os.path.getsize(path)


PIL.Image.open(path)


PIL.Image.verify()


Если verify() проходит,
значит PNG корректный.


============================================================
9. CRITICAL PATH PROBLEM
============================================================

Проверить различие между:


relative path


absolute path


current working directory


__file__


project root


Например:


assets/cards/...


может работать из:


main.py


но не работать из:


cogs/pack.py


Не использовать случайные:


../../assets


../../../assets


Использовать единый PROJECT_ROOT.


Например:


PROJECT_ROOT = Path(__file__).resolve().parents[...] 


Но сначала определить правильный
root проекта по существующей структуре.


============================================================
10. ASSET MANAGER
============================================================

Если AssetManager уже существует:

НЕ создавать второй.


Исправить существующий.


Если его нет:

создать один.


Он должен возвращать:


Path


а не Discord URL.


Например:


asset_manager.get_pack_asset("rare_pack")


→ Path(.../rare.png)


А Discord layer уже решает,
как превратить Path в attachment.


НЕ смешивать filesystem
и Discord URL.


============================================================
11. IMPORTANT ARCHITECTURE
============================================================

Разделить:


FILESYSTEM LAYER


AssetManager


↓


Path


DISCORD PRESENTATION LAYER


DiscordImage


↓


discord.File


↓


attachment://filename


Это должно быть разделено.


============================================================
12. DISCORD IMAGE HELPER
============================================================

Создать ОДИН helper,
если аналогичного уже нет:


create_discord_image_attachment(path, filename)


Он должен:


1. проверить существование;
2. проверить файл;
3. создать discord.File;
4. вернуть File + attachment URL.


Например логика:


file = discord.File(
    str(path),
    filename=filename
)


url = f"attachment://{filename}"


return file, url


Все Pack / Chest / Card
изображения должны использовать
один и тот же механизм.


============================================================
13. GENERATED CARD SEND
============================================================

Найти текущую систему,
которая раньше показывала
сгенерированные карты.


НЕ заменять card_generator.


Нужно восстановить:


generated PNG


↓


discord.File


↓


attachment://...


↓


Discord message


============================================================
14. PACK OPENING
============================================================

Проверить полный pipeline:


OPEN PACK


↓


calculate rewards


↓


generate cards


↓


save cards


↓


verify cards


↓


create Discord files


↓


create embed/message


↓


send attachments


↓


display cards


Если любой этап возвращает
None / invalid path / missing file,
остановиться и вывести DEBUG.


============================================================
15. IMPORTANT — FILE LIFETIME
============================================================

Проверить, что discord.File
не закрывается до отправки сообщения.


Не делать:


with open(...) as f:
    file = discord.File(f)


а затем отправлять
после выхода из context.


Также проверить временные
generated files.


Если generated card сохраняется
во временный каталог,
файл не должен удаляться
до момента завершения Discord upload.


============================================================
16. PACK + CARDS
============================================================

Если Pack Opening показывает:


Pack image


и


generated cards


проверить, как именно
реализовано сообщение.


Если используется один embed:

Discord Embed имеет
только одну основную image URL.


Поэтому НЕ пытаться положить
несколько card images
в один embed.set_image().


Для нескольких карт использовать
существующую систему:


- отдельные attachments;
- отдельные embeds/messages;
- или существующий carousel/navigation.


Не ломать текущий UX.


============================================================
17. EXISTING CARD REVEAL FLOW
============================================================

В проекте ранее планировался
Pack Opening:

один message


+
pack image


+
Open button


+
card reveal


+
full card image


+
arrow navigation.


Сохранить именно этот UX.


При открытии карты:


[ ← ] [ → ]


и большая generated card image.


Не отправлять новую карту
в случайный канал.


Не создавать несколько
бессмысленных сообщений.


============================================================
18. CARD REVEAL IMAGE
============================================================

При переходе:

Card 1 → Card 2


нужно корректно заменить
image attachment/embed.


ВАЖНО:

Discord attachment старого
сообщения нельзя просто заменить
новым локальным path.


Нужно заново отправить/редактировать
message с новым attachment
в соответствии с Discord API.


Проверить существующую реализацию.


============================================================
19. EMBED IMAGE URL
============================================================

Проверить все:

embed.set_image()


embed.set_thumbnail()


embed.set_author()


attachment://


и убедиться,
что URL соответствует
реальному filename attachment.


Например:


filename="card_1.png"


тогда:


attachment://card_1.png


НЕ:


attachment://card.png


НЕ:


attachment://generated/card_1.png


НЕ:


локальный filesystem path.


============================================================
20. UNIQUE FILENAMES
============================================================

Для generated cards использовать
уникальные filenames.


Например:


pack_123_card_1.png


pack_123_card_2.png


pack_123_card_3.png


Чтобы Discord/client/cache
не путал одинаковые filenames.


============================================================
21. DO NOT USE SAME FILENAME
============================================================

Не делать:


card.png


card.png


card.png


для нескольких generated images
в одном flow.


Использовать уникальные имена.


============================================================
22. PACK ASSET FILENAME
============================================================

Pack asset:

rare_pack.png


filename должен совпадать
с attachment URL:


attachment://rare_pack.png


Chest:


mythic_chest.png


→


attachment://mythic_chest.png


============================================================
23. TEST RAW DISCORD IMAGE
============================================================

Создать отдельный временный
debug/test mechanism.


Отправить ОДИН существующий PNG
в Discord без Embed.


Например:


await channel.send(
    file=discord.File(path)
)


Если изображение отображается:


filesystem + Discord upload работают.


После этого протестировать:


file + embed.set_image()


Если первый работает,
а второй нет — проблема
в embed attachment URL.


============================================================
24. TEST GENERATED CARD
============================================================

Сгенерировать одну карту.


Не через Pack.


Напрямую:


card_generator


↓


PNG


↓


discord.File


↓


Discord.


Если карта отображается:

card_generator исправен.


Затем:


Pack


↓


generate card


↓


Discord.


Если здесь ломается:

проблема в Pack Opening integration.


============================================================
25. DO NOT CHANGE CARD GENERATOR
============================================================

НЕ менять:

ART_WIDTH


ART_HEIGHT


ART_X


ART_Y


без доказательства,
что проблема именно там.


Текущая рабочая конфигурация:


ART_WIDTH = 930
ART_HEIGHT = 950
ART_X = 60
ART_Y = 93


Сохранить.


============================================================
26. CHECK CARD GENERATOR RETURN VALUE
============================================================

Очень важно.


Если:


generate_card(...)


раньше возвращал:


Path


а новый код ожидает:


str


или наоборот,


исправить interface.


Проверить:


return value


тип:


Path


str


bytes


PIL.Image


и место использования.


Не делать:


str(path)


если следующий код ожидает
PIL Image.


============================================================
27. CHECK DATABASE
============================================================

Не хранить filesystem path
generated card в database,
если карта должна быть
перегенерирована.


Проверить existing architecture.


Card identity:


card_id


champion


skin


rarity


etc.


Image path должен
получаться через Card Generator
или asset system.


============================================================
28. DO NOT BREAK COLLECTION
============================================================

После исправления Pack Opening
проверить:


Collection


Inventory


Cards


Rewards


Profile


Battle


не должны перестать
работать.


============================================================
29. FINAL DEBUG MATRIX
============================================================

Обязательно проверить:


TEST A
Pack PNG direct send


TEST B
Pack PNG + embed


TEST C
Chest PNG direct send


TEST D
Chest PNG + embed


TEST E
Generated Card direct send


TEST F
Generated Card + embed


TEST G
Pack → generated card


TEST H
Pack → multiple generated cards


TEST I
Pack → navigation


TEST J
Inventory → Pack image


TEST K
Shop → Pack image


TEST L
Purchase Confirmation → Pack image


============================================================
30. REQUIRED DEBUG OUTPUT
============================================================

После запуска тестов вывести:


IMAGE PIPELINE REPORT


PACK ASSETS
----------------
common_pack: PASS/FAIL
rare_pack: PASS/FAIL
epic_pack: PASS/FAIL
legendary_pack: PASS/FAIL
mythic_pack: PASS/FAIL
prestige_pack: PASS/FAIL
ultimate_pack: PASS/FAIL


CHEST ASSETS
----------------
...


GENERATED CARDS
----------------
direct generation: PASS/FAIL
discord upload: PASS/FAIL
pack integration: PASS/FAIL
reveal navigation: PASS/FAIL


============================================================
31. IMPORTANT
============================================================

НЕ говорить:

"Path выглядит правильно"


Нужно реально проверить:


exists


open


PIL verify


Discord upload


Embed display.


============================================================
32. FIND ROOT CAUSE
============================================================

В конце обязательно написать:


ROOT CAUSE:


Например:


1. Asset path incorrect.


или:


2. discord.File was not attached
   to the message.


или:


3. attachment:// filename mismatch.


или:


4. generated card path was lost
   between card_generator and pack.py.


или:


5. temporary file was deleted
   before Discord upload.


или:


6. multiple images were incorrectly
   placed into one Embed.


или:


7. interaction.followup/edit_message
   did not include the new attachment.


Не писать общий ответ.


Найти конкретную причину.


============================================================
33. FIX
============================================================

После нахождения причины
исправить её минимально.


Не делать большой rewrite.


Не создавать новую
параллельную систему.


Использовать существующую
архитектуру ILTA.


============================================================
34. REGRESSION TEST
============================================================

После исправления проверить:


Shop
✓ Pack image


Shop
✓ Chest image


Purchase confirmation
✓ Pack image


Purchase confirmation
✓ Chest image


Inventory
✓ Pack image


Inventory
✓ Chest image


Pack Opening
✓ Pack image


Pack Opening
✓ Generated card image


Pack Opening
✓ Arrow navigation


Collection
✓ Card


Profile
✓ Card


============================================================
35. FINAL REPORT
============================================================

В конце предоставить:


1. ROOT CAUSE


2. Исправленные файлы


3. Что было сломано


4. Почему изображения не отображались


5. Почему generated cards
   перестали отображаться


6. Как теперь работает
   image pipeline


7. Результаты тестов


8. Неизменённые системы


============================================================
END
============================================================
