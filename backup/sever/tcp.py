import socket
import urllib2

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 30

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()

while 1:

    data = conn.recv(BUFFER_SIZE)
    
    if not data:
        break

    else:
        print("received data:", data)
        response = urllib2.urlopen(data)
        html = response.read()

        conn.send(html)

conn.close()