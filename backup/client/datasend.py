# -*- coding: utf-8 -*-

import socket
import sys

def http_request(url, port):

    #remote_ip = socket.gethostbyname(url)

    try:
        remote_ip = socket.gethostbyname(url)

    except socket.gaierror:
        print('Não foi possível encontar o servidor')
        sys.exit()


    print("Host " + url + " encontrado o ip é " + remote_ip)

    s = open_tcp_socket_ipv4(remote_ip, port)

    print("Conectando ao servidor...")
    s.connect((remote_ip, port))

    message = "\n\nGET / HTTP/1.0\r\n\r\n"

    try:
        print("Enviando menssagem... " + message)
        s.sendall(message)
        print("Menssagem enviada com sucesso!")
    
    except socket.error:
        print('Send fail')
        sys.exit()

    print("Aquardando resposta \r\n\r\n")

    reply = s.recv(4096)

    print reply

def open_tcp_socket_ipv4(server_ip, port):

    print("Espere...")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error, msg:
        print("Falha ao criar socket, código: " + str(msg[0]) + " " + msg[1])
        sys.exit()

    print("Socket criado com sucesso!")

    return s

if sys.argv[1] != None and sys.argv[2] != None:
    http_request(sys.argv[1], int(sys.argv[2]))
elif sys.argv[0] != None:
    http_request('www.google.com.br', 80)
    