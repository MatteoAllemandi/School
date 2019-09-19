import socket as sck

main()

def only_server():
    HOST = input("insert host address: ")
    PORT = input("insert port number: ")

    PORT = int(PORT)

    STOP = "stop"

    s = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(1)
    conn, addr = s.accept()
    print("connected to " + str(addr))

    while 1:
        data = conn.recv(4096)
        print("received: --> " + str(data))

        if not data: break
        if data==STOP.encode() :
            break

        testo = input("inserisci stringa: ")
        conn.send(testo.encode())
    conn.close()
    print("closing server")

def only_client():
    HOST = input("insert host address: ")
    PORT = input("insert port number: ")

    PORT = int(PORT)

    s = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
    s.connect((HOST,PORT))

    while 1:

        text = input("insert text:  ")
        s.send(text.encode())

        if(text=="stop"):
            break

        data = s.recv(4096)
        print("received -->" + str(data))

    s.close()
    print("closing client")

def actor():
    IP_SERVER = print("insert next host address: ")
    PORT_SERVER = print("insert port number: ")

    PORT_SERVER = int(PORT_SERVER)

    IP_CLIENT = print("insert your IP address: ")
    PORT_CLIENT = print("insert port number: ")

    PORT_CLIENT = int(PORT_CLIENT)

    STOP = "stop"

    socket_server = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
    socket_client = sck.socket(sck.AF_INET,sck.SOCK_STREAM)

    socket_server.bind((IP_SERVER,PORT_SERVER))

    socket_client.connect((IP_CLIENT,PORT_CLIENT))


    socket_server.listen()

    conn, addr = socket_server.accept()
    print("connected to " + str(addr))


    while True:
        data = conn.recv(4096)
        print("received: --> " + str(data))

        if data==STOP.encode() :
            break

        socket_client.send(data)

    socket_client.close()
    socket_server.close()
    print("closing actor")

def main():
    while True:
        function = input("insert--a-- for actor, --s-- for server only, --c-- for client only")

        if function == "a" or function == "A":
            actor()
            break
        elif function == "s" or function == "S":
            only_server()
            break
        elif function == "c" or function == "C":
            only_client()
            break
        else:
            print("value error, please try again")
    print("end of trasmission")

