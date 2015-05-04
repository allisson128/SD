import socket
import sys

from urlParse import URLParse
from urlParse import URLException
from logClass import Log

#------------------------------------------------------
# CLASSE CRIADA PARA ATENDER REQUISICOES VIA URL
# UTILIZANDO METODOS HTTP (COMO GET OU POST)
#
# ESTA ABORDAGEM UTILIZA SOCKETS ENVIANDO DADOS VIA TCP
#------------------------------------------------------

class HttpClientRequest:
    #--------------------------------------------------
    # ATRIBUTOS ESTATICOS
    #--------------------------------------------------

    __saltoLinha = '\r\n\r\n'
    __bufferSize = 4096

    #--------------------------------------------------
    # ATRIBUTOS ESTATICOS
    #--------------------------------------------------
    def __init__(self, logfilename = 'logclient.txt'):
        self.__log = Log(logfilename)
    
    #--------------------------------------------------
    # METODOS 
    #--------------------------------------------------

    #obtem html a partir de uma resposta get
    def htmlFromGETResponse(self,getResponse):
        try:
            i = getResponse.index('<')
            return getResponse[i:]
        except ValueError:
            return 'nemhum HTML'
    
    #Realiza o metodo GET do HTTP
    def doGetRequest(self,url):
        self.__log.writeLog('Iniciando requisição GET para URL \"' + url + '\"...')
        #captura URL
        self.__log.writeLog('Parsing URL...')
        urlParse  = self.__getURLParsed(url)

        #captura IP remoto e porta
        self.__log.writeLog('Obtendo Host IP e numero da porta para conexao...')
        socketInfo = self.__getIPPortHost(urlParse)
        
        self.__log.writeLog('\t::IP para host \"' + urlParse.getHost() + '\" = ' + socketInfo[0] + '!')
        self.__log.writeLog('\t::Porta da conexao = ' + str(socketInfo[1]) + '!')
        
        #obtendo socket
        self.__log.writeLog('Criando socket TCP...')
        s = self.__openTCPSocketIPv4()
        self.__log.writeLog('\t::Socket criado com sucesso!')

        #iniciando conexao
        self.__log.writeLog('Iniciando conexao...')
        self.__beginSocketConnection(s, socketInfo)
        self.__log.writeLog('\t::Conexao iniciada em IP \"'+socketInfo[0]+'\" e Porta \"'+str(socketInfo[1])+'\"!')

        #montando mensagem GET
        self.__log.writeLog('Montando mensagem GET...')
        getMessage = self.__createGETMessageRequest(urlParse)
        self.__log.writeLog('\t::MENSAGEM GET\n****\n'+getMessage+'\n****')
        
        #enviando mensagem via socket
        self.__log.writeLog('Enviando mensagem via socket...')
        self.__sendingGETMessage(s,getMessage)
        self.__log.writeLog('\t::Mensagem enviada com sucesso!')

        #recebendo mensagem do servidor
        self.__log.writeLog('Recebendo mensagem do servidor...')
        receivedMessage = self.__receivingGETMessage(s)
        self.__log.writeLog('\t::Mensagem recebida com sucesso de Host \"'+socketInfo[0]+'\" Porta \"'+str(socketInfo[1])+'\"!')
        self.__log.writeLog('\t::MENSAGEM RECEBIDA\n\n****\n'+receivedMessage+'\n****')
        
        return receivedMessage


    #--------------------------------------------------
    # METODOS PRIVADOS
    # utilizados no processo de parser
    #--------------------------------------------------

    #Recupera URL atraves da string url recebida do usuario
    def __getURLParsed(self,url):
        try:
            return URLParse(url)
        except URLException as e:
            self.__log.writeLog('\tErro: ' + e)
            sys.exit()
    
    #Recebe IP e porta atraves de um endereco host
    def __getIPPortHost(self,urlParse):
        try:
            return (socket.gethostbyname(urlParse.getHost()), urlParse.getPorta())
        except socket.gaierror:
            self.__log.writeLog('\tErro:: Não foi possível encontrar o servidor')
            sys.exit()
    
    #Abre socket TCP IPv4 
    def __openTCPSocketIPv4(self):
        try:
            return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as msg:
            self.__log.writeLog('\tFalha ao criar socket, código: ' + str(msg[0]) + ' ' + msg[1])
            sys.exit()

    #Inicia conexao
    def __beginSocketConnection(self,s,socketInfo,timeout = 30):
        s.settimeout(timeout)
        try:
            s.connect(socketInfo)
        except socket.error as msg:
            self.__log.writeLog('\tFalha ao criar socket, código: ' + str(msg[0]) + ' ' + msg[1])
            sys.exit()

    #monta mensagem GET
    def __createGETMessageRequest(self,urlParse):
        get  = 'GET /{0} HTTP/1.0'.format(urlParse.getURLRelativa()) + HttpClientRequest.__saltoLinha
        host = 'Host: {0}'.format(urlParse.getHost()) + HttpClientRequest.__saltoLinha
        conexao = 'Connection: Closed'
        
        return get + host + conexao

    #enviando mensagem ao servidor via socket
    def __sendingGETMessage(self,s,getMessage):
        try:
            s.sendall(getMessage.encode('ascii'))
        except socket.error as msg:
            self.__log.writeLog('\tFalha ao enviar mensagem, código: ' + str(msg[0]) + ' ' + msg[1])
            sys.exit()

    #recebendo mensagem via socket do servidor
    def __receivingGETMessage(self,s):
        try:
            return s.recv(HttpClientRequest.__bufferSize).decode()
        except socket.error as msg:
            self.__log.writeLog('\tFalha ao receber mensagem, código: ' + str(msg[0]) + ' ' + msg[1])
            sys.exit()

