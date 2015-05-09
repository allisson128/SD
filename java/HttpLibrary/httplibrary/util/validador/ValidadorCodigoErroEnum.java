/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package httplibrary.util.validador;

/**
 *  Enumeracao para especificar codigos de erros para uma validação. 
 */
enum ValidadorCodigoErroEnum {
    
    // <editor-fold defaultstate="collapsed" desc="Enumerações">
    
        // <editor-fold defaultstate="collapsed" desc="Enumerações para validação da porta">
    /** Código de erro para quando uma porta TCP em formato de string nao for um numero. */
    PORTA_TCP_NAO_NUMERICA(0x60, "Código 0x60: Porta TCP informada não é um número"),
    /** Código de erro para quando uma porta TCP não está no intervalo. */
    PORTA_TCP_FORA_INTERVALO(0x61, "Código 0x61: Porta TCP fora do intervalo de 0 a 65535"),
    //</editor-fold>
    
        // <editor-fold defaultstate="collapsed" desc="Enumerações para argumentos passados pelo usuario">
    /** Código de erro para quando uma a quantidade de argumentos ultrapassa o maximo. */
    MUITOS_ARGUMENTOS_PASSADOS (0x50, "Código 0x50: Quantidade de argumentos maior que o máximo"),
    /** Código de erro para quando uma a quantidade de argumentos ultrapassa o mínimo. */
    POUCOS_ARGUMENTOS_PASSADOS (0x51, "Código 0x51: Quantidade de argumentos menor que o mínimo")
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
    ValidadorCodigoErroEnum(int codigo, String msgErro)
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
