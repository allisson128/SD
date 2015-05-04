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
        self.__host  = parse[0]
        self.__porta = parse[1]
        self.__urlRelativa  = parse[2]
        self.__parametros = parse[3]

    #-------------------------------------
    # METODOS GET E SET
    #-------------------------------------

    #OBTER HOST DA URL
    def getHost(self):
        return self.__host
    
    #OBTER PORTA DA URL
    def getPorta(self):
        return self.__porta

    #OBTER URL RELATIVA
    def getURLRelativa(self):
        return self.__urlRelativa

    #OBTER URL RELATIVA GET
    def getURLRelativaGET(self):
        if(self.__parametros == ''):
            return self.__urlRelativa
        else:
            return self.__urlRelativa + '?' + self.__parametros

    #OBTER URL PARAMETROS
    def getParametrosURL(self):
        return self.__parametros

    #OBTER URL COMPLETA
    def getURLCompleta(self):
        return self.__host + ':' + str(self.__porta) + '/' + self._urlRelativa + '?' + self.__parametros
    
    #-------------------------------------
    # METODOS PARSER
    #-------------------------------------

    def __parseParametrosPost(urlRelativa):
    
        if(StringHandle.strContem(urlRelativa,'?')):
            i = urlRelativa.index('?')
            return(urlRelativa[:i],urlRelativa[i+1:])

        return(urlRelativa,'')

    #metodo da classe URLParse 
    def parseURL(url, portaPadrao = 80):
        host = ''
        porta = portaPadrao
        urlRelativa = ''
        parametros = ''

        #verifica se inicia com http ou https
        #se sim, remove da url
        if(StringHandle.strIniciaCom(url,'http://')):
            url = url[7:]
        if(StringHandle.strIniciaCom(url,'https://')):
            url = url[8:]
            porta = 443 #porta https

        host = url
        
        #verifica se contem url relativa
        if(StringHandle.strContem(url,'/')):
            i = url.index('/')
            host = url[:i]
            urlRelativa = url[i+1:]
			
           	#verifica se url nao contem ponto no final, significando extensao (.html, .jsp)
            if(not StringHandle.strContem(urlRelativa,'.')):
                urlRelativa = urlRelativa + '/'

			#trata os parametros caso existam
            (urlRelativa, parametros) = URLParse.__parseParametrosPost(urlRelativa)

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
           
        return (host,porta,urlRelativa,parametros)

#fim da classe
"""
url = URLParse('http://www.efacil.com.br/loja/ProductDisplay?storeId=10154&catalogId=10051&productId=45787&langId=-6&canal=ca_9784&redirectflag=true&canal=ca_9784&gclid=CP3rkfHaqMUCFYEjgQod9rIAjg')
print(url.getHost())
print(url.getPorta())
print(url.getURLRelativa())
print(url.getParametrosURL())
"""
