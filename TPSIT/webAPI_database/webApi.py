import flask
import sqlite3
from flask import request
from flask import jsonify

app = flask.Flask(__name__)
app.config["debug"] = True

@app.route('/',methods=["GET"])
def home():
   return "<h1>Biblioteca online con database</h1>"

@app.route('/allBooks', methods=["GET"])
def getAllBooks():
    try:
        sqliteConnection = sqlite3.connect('LibriDB.db')
        cursor = sqliteConnection.cursor()

        cursor.execute("SELECT * FROM libri")
        allBooks = cursor.fetchall()

        print("eseguito")
        sqliteConnection.commit()

    except sqlite3.Error as error:
        print("eccezione --> " + error)

    finally:
        if (sqliteConnection):
            print('chiusura connessione con database')
            sqliteConnection.close()
    return jsonify(allBooks)
   
@app.route('/bookById', methods=["GET"])
def searchById():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: no id field provided. Please specify an id"

    try:
        sqliteConnection = sqlite3.connect('LibriDB.db')
        cursor = sqliteConnection.cursor()

        cursor.execute(f"SELECT * FROM libri where id=={id}")
        book = cursor.fetchall()

        print("eseguito")
        sqliteConnection.commit()

    except sqlite3.Error as error:
        print("eccezione --> " + error)

    finally:
        if (sqliteConnection):
            print('chiusura connessione con database')
            sqliteConnection.close()
    return jsonify(book)

@app.route('/insertBook',methods=["GET"])
def insertBook():
    if 'title' in request.args and 'author' in request.args and 'published' in request.args:
        newTitle = request.args['title']
        newAuthor = request.args['author']
        newYear = int(request.args['published'])
    else:
        return 'error: some field missing for book registration'

    print(f'{newTitle},{newAuthor},{newYear}')
    
    try:
        sqliteConnection = sqlite3.connect('LibriDB.db')
        cursor = sqliteConnection.cursor()

        cursor.execute(f"INSERT INTO libri (title,author,published) VALUES ('{newTitle}','{newAuthor}',{newYear});")
        sqliteConnection.commit()
        print('inserimento eseguito')
    except sqlite3.Error as error:
        print(f'Errore inserimento-->, {error}')
    finally:
        if (sqliteConnection):
            print('chiusura connessione con database')
            sqliteConnection.close()
    return 'Funzione Finita'

app.run()
