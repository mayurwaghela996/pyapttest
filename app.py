from flask import Flask, request, jsonify
import json
# import sqlite3
import pymysql

# conn = pymysql.connect


app = Flask(__name__)

def dbConnection():
    conn = None
    try:
        print('DB connection is started')
        conn = pymysql.connect(
            host = 'sql6.freesqldatabase.com',
            database = "sql6524367",
            user = 'sql6524367',
            password = 'NsDtvQzUTV',
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor
        )
        print('DB Connected')
    except pymysql.Error as e:
        print(e)
    return conn


# bookList = [
#     {
#         "id" : 0,
#         "authorName" : "A0",
#         "bookName" : "B0",
#         "title" : "C0",
#     },
#     {
#         "id" : 1,
#         "authorName" : "A1",
#         "bookName" : "B1",
#         "title" : "C1",
#     },
#     {
#         "id" : 2,
#         "authorName" : "A2",
#         "bookName" : "B2",
#         "title" : "C2",
#     },
#     {
#         "id" : 3,
#         "authorName" : "A3",
#         "bookName" : "B3",
#         "title" : "C3",
#     },
# ]

# @app.route('/')
# def index():
#     return 'Hello'

@app.route('/books', methods = ['GET', 'POST'])
def books():
    conn = dbConnection()
    cursor = conn.cursor()
    # cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    if request.method == 'GET':
        cursor.execute("SELECT * FROM books")
        books = [
            dict(id=row['id'], author=row['author'],
            language=row['language'], title=row['title'])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)
        # if len(bookList) > 0:
        #     return jsonify(bookList)
        # else:
        #     'Nothing Found', 404

    if request.method == 'POST':
        newAuthor = request.form['author']
        newLanguage = request.form['language']
        newTitle = request.form['title']
        # id = bookList[-1]['id']+1
        sql = """INSERT INTO books(author, language, title) 
        VALUES(%s, %s, %s)"""

        # newId = bookList[-1]['id'] + 1
        # newObj = {
        #     'id' : newId,
        #     'author' : newAuthor,
        #     'language' : newLanguage, 
        #     'title' : newTitle
        # }
        # bookList.append(newObj)
        # return jsonify(bookList), 201

        bindData = (newAuthor, newLanguage, newTitle)
        cursor = cursor.execute(sql, bindData)
        conn.commit()
        respone = jsonify('Employee added successfully!')
        respone.status_code = 200
        return respone
        # return f"Book with id: {cursor.lastrowwid} created sucessfully"
        
@app.route('/books/<int:id>', methods=['GET','PUT','DELETE'])
def singleBook(id):
    conn = dbConnection()
    cursor = conn.cursor()
    book = None
    if request.method == 'GET':
        cursor.execute("SELECT * FROM books where id=%s",(id,))
        rows = cursor.fetchall()
        for r in rows:
            book = r
        if book is not None:
            return jsonify(book),200
        else:
            return "Something Wrong", 404 
        # for book in bookList:
        #     if book['id']==id:
        #         return jsonify(book)
    
    if request.method == 'PUT':
        
        sql = """UPDATE books SET 
        author = %s,
        language = %s,
        title = %s
        WHERE id = %s"""
        # for book in bookList:
        #     if book['id']==id:
        # json = request.json
        author = request.form['author']
        language = request.form['language']
        title = request.form['title']
        # id = request.form['id']
        # updatedBook = {
        #     'title': title,
        #     'author': author,
        #     'language': language,
        #     'id': id,
        # }
        dataBind = (author, language, title, id)
        cursor.execute(sql, dataBind)
        conn.commit()
        return ('Book data updated')

    if request.method == 'DELETE':
        sql = """DELETE FROM books WHERE id=%s"""
        cursor.execute(sql,(id))
        conn.commit()
        return "data deleted"
        # for index, book in enumerate(bookList):
        #     if book['id'] == id:
        #         bookList.pop(index)
        #         return jsonify(bookList)




# if __name__ == '__main__':
#     app.run()
if __name__ == '__main__':
    app.debug = True
    app.run()
