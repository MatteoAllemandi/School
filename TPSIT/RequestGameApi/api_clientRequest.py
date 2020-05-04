import requests
import sqlite3
from flask import jsonify
import shutil
#most popular

URL = "https://api.rawg.io/api/games?dates=2019-01-01,2019-12-31&ordering=-added"   #page url

def getJson():                      
    r = requests.get(url= URL)          #get the json data from the website with an http request using get method
    print(r)
    return(r.json())

def downloadImage(id):
    try :
        sqliteConnection = sqlite3.connect('gamesDB.db')            #connect to database
        cursor = sqliteConnection.cursor()

        cursor.execute(f"SELECT background_image,nome FROM mostPopular WHERE idCampo = {id}")       #get name and link from the db for background img download
        fetch = cursor.fetchall()
        img_link = fetch[0][0]  #split data in name and link
        name = fetch[0][1]
        
    except sqlite3.Error as error:
        print("eccezione --> " + error)

    finally:
        if (sqliteConnection):
            print('chiusura connessione con database')
            sqliteConnection.close()

    filename = f"{name}.jpeg"                #format the name with underscore
    filename = filename.replace(" ", "-")
    filename = filename.replace(":", "-")

    r = requests.get(url = img_link, stream = True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(filename,'wb') as f:      #save the image in a new file 
            shutil.copyfileobj(r.raw, f)
        f.close()
    else:
        print("immagine non scaricata") #if the request doesn't work, print an error

def writeOnDB(data):
    try:
        sqliteConnection = sqlite3.connect('gamesDB.db')
        cursor = sqliteConnection.cursor()              #connect to db 

        cursor.execute("DELETE FROM mostPopular;")
        
        for i in range(len(data['results'])):               #save json data in single variables and then load on the db
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
            background_image = (data['results'][i]['background_image'])

            cursor.execute(f"INSERT INTO mostPopular (nome,dataRilascio,rating,rating_top,ratings_count,reviews_text_count,added,suggestions_count,id,reviews_count,slug,background_image) VALUES ('{name}',{released},{rating},{rating_top},{ratings_count},{reviews_text_count},{added},{suggestions_count},{id},{reviews_count},'{slug}','{background_image}');")

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

        cursor.execute("SELECT nome,dataRilascio,rating FROM mostPopular")         #get data from the most popular games in the db 
        ranking = cursor.fetchall()

    except sqlite3.Error as error:
        print("eccezione --> " + error)

    finally:
        if (sqliteConnection):
            print('Lettura eseguita: chiusura connessione con database\n')
            sqliteConnection.close()
    
    return ranking


def main():

    while True:
        selection = int(input("1 -> carica DB\n2->ottieni classifica\n3->ottieni immagine con id\n4->Esci\n>>>"))

        if selection == 1:
            writeOnDB(getJson())
        if selection == 2:
            ranking = GetDataFromDB() 
            for i,val in enumerate(ranking):
                print(f"{i+1} posto --> nome: {val[0]}, rilasciato nel {val[1]}, rating: {val[2]}\n")
        if selection == 3:
            downloadImage(int(input("\n\ninserisci id del gioco da cercare: ")))
        if selection == 4:
            break


main()

