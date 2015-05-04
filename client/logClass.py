from datetime import datetime

#----------------------------------------------------
#Classe criada para gravar logs em arquivo
#----------------------------------------------------
class Log:
    #construtor do log
    def __init__(self, filename):
        #cria arquivo para escrita
        self.__filename = filename
        #linha da mensagem do log (mensagem um, dois, etc
        self.__logLine = 1
    
    #escreva em log
    def writeLog(self, message):
        file = open(self.__filename, 'a')
        file.write('#{0} - {1}\n'.format(self.__logLine, datetime.now()))
        file.write('{0}\n\n'.format(message))
        self.__logLine = self.__logLine + 1
        file.close()

