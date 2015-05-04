#importa arquivo python com metodos uteis para string
from strHandle import StringHandle

#---------------------------------------------------
#Classe URLParse: efetua o parse de uma URL
#---------------------------------------------------

class URLException(Exception):
    #construtor da excecao
    def __init__(self, mensagem):
        super(URLException, self).__init__(mensagem)

class URLParse:
    #construtor da classe, recebe uma URL
    def __init__(self, url):
        parse = URLParse.parseURL(url)
        self._host  = parse[0]
        self._porta = parse[1]
        self._urlRelativa  = parse[2]

    #-------------------------------------
    # METODOS GET E SET
    #-------------------------------------

    #OBTER HOST DA URL
    def getHost(self):
        return self._host
    
    #OBTER PORTA DA URL
    def getPorta(self):
        return self._porta

    #OBTER URL RELATIVA
    def getURLRelativa(self):
        return self._urlRelativa

    #OBTER URL COMPLETA
    def getURLCompleta(self):
        return self._host + ':' + str(self._porta) + '/' + self._urlRelativa
    
    #-------------------------------------
    # METODOS GET E SET
    #-------------------------------------

    #metodo da classe URLParse 
    def parseURL(url, portaPadrao = 80):
        host = ''
        porta = portaPadrao
        urlRelativa = ''

        #verifica se inicia com http ou https
        #se sim, remove da url
        if(StringHandle.strIniciaCom(url,'http://')):
            url = url[7:]
        if(StringHandle.strIniciaCom(url,'https://')):
            url = url[8:]

        host = url
        
        #verifica se contem url relativa
        if(StringHandle.strContem(url,'/')):
           i = url.index('/')
           host = url[:i]
           urlRelativa = url[i+1:]

           #verifica se url nao contem ponto no final, significando extensao (.html, .jsp)
           if(not StringHandle.strContem(urlRelativa,'.')):
               urlRelativa = urlRelativa + '/'

        #verifica se porta foi informada pelo usuario
        if(StringHandle.strContem(host,':')):
            i = host.index(':')
            #lanca excecao se porta nao for um numero ou fora do intervalo [0,65095]
            try:
                porta = int(host[i+1:])
                if(porta < 0 or porta > 65095):
                    raise URLException("Valor da porta deve estar no intervalo [0,65095]")
            except ValueError:
                raise URLException("Valor da porta deve ser um número")
            host = host[:i]
           
        return (host,porta,urlRelativa)
