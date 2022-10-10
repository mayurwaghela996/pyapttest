import pymysql

conn = pymysql.connect(
    host = 'sql6.freesqldatabase.com',
    database = "sql6524367",
    user = 'sql6524367',
    password = 'NsDtvQzUTV',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

cursor = conn.cursor() # Cursor object is used to execute SQL statement.
sqlQuery = """ CREATE TABLE books1(
    id integer PRIMARY KEY AUTOINCREMENT,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL
)
"""


cursor.execute(sqlQuery)
conn.close()