import socket
from datetime import datetime
from logClass import Log
import sys

class HttpServerResponse:
    __saltoLinha = '\r\n'
    __bufferSize = 8192
    
    #------------------------------------------------------------------
    # inicia a classe para o servidor para a resposta de uma requisicao
    #------------------------------------------------------------------
    def __init__(self, ip, port, logfilename = 'logserver.txt'):
        self.__ip = ip
        self.__port = port
        self.__log = Log(logfilename)

    #------------------------------------------------------------------
    # METODO PARA RECEBIMENTO DE REQUISICOES GET
    #------------------------------------------------------------------
    
    # lanca o servidor para receber requisicoes GET
    # recebe apenas uma unica requisicao por vez
    def launchGETServer(self):
        #cria socket e 'liga' porta e ip ao socket
        print("Server:: Criando socket...")
        self.__log.writeLog("Server:: Criando socket...")
        s = self.__openTCPSocketIPv4()

        print("Server:: Ligando socket servidor pelo ip e porta...")
        self.__log.writeLog("Server:: Ligando socket servidor pelo ip e porta...")
        self.__makeBinding(s)

        #escuta requisicoes
        print("Server:: Aguardando requisicoes...")
        self.__log.writeLog("Server:: Aguardando requisicoes...")
        self.__makeListen(s,1)

        while(True):
            #aceita primeira conexao de um cliente
            (conn, addr) = self.__makeAccept(s)
            print("Server:: Obteve conexao de "+addr[0]+"\n")
            self.__log.writeLog("Server:: Obteve conexao de "+addr[0]+"\n")
            
            request = self.__receiveMessage(conn)

            #reinicia o loop se servidor se nao receber requisicao
            if(not request):
                continue
            
            print("Server:: Obteve mensagem de "+addr[0]+"\n"+ request + "\n")
            self.__log.writeLog("Server:: Obteve mensagem de "+addr[0]+"\n"+ request + "\n")

            #parse do get, obtendo host e urlRelativa
            (host,urlRelative) = self.__parseGETRequest(request)
            print(host + ' ' + urlRelative)
            
            #gera resposta
            response = self.__createResponse(host,urlRelative)
            
            #envia resposta via socket
            print("Server:: Enviando mensagem para "+addr[0]+"\n")
            self.__log.writeLog("Server:: Enviando mensagem para "+addr[0]+"\n"+response+"\n")
            self.__sendMessage(conn,response)
        
        #fecha conexao
        conn.close()

    #------------------------------------------------------------------
    # METODOS PARA MANIPULACAO DE SOCKETS
    #------------------------------------------------------------------
        
    # Abre socket TCP IPv4
    def __openTCPSocketIPv4(self):
        try:
            return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as msg:
            self.__log.writeLog('\tFalha ao criar socket, codigo: ' + str(msg[0]) + ' ' + msg[1])
            sys.exit()

    # Realiza binding no socket
    def __makeBinding(self, s):
        try:
            s.bind((self.__ip,self.__port))
        except socket.error as msg:
            self.__log.writeLog('\tFalha ao realizar binding em IP '+ self.__ip +' e porta '+ str(self.__port) +', codigo: ' + str(msg[0]) + ' ' + msg[1])
            sys.exit()

    # Realiza listen do socket
    def __makeListen(self, s, elem):
        try:
            s.listen(elem)
        except socket.error as msg:
            self.__log.writeLog('\tFalha ao realizar listening sobre o socket, codigo: ' + str(msg[0]) + ' ' + msg[1])
            sys.exit()

    # Realiza accept em socket
    def __makeAccept(self, s):
        try:
            return s.accept()
        except socket.error as msg:
            self.__log.writeLog('\tFalha ao aceitar cliente , codigo: ' + str(msg[0]) + ' ' + msg[1])
            sys.exit()

    # Envia mensagem de um socket
    def __sendMessage(self,s,message):
        try:
            s.sendall(message.encode('ascii'))
        except socket.error as msg:
            self.__log.writeLog('\tFalha ao enviar mensagem, codigo: ' + str(msg[0]) + ' ' + msg[1])
            sys.exit()

    # Recebe mensagem de um socket
    def __receiveMessage(self,s):
        try:
            data = s.recv(HttpServerResponse.__bufferSize)
            return data.decode()
        except socket.error as msg:
            self.__log.writeLog('\tFalha ao receber mensagem, codigo: ' + str(msg[0]) + ' ' + msg[1])
            sys.exit()

    #------------------------------------------------------------------
    # PARSER PARA REQUISICAO GET
    #------------------------------------------------------------------
    
    def __parseGETRequest(self,dados):
        strings = dados.split(HttpServerResponse.__saltoLinha)
        return (self.__parseHostLine(strings[1]),
                self.__parseGETLine(strings[0]))
        

    def __parseGETLine(self,getLine):
        try:
            i = getLine.index('/')      #pega posicao onde inicia a barra (inicio url relativo)
            j = getLine.index(' HTTP')  #pega posicao do fim do endereco relativo
            return getLine[i : j]
        except ValueError:
            self.__log.writeLog('Falha no parser do GET')
            sys.exit()

    def __parseHostLine(self,hostLine):
        try:
            i = hostLine.index(':')
            return hostLine[i+2:]
        except ValueError:
            self.__log.writeLog('Falha no parser do HOST')
            sys.exit()

    #------------------------------------------------------------------
    # CRIACAO DE MENSAGEM GET
    #------------------------------------------------------------------
    
    def __createResponse(self,host,urlRelative):
        code = "200"
        descriptionCode = "OK"
        try:
            html = self.__getHTMLText(urlRelative)
        except FileNotFoundError:
            html = self.__get404Page()
            code = "404"
            descriptionCode = "Not Found"
        
        strings = []
        strings.append("HTTP/1.0 {0} {1}".format(code, descriptionCode))
        strings.append(self.__strDateFormat())
        strings.append("Content-Length: {0}".format(len(html)))
        strings.append("Content-Type: text/html; charset=UTF-8")
        strings.append("\r\n")
        strings.append(html)

        return HttpServerResponse.__saltoLinha.join(strings)
       
    # Retorna a pagina de erro 404
    def __get404Page(self):
        strings = []
        strings.append('<!DOCTYPE html>')
        strings.append('<html>')
        strings.append('<head>')
        strings.append('<title>ERRO 404</title>')
        strings.append('<style>')
        strings.append('\tdiv#conteudo {')
        strings.append('\t\tbackground-color: #ccc;')
        strings.append('\t\tmargin: 0px auto;')
        strings.append('\t\twidth:860px;')
        strings.append('\t\tpadding:10px;')
        strings.append('\t}')
        strings.append('</style>')
        strings.append('</head>')
        strings.append('<body>')
        strings.append('\t<div id="conteudo">')
        strings.append('\t\t<h1>Erro no servidor 404</h1>')
        strings.append('\t\t<p>Pagina requisitada nao foi encontrada</p>')
        strings.append('\t</div>')
        strings.append('</body>')
        strings.append('</html>')

        return HttpServerResponse.__saltoLinha.join(strings)
  
    # Recupera pagina URL do servidor. As paginas devem estar na pasta www
    def __getHTMLText(self,urlRelative):
        #adiciona o diretorio geral WWW
        urlRelative = 'www' + urlRelative

        #verifica se o final eh um diretorio
        n = len(urlRelative)
        if(urlRelative[n-1] == '/'):
            urlRelative = urlRelative + 'index.html'

        with open(urlRelative,'r') as f:
            return f.read()

    #------------------------------------------------    
    # Retorna formato string para data usado na resposta GET
    # Se nao passar nenhum argumento, formato da data atual em GMT (UTC)
    # Exemplo: 'Date: Fri, 17 Apr 2015 02:06:10 GMT'
    #------------------------------------------------

    def __strDateFormat(self,date = datetime.utcnow()):
        strWeekDay = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        strMonth   = ["NOT", "Jan", "Feb", "Mar", "Apr", "May", "Jun",
                      "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        time    = datetime.utctimetuple(date)
        
        weekday = strWeekDay[time.tm_wday]
        day     = self.__strTwoDigitNumber(time.tm_mday)
        month   = strMonth[time.tm_mon]
        year    = time.tm_year
        hour    = self.__strTwoDigitNumber(time.tm_hour)
        minute  = self.__strTwoDigitNumber(time.tm_min)
        second  = self.__strTwoDigitNumber(time.tm_sec)
        
        return "Date: {0}, {1} {2} {3} {4}:{5}:{6} GMT".format(weekday,day,month,year,
                                                               hour,minute,second)
    #------------------------------------------------    
    # insere numero zero se numero for menor que 10
    # ex: 1 => 01
    #------------------------------------------------
    def __strTwoDigitNumber(self,n):
        if(n < 10):
            return '0{0}'.format(n)
        
        return '{0}'.format(n)
