import pymysql
# from dbconfig import MySql
# from app import app
from flask import Flask, jsonify, request

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

# CRUD Operation - CREATE 
@app.route('/add', methods=['POST'])
def add_book():
	try:
		json = request.json
		title = json['title']
		Author_name = json['author_name']
		language = json['language']
		if title and Author_name and language and request.method == 'POST':
			SQL_Query = "INSERT INTO books(title, Author_name, language) VALUES(%s, %s, %s)"
			data = (title, Author_name, language)
			connection = dbConnection()
			Pointer = connection.cursor()
			Pointer.execute(SQL_Query, data)
			connection.commit()
			response = jsonify('Book added!')
			response.status_code = 200
			return response
		else:
			return "Not able to add data"
	except Exception as e:
		print(e)
	finally:
		Pointer.close() 
		connection.close()
		
#CRUD Operation - READ			
