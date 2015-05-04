from httpServerResponse import HttpServerResponse
from sys import argv
import sys

#------------------------------------------------    
#metodo main
#------------------------------------------------
def main():
    if(verificarQuantidadeArgumentos()):
        try:
           server = HttpServerResponse(argv[1],int(argv[2]))
           server.launchGETServer()
        except ValueError as e:
            print("Porta inserida nao e' um numero" + str(e))
            sys.exit()

#------------------------------------------------    
#teste criado para avaliar quantidade de argumentos
#------------------------------------------------
def verificarQuantidadeArgumentos():
    if(len(argv) != 3):
        print("Insira URL e porta")
        return False
    
    return True

main()
