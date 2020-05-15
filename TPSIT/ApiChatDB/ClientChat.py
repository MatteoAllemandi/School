import sqlite3
from threading import Thread
import flask
from flask import jsonify,request
from datetime import datetime
import threading
import requests
import time

class ClientThread(Thread):
    def __init__(self, myId, ip):
        Thread.__init__(self)
        self.id = myId
        self.ip = ip

    def run(self):        
        while True:
            time.sleep(5)
            params = {'id_dest': self.id}
            URL = "http://" + self.ip + "/api/v1/receive"
            r = requests.get(url= URL, params = params)
            if r.status_code == 200:
                try:
                    sqliteConnection = sqlite3.connect('clientDB.db')
                    cursor = sqliteConnection.cursor()

                    if len(r.json()) != 0:
                        for i in r.json():
                            cursor.execute(f"INSERT INTO receivedMessages (text,sender,received_at,alreadyRead) VALUES ('{i[1]}',{i[2]},'{i[3]}',{False})")
                            sqliteConnection.commit()

                except sqlite3.Error() as e:
                    print('Error: ' + e)  
                finally:
                    if (sqliteConnection):
                        sqliteConnection.close()
            else:
                print('status code error')           
                    

def readMessages(myId):
    try:
        sqliteConnection = sqlite3.connect('clientDB.db')
        cursor = sqliteConnection.cursor()

        msg = cursor.execute(f"SELECT * FROM receivedMessages WHERE locked=0;")

        cursor.execute("UPDATE receivedMessages SET alreadyRead = True WHERE locked = 0;")
        sqliteConnection.commit()

        for i in msg:
            print("Nuovo messaggio ricevuto da " + str(i[2]) +  ": " + i[1] + " alle ore " + str(i[3] + "\n"))

    except sqlite3.Error as error:
        print("Error: " + error)

    finally:
        if (sqliteConnection):
            print('chiusura connessione DB')
            sqliteConnection.close()

    return

def sendMessage(id_dest, text, myId, ip):
    params = {'id_dest' : id_dest,'text' : text, 'id_mitt' : myId}
    text = text.replace(" ", "+")
    URL = "http://" + ip + "/api/v1/send"   

    r = requests.get(url = URL, params=params)
    if r.status_code == 200:
        print("messaggio inviato")
    else:
        print("non sono riuscito ad inviare")
    
    return 
    
def getAllUsers(ip):
    URL = "http://" + ip + "/api/v1/user_list" 
    r = requests.get(url = URL)
    data = r.json()
    for i in data:
        print(i)



def main(idReg, ip):
    while True:
        sel = int(input("\n1: invia messaggio\n2: blocca utente\n3: sblocca utente\n4: stampa tutti gli utenti\n5: stampa messaggi\n6: Esci\n>>>>"))

        if sel == 1:
            id_dest = int(input("\nInserisci il numero di registro del destinatario"))
            text = input("\nInserisci testo del messaggio\n")
            sendMessage(id_dest,text,myId,ip)

        if sel == 2:
            pass
        if sel == 3:
            pass
        if sel == 4:
            getAllUsers(ip)

        if sel == 5:
            readMessages(myId)
        if sel == 6:
            break
    return 


if __name__ == "__main__":
    myId = int(input("inserisci il tuo numero di registro: "))
    ip =  input("\nInserisci ip e porta del server (Es xxx.xxx.x.x : xxxx)\n")
    newThread = ClientThread(myId, ip)
    newThread.start()

    main(myId, ip)

    newThread.join()
    