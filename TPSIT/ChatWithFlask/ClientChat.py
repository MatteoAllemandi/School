import sqlite3
from threading import Thread
import flask
from flask import jsonify,request
from datetime import datetime
import threading
import requests
import time

class ClientThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.id = myId
        self.ip = ip

    def run(self):        
        while True:
            time.sleep(15)
            params = {'id_dest': self.id}
            URL = "http://" + self.ip + "/api/v1/receive"
            r = requests.get(url= URL, params = params)

            try:
                sqliteConnection = sqlite3.connect('clientDB.db')

                cursor = sqliteConnection.cursor()

                if len(r.json()) != 0:
                    for i in r.json():
                        cursor.execute(f"INSERT INTO receivedMessages (text,sender,received_at,alreadyRead) VALUES ('{i[1]}','{i[0]}','{i[3]}',{False})")
                        sqliteConnection.commit()

            except sqlite3.Error() as e:
                print('Error: ' + e)  
            finally:
                if (sqliteConnection):
                    sqliteConnection.close()               

def readMessages():
    try:
        sqliteConnection = sqlite3.connect('clientDB.db')
        cursor = sqliteConnection.cursor()

        cursor.execute(f"SELECT * FROM receivedMessages,rubrica where receivedMessages.sender = rubrica.id and rubrica.locked = 0 order by received_at;")
        msg = cursor.fetchall()

        for i in msg:
            cursor.execute(f"SELECT name,surname FROM rubrica where id = {i[2]}")
            name = cursor.fetchall()

            print(str(name[0][0]), str(name[0][1])  +  ": " + i[1] + " alle ore " + str(i[3] + "\n"))

    except sqlite3.Error as error:
        print("Error: " + error)

    finally:
        if (sqliteConnection):
            print('messaggi stampati')
            sqliteConnection.close()

    return

def sendMessage():
    id_dest = int(input("\nInserisci il numero di registro del destinatario"))
    text = input("\nInserisci testo del messaggio\n")

    params = {'id_dest' : id_dest,'text' : text, 'id_mitt' : myId}
    text = text.replace(" ", "+")
    URL = "http://" + ip + "/api/v1/send"   

    r = requests.get(url = URL, params=params)
    if r.status_code == 200:
        print("messaggio inviato")
    else:
        print("non sono riuscito ad inviare il messaggio")
    
    return 
    
def getAllUsers():
    URL = "http://" + ip + "/api/v1/user_list" 
    r = requests.get(url = URL)
    data = r.json()
    for i in data:
        print(i[0]," -- ", i[1], " -- ", i[2])

def lockUser():
    getAllUsers()
    nUser = int(input("inserisci numero di registro del contatto da bloccare: "))
    try:
        sqliteConnection = sqlite3.connect('clientDB.db')
        cursor = sqliteConnection.cursor()

        cursor.execute(f"UPDATE rubrica SET locked = 1 WHERE id = {nUser}")
        sqliteConnection.commit()

        cursor.execute(f"SELECT name,surname FROM rubrica where id = {nUser}")
        name = cursor.fetchall()

        print(f"utente bloccato: {name[0][0]} {name[0][1]}")

    except sqlite3.Error as error:
        print("Error: " + error)
    finally:
        if (sqliteConnection):
            print('chiusura connessione DB')
            sqliteConnection.close()

def unlockUser():
    getAllUsers()
    nUser = int(input("inserisci numero di registro del contatto da sbloccare: "))
    try:
        sqliteConnection = sqlite3.connect('clientDB.db')
        cursor = sqliteConnection.cursor()

        cursor.execute(f"UPDATE rubrica SET locked = 0 WHERE id = {nUser}")
        sqliteConnection.commit()

        cursor.execute(f"SELECT name,surname FROM rubrica where id = {nUser}")
        name = cursor.fetchall()

        print(f"utente sbloccato: {name[0][0]} {name[0][1]}")

    except sqlite3.Error as error:
        print("Error: " + error)
    finally:
        if (sqliteConnection):
            print('chiusura connessione DB')
            sqliteConnection.close()



def main(idReg, newThread):
    while True:
        sel = int(input("\n1: invia messaggio\n2: blocca utente\n3: sblocca utente\n4: stampa tutti gli utenti\n5: stampa messaggi\n6: Esci\n>>>>"))

        if sel == 1:
            getAllUsers()
            sendMessage()
        if sel == 2:
            lockUser()
        if sel == 3:
            unlockUser()
        if sel == 4:
            getAllUsers()
        if sel == 5:
            readMessages()
        if sel == 6:
            newThread.join()
            break
    return 


if __name__ == "__main__":
    myId = int(input("inserisci il tuo numero di registro: "))
    ip =  input("\nInserisci ip e porta del server (Es xxx.xxx.x.x : xxxx)\n")

    newThread = ClientThread()
    newThread.start()

    main(myId, newThread)
    

    
    