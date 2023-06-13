"""Database functionality."""
import sqlite3
from datetime import datetime

TIMESTAMP_FIELDS = ["created", "updated"]


def _get_conn():
    """Gets DB connection to perform queries."""
    conn = sqlite3.connect("database.db")

    def dict_factory(cursor, row):
        result = {}
        for idx, col in enumerate(cursor.description):
            column = col[0]
            value = row[idx]
            if column in TIMESTAMP_FIELDS:
                value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
            result[column] = value
        return result

    conn.row_factory = dict_factory

    return conn


def select_all(tablename, where=""):
    """Get all items from the `tablename` table."""
    if where:
        where = f"WHERE {where}"
    with _get_conn() as conn:
        return conn.execute(f"SELECT * FROM {tablename} {where}")


def select_by_id(tablename, item_id):
    """Select the item by id."""
    result = list(select_all(tablename=tablename, where=f"id={item_id}"))
    if result:
        return result[0]
    return None


def insert(tablename, columns, values):
    """Insert a new element into database."""
    with _get_conn() as conn:
        columns_str = ", ".join(columns)
        values_str = ", ".join(list(map(lambda x: f"'{x}'", values)))

        cur = conn.cursor()
        cur.execute(f"INSERT INTO {tablename} ({columns_str}) VALUES ({values_str})")

        return cur.lastrowid


def update(tablename, columns, values, where):
    """Update an existing item in the database."""
    with _get_conn() as conn:
        values = list(map(lambda x: f"'{x}'", values))
        pairs = list(zip(columns, values))
        pairs_str = ",".join("=".join(pair) for pair in pairs)

        cur = conn.cursor()
        cur.execute(f"UPDATE {tablename} SET {pairs_str} WHERE {where}")

        return cur.rowcount


def delete(tablename, where):
    """Delete an existing item in the database."""
    with _get_conn() as conn:
        cur = conn.cursor()
        cur.execute(f"DELETE FROM {tablename} WHERE {where}")

        return cur.rowcount


def is_exists(tablename, column, value):
    """Check if the item is exists in the database."""
    return bool(list(select_all(tablename=tablename, where=f"{column}='{value}'")))


def init():
    """Init the database."""
    with open("schema.sql", encoding="utf-8") as f:
        with _get_conn() as conn:
            conn.executescript(f.read())
    floof_description = """
Floof is an adorable puppy with soft, fluffy fur that is as brown as milk chocolate. His round, dark eyes are full of wonder and excitement as he explores the world around him with boundless energy and enthusiasm. His small, black nose twitches as he sniffs at everything in his path, from the grass beneath his paws to the flowers blooming in the nearby meadow.

Despite his small size, Floof is fearless and full of personality. He loves to play and cuddle, and his tail never stops wagging when he is around people. His playful nature is infectious, and he has a way of brightening up any room with his silly antics and playful barks.

Whether he is chasing after a ball or snuggled up on a cozy blanket, Floof is always eager for adventure and companionship. With his sweet disposition and charming personality, it is impossible not to fall in love with this little bundle of joy.
"""
    snow_description = """
Snow is an exquisite puppy, whose fur is as white as a freshly painted canvas. Her silky coat shimmers in the light, with a delicate sheen that makes her seem almost ethereal. Her eyes are large and expressive, a bright and clear blue that mirrors the sky on a clear summer day.

Her ears are soft and fluffy, and they seem to perk up at the slightest sound, indicating her alertness and intelligence. Snow iss movements are graceful, with an effortless stride that makes her seem almost weightless.

Despite her refined appearance, Snow is a playful and adventurous puppy, always eager to explore and discover new things. Her enthusiasm is infectious, and she has a way of making everyone around her feel happy and uplifted. Whether she is chasing after a ball or snuggling up with her human companions, Snow is a gentle and loving creature who brings joy and warmth wherever she goes.

In short, Snow is a puppy of rare beauty and charm, whose gentle nature and joyful spirit make her a beloved companion to all who have the good fortune to know her.
"""
    lunarie_description = """
Lunaire is a unique and mystical puppy that will capture your heart with her ethereal beauty and playful nature. Her coat is a shimmering silver-gray color that glistens in the sunlight and gives her an otherworldly appearance.

Despite her enchanting appearance, Lunaire is also a friendly and outgoing puppy who loves to play and explore. She is curious and adventurous, always eager to discover new sights and smells. Her energy and enthusiasm are contagious, and she will bring joy and laughter to any home.

Lunaire is also a loyal and loving companion, always eager to be by your side and share in your adventures. She is intelligent and trainable, making her a great choice for families who want a smart and obedient puppy. Whether you are looking for a hiking buddy or a couch potato, Lunaire is the perfect mix of beauty, brains, and fun-loving spirit.
"""
    insert(
        tablename="pets",
        columns=["name", "description", "img_url"],
        values=["Floof", floof_description, "/img/pets/floof.jpeg"],
    )
    insert(
        tablename="pets",
        columns=["name", "description", "img_url"],
        values=["Snow", snow_description, "/img/pets/snow.jpeg"],
    )
    insert(
        tablename="pets",
        columns=["name", "description", "img_url"],
        values=["Lunaire", lunarie_description, "/img/pets/lunaire.jpeg"],
    )
