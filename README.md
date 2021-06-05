# Guide to Socket Programming Introduction

## Socket programming is started by socket library

```
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
```

+ AF_INET refers to address family ipv4
+ SOCK_STREAM meaning TCP protocol

*****************

## SERVER code
+ s = socket.socket()
   + It simply creates a new socket using the given address family,socket type and protocol number.
+ port = 12345
   + Reserves a port for computer
+ s.bind('',port)
  + We binded our server to the specified port. Passing an empty string means that the server can listen to incoming connections from other computers as well. If we would have passed 127.0.0.1 then it would have listened to only those calls made within the local computer.
+ s.listen(5)
   + Server can connect to 5 clients, 6th or more clients are rejected.
+ s.accept()
   + Return new socket object c and address
+ s.close()
  + Marks the socket closed, all future operaions on socket will be failed.

 #### OverView
  ```
 #import library
 import socket

 s=socket.socket()
 port=12345
 s.bind('',port)
 s.listen(5)

 while True:
   c,addr = s.accept()
   data = c.recv(1024)
   c.sendall(data)
 c.close()
```
Server uses `bind() , listen() , accept()`
*************
## Client Code

+ First create socket object
+ Give port number same as server
+ connect() '127.0.0.1' local machine connection
+ print s.recv(1024) #print data recv from socket
+ close() connection
```
 import socket
 s=socketsocket()
 port=12345
 s.connect('127.0.0.1',port)
 print s.recv(1024)
 s.close()
```

<img src = 'https://raw.githubusercontent.com/InternityFoundation/Socket-Programming-Python/master/1.%20String%20Reverse%20(Client-Server)%20Python/ReverseString.PNG' height = "430px" width = "630px"/>

 ## Reference Link
 + [Explaination and sample program geeksforgeeks](http://www.geeksforgeeks.org/socket-programming-python/)
 + [Sample Program python socket programming](http://www.bogotobogo.com/python/python_network_programming_server_client.php)

 ****************
 ## CRC Socket PROGRAMMING
 [Article Link](https://www.geeksforgeeks.org/cyclic-redundancy-check-python/)


***************************
# SOCKET PROGRAMMING WITH MULTI-THREADING
### Checkout Article [Socket Programming Multi-Threading At Geeksforgeeks](http://www.geeksforgeeks.org/socket-programming-multi-threading-python/)

## Socket Programming->
It helps us to connect a client to a server. Client is message sender and receiver and server is just a listener that works on data sent by client.

## What is a Thread?
A thread is a light-weight process that does not require much memory overhead, they are cheaper than processes.

## What is Multi-threading Socket Programming?
Multithreading is a process of executing multiple threads simultaneously in a single process.

## Multi-threading Modules : 
A *_thread module & threading module* is used for multi-threading in python, these modules help in synchronization and provide a lock to a thread in use.

Console Window:
Received from the server : skeegrofskeeg syas ayruahs

Do you want to continue(y/n) :y
Received from the server : skeegrofskeeg syas ayruahs

Do you want to continue(y/n) :n

Process finished with exit code 0
