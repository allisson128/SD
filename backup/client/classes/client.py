from httpClientRequest import HttpClientRequest
from sys import argv

#------------------------------------------------    
#teste criado para avaliar quantidade de argumentos
#------------------------------------------------
def verificarQuantidadeArgumentos():
    if(len(argv) < 2):
        print("Insira URL")
        return False

    if(len(argv) > 2):
        print("Insira apenas URL")
        return False
    
    return True

#------------------------------------------------    
#metodo MAIN
#------------------------------------------------

def main():
    if(not verificarQuantidadeArgumentos()):
        exit()

    httpClientRequest = HttpClientRequest()
    
    getResponse = httpClientRequest.doGetRequest(argv[1])
    #exibe toda a resposta get
    #print(getResponse)
    
    #exibe apenas a pagina html
    print(httpClientRequest.htmlFromGETResponse(getResponse))
    

main()
