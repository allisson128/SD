#----------------------------------------------------
# METODOS PARA TRATAMENTO DE STRING
#----------------------------------------------------

class StringHandle:
    #----------------------------------
    # METODOS ESTATICOS
    #----------------------------------
    
    """
    Se uma string inicia com string definida como inicio
    """
    def strIniciaCom(string, inicio):
        return (string[:len(inicio)] == inicio)

    """
    Se a string contem o conteudo.
    """
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
