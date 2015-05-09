/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package httplibrary.util.parser;

/**
 * Excecao para um parser
 */
public class ParserException  extends Exception{
    
    // <editor-fold defaultstate="collapsed" desc="Atributos">
    private final ParserCodigoErroEnum validador;
    // </editor-fold>
    
    // <editor-fold defaultstate="collapsed"  desc="Construtores">
    /**
     * Aloca uma classe para erros de validação
     * @param validador a enumeracao para erro do validador
     */
    public ParserException(ParserCodigoErroEnum validador)
    {
        this.validador = validador;
    }
    //</editor-fold>
    
    //<editor-fold defaultstate="collapsed"  desc="Metodos Sobreescritos">
    @Override
    public String toString()
    {
        return validador.getMensagemErro();
    }
    //</editor-fold>

}
