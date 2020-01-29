import socket
from threading import Thread

BUFFSIZE = 4096
SERVER_IP = '192.168.0.104'
SERVER_PORT = 1234

close = False
shutdown = False

threadList = [] 
connectionList = []

class ClientThread(Thread):
    def __init__(self,client_ip,client_port,conn):
        Thread.__init__(self)
        self.client_ip = client_ip
        self.client_port = client_port
        self.conn = conn
        print(f"new thread started for {client_ip},{client_port}")

    def run(self):
        global close
        while True:
            data = self.conn.recv(BUFFSIZE)
            print(f"received data from {self.client_ip},{self.client_port}---> {data.decode()}")
            if data.decode() == "stop" or data.decode() == "STOP":
                conn.close()
                close = True
                break
        
        print(f"connessione chiusa da {self.client_ip},{self.client_port}")
        print(close)

class Controller(Thread):
    def __init__(self):
        Thread.__init__(self)
        print("control thread to close connection ready ")

    def run(self):
        global close
        global shutdown
        while True:
            if close :
                print(f"closing all the threads")
                for i in threadList:
                    i.join()

                for i in connectionList:
                    i.close()

                shutdown = True
                threadList.clear()
                break

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((SERVER_IP,SERVER_PORT))
s.listen(5)

print("multithread python server waiting for connection")

controller = Controller()
controller.start()

while True:
    if shutdown == True and len(threadList) == 0:
        break

    print("IM HERE")
    (conn,(ip,port)) = s.accept()
    connectionList.append(conn)
    newThread = ClientThread(ip,port,conn)
    newThread.start()
    threadList.append(newThread)

controller.join()
print("chiusura server")
s.close()