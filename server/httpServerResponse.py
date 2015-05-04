from datetime import datetime
from httpSocket import HttpServerSocket
from getMethodHandle import GETMethodHandle
import sys

class HttpServerResponse:
    
    #------------------------------------------------------------------
    # inicia a classe para o servidor para a resposta de uma requisicao
    #------------------------------------------------------------------
    def __init__(self, ip, port, logfilename = 'logserver.txt'):
        #cria socket
        print('Server:: Criando socket...')
        self.__httpSocket = HttpServerSocket(ip,port,logfilename)
        self.__getHandle  = GETMethodHandle(logfilename)
        self.__httpSocket.writeLog('Server:: Criando socket...')
    #------------------------------------------------------------------
    # METODO PARA RECEBIMENTO DE REQUISICOES GET
    #------------------------------------------------------------------
    
    # lança o servidor para receber requisicoes GET
    # recebe apenas uma unica requisicao por vez
    def launchGETServer(self):
        s = self.__httpSocket
        
        print("Server:: Ligando socket servidor pelo ip e porta...")
        s.writeLog("Server:: Ligando socket servidor pelo ip e porta...")
        s.makeBinding()

        #escuta requisicoes
        print("Server:: Aguardando requisicoes...")
        s.writeLog("Server:: Aguardando requisicoes...")
        s.makeListen(1)

        while(True):
            #aceita primeira conexao de um cliente
            (conn, addr) = s.makeAccept()
            print("Server:: Obteve conexao de "+addr[0]+"\n")
            s.writeLog("Server:: Obteve conexao de "+addr[0]+"\n")
            
            request = s.receiveConnMessage(conn)

            #reinicia o loop se servidor se nao receber requisicao
            if(not request):
                continue
            
            print("Server:: Obteve mensagem de "+addr[0]+"\n"+ request + "\n")
            s.writeLog("Server:: Obteve mensagem de "+addr[0]+"\n"+ request + "\n")

            #parse do get, obtendo host e urlRelativa
            (host,urlRelative) = self.__getHandle.parseGETRequest(request)
            print(host + ' ' + urlRelative)
            
            #gera resposta
            response = self.__getHandle.createResponse(host,urlRelative)
            
            #envia resposta via socket
            print("Server:: Enviando mensagem para "+addr[0]+"\n")
            s.writeLog("Server:: Enviando mensagem para "+addr[0]+"\n"+response+"\n")
            s.sendConnMessage(conn,response)
        
        #fecha conexao
        conn.close()
