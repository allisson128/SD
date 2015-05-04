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
        print('Iniciando requisição GET para URL \"' + url + '\"...')
        self.__log.writeLog('Iniciando requisição GET para URL \"' + url + '\"...')

        #captura URL
        print('Parsing URL...')
        self.__log.writeLog('Parsing URL...')
        
        urlParse  = self.__getURLParsed(url)

        #captura IP remoto e porta
        print('Obtendo Host IP e numero da porta para conexao...')
        self.__log.writeLog('Obtendo Host IP e numero da porta para conexao...')
        
        socketInfo = self.__getIPPortHost(urlParse)

        print('\t::IP para host \"' + urlParse.getHost() + '\" = ' + socketInfo[0] + '!')
        print('\t::Porta da conexao = ' + str(socketInfo[1]) + '!')
        self.__log.writeLog('\t::IP para host \"' + urlParse.getHost() + '\" = ' + socketInfo[0] + '!')
        self.__log.writeLog('\t::Porta da conexao = ' + str(socketInfo[1]) + '!')
        
        #obtendo socket
        print('Criando socket TCP...')
        self.__log.writeLog('Criando socket TCP...')
        
        s = self.__openTCPSocketIPv4()
        
        print('\t::Socket criado com sucesso!')
        self.__log.writeLog('\t::Socket criado com sucesso!')
        
        #iniciando conexao
        print('Iniciando conexao...')
        self.__log.writeLog('Iniciando conexao...')
        
        self.__beginSocketConnection(s, socketInfo)
        
        print('\t::Conexao iniciada em IP \"'+socketInfo[0]+'\" e Porta \"'+str(socketInfo[1])+'\"!')
        self.__log.writeLog('\t::Conexao iniciada em IP \"'+socketInfo[0]+'\" e Porta \"'+str(socketInfo[1])+'\"!')
        
        #montando mensagem GET
        print('Montando mensagem GET...')
        self.__log.writeLog('Montando mensagem GET...')
        getMessage = self.__createGETMessageRequest(urlParse)
        print('\t::MENSAGEM GET\n****\n'+getMessage+'\n****')
        self.__log.writeLog('\t::MENSAGEM GET\n****\n'+getMessage+'\n****')
        
        #enviando mensagem via socket
        print('Enviando mensagem via socket...')
        self.__log.writeLog('Enviando mensagem via socket...')
        self.__sendingMessage(s,getMessage)
        print('\t::Mensagem enviada com sucesso!')
        self.__log.writeLog('\t::Mensagem enviada com sucesso!')

        #recebendo mensagem do servidor
        print('Recebendo mensagem do servidor...')
        self.__log.writeLog('Recebendo mensagem do servidor...')
        receivedMessage = self.__receivingMessage(s)
        print('\t::Mensagem recebida com sucesso de Host \"'+socketInfo[0]+'\" Porta \"'+str(socketInfo[1])+'\"!')
        print('\t::MENSAGEM RECEBIDA\n\n****\n'+receivedMessage+'\n****')
        self.__log.writeLog('\t::Mensagem recebida com sucesso de Host \"'+socketInfo[0]+'\" Porta \"'+str(socketInfo[1])+'\"!')
        self.__log.writeLog('\t::MENSAGEM RECEBIDA\n\n****\n'+receivedMessage+'\n****')

        return receivedMessage

    #Realiza o metodo POST do HTTP
    def doPostRequest(self,url):
        print('Iniciando requisição POST para URL \"' + url + '\"...')
        self.__log.writeLog('Iniciando requisição POST para URL \"' + url + '\"...')

        #captura URL
        print('Parsing URL...')
        self.__log.writeLog('Parsing URL...')
        
        urlParse  = self.__getURLParsed(url)

        #captura IP remoto e porta
        print('Obtendo Host IP e numero da porta para conexao...')
        self.__log.writeLog('Obtendo Host IP e numero da porta para conexao...')
        
        socketInfo = self.__getIPPortHost(urlParse)

        print('\t::IP para host \"' + urlParse.getHost() + '\" = ' + socketInfo[0] + '!')
        print('\t::Porta da conexao = ' + str(socketInfo[1]) + '!')
        self.__log.writeLog('\t::IP para host \"' + urlParse.getHost() + '\" = ' + socketInfo[0] + '!')
        self.__log.writeLog('\t::Porta da conexao = ' + str(socketInfo[1]) + '!')
        
        #obtendo socket
        print('Criando socket TCP...')
        self.__log.writeLog('Criando socket TCP...')
        
        s = self.__openTCPSocketIPv4()
        
        print('\t::Socket criado com sucesso!')
        self.__log.writeLog('\t::Socket criado com sucesso!')
        
        #iniciando conexao
        print('Iniciando conexao...')
        self.__log.writeLog('Iniciando conexao...')
        
        self.__beginSocketConnection(s, socketInfo)
        
        print('\t::Conexao iniciada em IP \"'+socketInfo[0]+'\" e Porta \"'+str(socketInfo[1])+'\"!')
        self.__log.writeLog('\t::Conexao iniciada em IP \"'+socketInfo[0]+'\" e Porta \"'+str(socketInfo[1])+'\"!')
        
        #montando mensagem GET
        print('Montando mensagem POST...')
        self.__log.writeLog('Montando mensagem POST...')
        message = self.__createPOSTMessageRequest(urlParse)
        print('\t::MENSAGEM POST\n****\n'+message+'\n****')
        self.__log.writeLog('\t::MENSAGEM POST\n****\n'+message+'\n****')
        
        #enviando mensagem via socket
        print('Enviando mensagem via socket...')
        self.__log.writeLog('Enviando mensagem via socket...')
        self.__sendingMessage(s,message)
        print('\t::Mensagem enviada com sucesso!')
        self.__log.writeLog('\t::Mensagem enviada com sucesso!')

        #recebendo mensagem do servidor
        print('Recebendo mensagem do servidor...')
        self.__log.writeLog('Recebendo mensagem do servidor...')
        receivedMessage = self.__receivingMessage(s)
        print('\t::Mensagem recebida com sucesso de Host \"'+socketInfo[0]+'\" Porta \"'+str(socketInfo[1])+'\"!')
        print('\t::MENSAGEM RECEBIDA\n\n****\n'+receivedMessage+'\n****')
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
            print('\tErro: ' + e)
            self.__log.writeLog('\tErro: ' + e)
            sys.exit()
    
    #Recebe IP e porta atraves de um endereco host
    def __getIPPortHost(self,urlParse):
        try:
            return (socket.gethostbyname(urlParse.getHost()), urlParse.getPorta())
        except socket.gaierror:
            print('\tErro:: Não foi possível encontrar o servidor')
            self.__log.writeLog('\tErro:: Não foi possível encontrar o servidor')
            sys.exit()
    
    #Abre socket TCP IPv4 
    def __openTCPSocketIPv4(self):
        try:
            return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as msg:
            print('\tFalha ao criar socket')
            self.__log.writeLog('\tFalha ao criar socket')
            sys.exit()

    #Inicia conexao
    def __beginSocketConnection(self,s,socketInfo,timeout = 30):
        s.settimeout(timeout)
        try:
            s.connect(socketInfo)
        except socket.error as msg:
            print('\tFalha ao conectar socket')
            self.__log.writeLog('\tFalha ao conectar socket')
            sys.exit()

    #monta mensagem GET
    def __createGETMessageRequest(self,urlParse):
        get  = 'GET /{0} HTTP/1.0'.format(urlParse.getURLRelativaGET()) + HttpClientRequest.__saltoLinha
        host = 'Host: {0}:{1}'.format(urlParse.getHost(), urlParse.getPorta()) + HttpClientRequest.__saltoLinha
        conexao = 'Connection: keep-alive'
        
        return get + host + conexao

    #monta mensagem GET
    def __createPOSTMessageRequest(self,urlParse):
        post  = 'POST /{0} HTTP/1.0'.format(urlParse.getURLRelativa()) + HttpClientRequest.__saltoLinha
        host = 'Host: {0}:{1}'.format(urlParse.getHost(), urlParse.getPorta()) + HttpClientRequest.__saltoLinha
        conexao = 'Connection: keep-alive' + HttpClientRequest.__saltoLinha
        parametros = urlParse.getParametrosURL() + HttpClientRequest.__saltoLinha + HttpClientRequest.__saltoLinha
        
        return post + host + conexao + parametros


    #enviando mensagem ao servidor via socket
    def __sendingMessage(self,s,getMessage):
        try:
            s.sendall(getMessage.encode('ascii'))
        except socket.error as msg:
            self.__log.writeLog('\tFalha ao enviar mensagem')
            sys.exit()

    #recebendo mensagem via socket do servidor
    def __receivingMessage(self,s):
        try:
            return s.recv(HttpClientRequest.__bufferSize).decode()
        except socket.error as msg:
            self.__log.writeLog('\tFalha ao receber mensagem')
            sys.exit()
