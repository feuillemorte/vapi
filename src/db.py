"""Database functionality."""
import sqlite3
from datetime import datetime

TIMESTAMP_FIELDS = ["created", "updated"]


def _get_conn():
    """Gets DB connction to perform queries."""
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
        print(f"SELECT * FROM {tablename} {where}")
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
    insert(tablename="pets", columns=["name"], values=["Floof"])
    insert(tablename="pets", columns=["name"], values=["Snow"])
