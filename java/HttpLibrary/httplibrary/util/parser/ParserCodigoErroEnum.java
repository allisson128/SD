/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package httplibrary.util.parser;

/**
 * Códigos de erro para parser
 * @author a11111BCC031
 */
enum ParserCodigoErroEnum {
       
    // <editor-fold defaultstate="collapsed" desc="Enumerações">
    
        // <editor-fold defaultstate="collapsed" desc="Enumerações para erros do parser ">
        URL_INVALIDA (0x71, "Código 0x71 : A url passada para o parser é inválida!"),
        PORTA_INVALIDA (0x72, "Código 0x71 : Porta descrita pela URL é inválida ou fora do intervalo [0, 65535]")
        // </editor-fold>
    
        // <editor-fold defaultstate="collapsed" desc="Ponto-virgula finalizador (nao remova-o)">
        ;
        // </editor-fold>
    
    //</editor-fold>
    
    // <editor-fold defaultstate="collapsed" desc="Atributos">
    private final int codigo;
    private final String msgErro;
    //</editor-fold>
    
    // <editor-fold defaultstate="collapsed" desc="Construtor">
    /**
     * Construtor para a enumeração, informando o código de erro e a mensagem de erro
     * @param codigo O código do erro
     * @param msgErro Mensagem de erro
     */
    ParserCodigoErroEnum(int codigo, String msgErro)
    {
        this.codigo = codigo;
        this.msgErro = msgErro;
    }
    //</editor-fold>
    
    // <editor-fold defaultstate="collapsed" desc="Metodos GET">
    /**
     * @return O código de erro em formato HEXADECIMAL
     */
    public String getCodigo() {
        return Integer.toHexString(codigo);
    }

    /**
     * @return A mensagem de erro
     */
    public String getMensagemErro() {
        return msgErro;
    }
    //</editor-fold>
    
}
