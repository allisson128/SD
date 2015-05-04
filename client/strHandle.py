from datetime import datetime

#----------------------------------------------------
# METODOS PARA TRATAMENTO DE STRING
#----------------------------------------------------

class StringHandle:
    #----------------------------------
    # METODOS ESTATICOS
    #----------------------------------
    
    #------------------------------------------------   
    # Se uma string inicia com string definida como inicio
    #------------------------------------------------   
    def strIniciaCom(string, inicio):
        return (string[:len(inicio)] == inicio)

    #------------------------------------------------   
    # Se a string contem o conteudo.
    #------------------------------------------------   

    def strContem(string, conteudo):
        n = len(string)
        i = 0
        try:
            while(i < n):
                i = string.index(conteudo)
                m = len(conteudo)
                
                if(string[i:i+m] == conteudo):
                    return True
                string = string[i+1:]
                i = 0
            return False
        except ValueError:
            return False

    #------------------------------------------------    
    # Retorna formato string para data usado na resposta GET
    # Se nao passar nenhum argumento, formato da data atual em GMT (UTC)
    # Exemplo: 'Date: Fri, 17 Apr 2015 02:06:10 GMT'
    #------------------------------------------------

    def strDateFormat(self,date = datetime.utcnow()):
        strWeekDay = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        strMonth   = ["NOT", "Jan", "Feb", "Mar", "Apr", "May", "Jun",
                      "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        time    = datetime.utctimetuple(date)
        
        weekday = strWeekDay[time.tm_wday]
        day     = self.__strTwoDigitNumber(time.tm_mday)
        month   = strMonth[time.tm_mon]
        year    = time.tm_year
        hour    = self.__strTwoDigitNumber(time.tm_hour)
        minute  = self.__strTwoDigitNumber(time.tm_min)
        second  = self.__strTwoDigitNumber(time.tm_sec)
        
        return "Date: {0}, {1} {2} {3} {4}:{5}:{6} GMT".format(weekday,day,month,year,
                                                               hour,minute,second)
    #------------------------------------------------    
    # insere numero zero se numero for menor que 10
    # ex: 1 => 01
    #------------------------------------------------
    def strTwoDigitNumber(self,n):
        if(n < 10):
            return '0{0}'.format(n)
        
        return '{0}'.format(n)
