"""Handle SQLite connections and retrieve database object."""

import sqlite3

from flask import g

# g is a context variable, stores data during request context

DATABASE = "./database/database.db"


def get_db() -> sqlite3.Connection:
    """
    Open database connection, or get existing database if connection already open.

    :return: an sqlite3.Connection object.
    """
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.execute("pragma busy_timeout=10000")
    #print("Connection to database established")
    return db


def close_connection() -> None:
    """
    Properly close database access from the app.

    :return: None (database closed).
    """
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()
        print("Database connection closed")
