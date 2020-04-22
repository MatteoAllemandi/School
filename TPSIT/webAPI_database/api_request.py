import requests

URL_INSERT = "http://127.0.0.1:5000/insertBook"
URL_ALL = "http://127.0.0.1:5000/allBooks"
URL_BYID = "http://127.0.0.1:5000/bookById"

def ID_research(id):
    PARAMS = {'id':id}
    r = requests.get(url = URL_BYID, params = PARAMS)
    data = r.json()[PARAMS['id']]
    print(f"libro cercato --> {data}")

def allBooks():
    r=requests.get(url=URL_ALL)
    data = r.json()
    for i in data:
        print(i)

def insertBook(title,author,year):
    PARAMS = {'title':title,'author':author,'published':year}
    r = requests.get(url=URL_INSERT, params=PARAMS)
    print('dati inviati')
    if r :
        print(r)

#tuttiLibri()
#print("^^^^^^^^^^^^^^^^^^^")
#ricercaPerId(1)


def main():
    while True:
        case = int(input('1 --> Inserisci libro nel database\n2--> Cerca con ID libro\n3--> Stampa tutti i libri\n4 --> esci\n'))
        if case == 1 :
            title = input('Inserisci il nome del libro : ')
            author = input("Inserisci l'autore : ")
            year = int(input("inserisci anno di pubblicazione (es. 2001) : "))
            insertBook(title,author,year)
        if case == 2:
            id_search = int(input("inserisci id del libro da cercare: "))
            ID_research(id_search)
        if case == 3:
            allBooks()
        if case == 4:
            break

        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")


if __name__ == "__main__":
    main()
