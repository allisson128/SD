from httpClientRequest import HttpClientRequest
from sys import argv

#------------------------------------------------    
#teste criado para avaliar quantidade de argumentos
#------------------------------------------------
def verificarQuantidadeArgumentos():
    n = len(argv)
    if(n != 2 and n != 3):
        print("Insira URL")
        return -1
    if(n == 3 and argv[1] != 'post'):
        print("Apenas sera permitido \"post\" antes da URL")
        return -1
    
    return n

#------------------------------------------------    
#metodo MAIN
#------------------------------------------------

def main():
    n = verificarQuantidadeArgumentos()
    if(n == -1):
        exit()

    httpClientRequest = HttpClientRequest()
    
    if(n == 2):
        response = httpClientRequest.doGetRequest(argv[1])
        #exibe toda a resposta get
        print(response)
        html = httpClientRequest.htmlFromGETResponse(response)
        #exibe apenas a pagina html
        #print(httpClientRequest.htmlFromGETResponse(response))
        with open('output.html','w') as f:
            f.write(html)
    else:
        response = httpClientRequest.doPostRequest(argv[2])
        print(response)

main()
