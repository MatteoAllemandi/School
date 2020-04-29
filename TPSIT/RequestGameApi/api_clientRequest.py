import requests
import sqlite3
from flask import jsonify
#most popular

URL = "https://api.rawg.io/api/games?dates=2019-01-01,2019-12-31&ordering=-added"

def getJson():
    r = requests.get(url= URL)
    print(r)
    return(r.json())
    #print(type(data))

def writeOnDB(data):

    try:
        sqliteConnection = sqlite3.connect('gamesDB.db')
        cursor = sqliteConnection.cursor()
        
        for i in range(len(data['results'])):
            slug = (data['results'][i]['slug'])
            name = (data['results'][i]['name'])
            released = (data['results'][i]['released'])
            rating = (data['results'][i]['rating'])
            rating_top = (data['results'][i]['rating_top'])
            ratings_count = (data['results'][i]['ratings_count'])
            reviews_text_count = (data['results'][i]['reviews_text_count'])
            added = (data['results'][i]['added'])
            suggestions_count = (data['results'][i]['suggestions_count'])
            id = (data['results'][i]['id'])
            reviews_count = (data['results'][i]['reviews_count'])

            cursor.execute(f"INSERT INTO mostPopular (nome,dataRilascio,rating,rating_top,ratings_count,reviews_text_count,added,suggestions_count,id,reviews_count,slug) VALUES ('{name}',{released},{rating},{rating_top},{ratings_count},{reviews_text_count},{added},{suggestions_count},{id},{reviews_count},'{slug}');")

        sqliteConnection.commit()

    except sqlite3.Error as error:
        print("eccezione --> " + error)

    finally:
        if (sqliteConnection):
            print('chiusura connessione con database')
            sqliteConnection.close()

def GetDataFromDB():
    try:
        sqliteConnection = sqlite3.connect('gamesDB.db')
        cursor = sqliteConnection.cursor()

        cursor.execute("SELECT nome,dataRilascio,rating FROM mostPopular")
        ranking = cursor.fetchall()

    except sqlite3.Error as error:
        print("eccezione --> " + error)

    finally:
        if (sqliteConnection):
            print('Lettura eseguita: chiusura connessione con database\n')
            sqliteConnection.close()
    
    return ranking

def alreadyLoaded():
    try:
        sqliteConnection = sqlite3.connect('gamesDB.db')
        cursor = sqliteConnection.cursor()

        cursor.execute("SELECT * FROM mostPopular")
        values = cursor.fetchall()

        if values[0] != None:
            loaded = True
        else:
            loaded = False

    except sqlite3.Error as error:
        print("eccezione --> " + error)

    finally:
        if (sqliteConnection):
            print("DATABASE CARICATO \n")
            sqliteConnection.close()

    return loaded

def main():
    if not alreadyLoaded():
        writeOnDB(getJson())
    
    ranking = GetDataFromDB() 
    for i,val in enumerate(ranking):
        print(f"{i+1} posto --> nome: {val[0]}, rilasciato nel {val[1]}, rating: {val[2]}\n")


main()

