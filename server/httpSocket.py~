import socket
from datetime import datetime
from logClass import Log
import sys

#----------------------------------------------------------------------------
# Classe que encapsula todo o tratamento de erro de um socket HTTP e todas as
# suas funcionalidades
#----------------------------------------------------------------------------

class HttpServerSocket:
    #construtor
    __BUFFER_SIZE = 8192
    
    def __init__(self, ip, port, logfilename):
        self.__ip   = ip
        self.__port = port
        self.__httpSocket = self.__openTCPSocketIPv4()
        self.__log = Log(logfilename)

    #------------------------------------------------------------------
    # METODOS PARA GET E SET
    #------------------------------------------------------------------

    #retorna ip e porta
    def getTCPAddress(self):
        return (self.__ip, self.__port)

    #escreve mensagem no log
    def writeLog(self,message):
        self.__log.writeLog(message)
    
    #------------------------------------------------------------------
    # METODOS PARA MANIPULAÇÃO DE SOCKETS
    #------------------------------------------------------------------
        
    # Abre socket TCP IPv4
    def __openTCPSocketIPv4(self):
        try:
            return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as msg:
            self.__log.writeLog('\tFalha ao criar socket')
            sys.exit()

    # Realiza binding no socket
    def makeBinding(self):
        try:
            self.__httpSocket.bind((self.__ip,self.__port))
        except socket.error as msg:
            self.__log.writeLog('\tFalha ao realizar binding em IP '+ self.__ip +' e porta '+ str(self.__port))
            sys.exit()

    # Realiza listen do socket
    def makeListen(self, elem):
        try:
            self.__httpSocket.listen(elem)
        except socket.error as msg:
            self.__log.writeLog('\tFalha ao realizar listening sobre o socket')
            sys.exit()

    # Realiza accept em socket
    def makeAccept(self):
        try:
            return self.__httpSocket.accept()
        except socket.error as msg:
            self.__log.writeLog('\tFalha ao aceitar cliente')
            sys.exit()

    # Envia mensagem de um socket
    def sendMessage(self,message):
        try:
            m = message.encode('ascii')
            self.__httpSocket.sendall(m)
        except socket.error as msg:
            self.__log.writeLog('\tFalha ao enviar mensagem, código:')
            sys.exit()

    # Envia mensagem de uma conexao com o servidor
    def sendConnMessage(self,conn,message):
        try:
            m = message.encode('ascii')
            conn.sendall(m)
        except socket.error as msg:
            self.__log.writeLog('\tFalha ao enviar mensagem')
            sys.exit()

    # Recebe mensagem de um socket
    def receiveMessage(self):
        try:
            data = self.__httpSocket.recv(HttpServerSocket.__BUFFER_SIZE)
            return data.decode()
        except socket.error as msg:
            self.__log.writeLog('\tFalha ao receber mensagem')
            sys.exit()

    # Recebe mensagem de uma conexao com o servidor
    def receiveConnMessage(self,conn):
        try:
            data = conn.recv(HttpServerSocket.__BUFFER_SIZE)
            return data.decode()
        except socket.error as msg:
            self.__log.writeLog('\tFalha ao receber mensagem')
            sys.exit()
