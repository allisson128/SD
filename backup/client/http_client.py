import socket
from sys import argv

PORTA_PADRAO_HTTP = 80

"""------------------------------------------------
IMPLEMENTACAO BASICA DE HTTP_GET CONFORME EXERCICIO 1

E' REALIZADA A PASSAGEM POR PARAMETRO DE UMA URL

ex: python http_client www.google.com/
ACRESCENTE UMA BARRA SEMPRE QUE FOR UM ENDERECO ONDE
O FINAL NAO E' UMA PAGINA .html ou com demais extensoes

AINDA RESTA REVER O PARSER E CRIAR UM PARSER SOBRE A RESPOSTA
DEVOLVIDA PELO GET COMO CAPTURAR A PAGINA HTML RETORNADA
------------------------------------------------"""

"""------------------------------------------------ 
realiza o parse da url.
------------------------------------------------"""
def parseURL(url):
    #remove da url caso inicia com http:// ou https://
    if(url[:7] == "http://"):
        url = url[7:]
    if(url[:8] == "https://"):
        url = url[8:]
    
    #insere barra '/' no final do endereco se ultimo caracter nao for '/'
    #if(url[-1] != '/'):
    #    url = url + '/'

    indexBarra = url.index('/')             #captura indice da primeira ocorrencia de '/'
    urlHost = url[0:indexBarra]             #substring da url ate ocorrencia de '/'
    urlRelativa = url[indexBarra+1:]        #substring apos ocorrencia de '/'
    
    porta = PORTA_PADRAO_HTTP
    #se existir a porta
    #if(':' in url):
    #    indexPontos = url.index(':')        #captura indice da primeira ocorrencia de ':' em urlHost
    #    urlHost = url[0:indexPontos]        #captura urlHost ate ocorrencia de ':'
    #    porta = int(url[indexPontos+1:])    #recupera porta entre ':' e primeira barra '/'
    
    return(urlHost,porta,urlRelativa)

"""------------------------------------------------ 
retorna um novo socket sobre internet (AF_INET) utilizando TCP (SOCK_STREAM)
------------------------------------------------"""
def novoSocketTCP():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""------------------------------------------------ 
retorna a mensagem do metodo GET a ser enviada para o servidor
exemplo: 

GET / HTTP/1.0
Host: www.google.com
------------------------------------------------"""
def GETMethodString(host, relativeURL):
    return "GET /{0} HTTP/1.0\r\n\r\nHost: {1}\r\n\r\n".format(relativeURL, host)

"""------------------------------------------------ 
implementacao do get via socket
------------------------------------------------"""
def httpGET(url):
    (urlHost,tcp_port,relativeURL) = parseURL(argv[1])
    tcp_ip = socket.gethostbyname(urlHost)
    bufferSize = 9000
    mensagem = GETMethodString(urlHost,relativeURL)
    
    print("DEBUG::IP:\n\n "+tcp_ip+"\n")
    print("DEBUG::mensagem:\n\n "+mensagem+"\n")
    
    s = novoSocketTCP()
    s.connect((tcp_ip, tcp_port))
    #se nao responder em 10 segundos, encerra a conexao
    s.settimeout(10)
    
    s.send(mensagem.encode('ascii'))
    data = s.recv(bufferSize)
    s.close()

    return data.decode()


"""------------------------------------------------    
teste criado para avaliar quantidade de argumentos
------------------------------------------------"""
def verificarQuantidadeArgumentos():
    if(len(argv) < 2):
        print("Insira URL")
        return False

    if(len(argv) > 2):
        print("Insira apenas URL")
        return False
    
    return True

"""------------------------------------------------    
metodo MAIN
------------------------------------------------"""

def main():
    if(not verificarQuantidadeArgumentos()):
        exit()

    data = httpGET(argv[1])
    print(data)

main()
