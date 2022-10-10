import sqlite3

conn = sqlite3.connect("book.sqlite")

cursor = conn.cursor() # Cursor object is used to execute SQL statement.
sqlQuery = """ CREATE TABLE books(
    id integer PRIMARY KEY,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL
)
"""
cursor.execute(sqlQuery)