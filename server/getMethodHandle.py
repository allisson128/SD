from strHandle import StringHandle
from logClass import Log
import sys

#------------------------------------------------------------------
# UTILIZADA PARA MANIPULACAO DO METODO GET
#------------------------------------------------------------------
    
class GETMethodHandle:
    __SALTO_LINHA = '\r\n\r\n'
    #__SALTO_LINHA = '\n'

    def __init__(self, logfilename):
        self.__log = Log(logfilename)
    #------------------------------------------------------------------
    # PARSER PARA REQUISICAO GET
    #------------------------------------------------------------------
    
    def parseGETRequest(self,dados):
        strings = dados.split(GETMethodHandle.__SALTO_LINHA)
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
    
    def createResponse(self,host,urlRelative):
        code = "200"
        descriptionCode = "OK"
        try:
            html = self.__getHTMLText(urlRelative)
         
        #except FileNotFoundError:
        #    html = self.__get404Page()
        #    code = "404"
        #    descriptionCode = "Not Found"
        
        except Exception:
            html = self.__get404Page()
            code = "404"
            descriptionCode = "Not Found"

        strings = []
        strings.append("HTTP/1.0 {0} {1}".format(code, descriptionCode))
        strings.append(StringHandle.strDateFormat())
        strings.append("Content-Length: {0}".format(len(html)))
        strings.append("Content-Type: text/html; charset=UTF-8")
        strings.append(GETMethodHandle.__SALTO_LINHA)
        strings.append(html)

        return GETMethodHandle.__SALTO_LINHA.join(strings)
       
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
        strings.append('\t\t<h2>Pagina requisitada nao foi encontrada</h2>')
        strings.append('\t</div>')
        strings.append('</body>')
        strings.append('</html>')

        return GETMethodHandle.__SALTO_LINHA.join(strings)
  
    # Recupera pagina URL do servidor. As paginas devem estar na pasta www
    def __getHTMLText(self,urlRelative):
        #adiciona o diretorio geral WWW
        urlRelative = 'www' + urlRelative

        if(not StringHandle.strContem(urlRelative,'.')):
            #verifica se o final é um diretorio
            n = len(urlRelative)
            if(urlRelative[n-1] == '/'):
                urlRelative = urlRelative + 'index.html'
            else:
                urlRelative = urlRelative + '/index.html'

        with open(urlRelative,'r') as f:
            return f.read()
