/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package httplibrary.util.validador;

import httplibrary.util.validador.ValidadorException;

/**
 *  Interface utilizada para implementaçoes de um validador.
 *  Possui um único método chamado "valida", o qual recebe um
 *  objeto e retorna se ele está válido ou não
 */
public interface Validador {
    
    // <editor-fold defaultstate="collapsed" desc="Métodos de verificação">
    /**
     * Realiza a validação de um objeto de acordo com as especificações do validador. Erros
     * são retornados de acordo 
     * @param o O objeto a ser validado
     * @throws httplibrary.util.validador.ValidadorException
     */
    public void valida(Object o) throws ValidadorException;
    
    /**
     * Realiza a validação de um array de objetos de acordo com as especificações do validador. Erros
     * são retornados de acordo 
     * @param array O objeto a ser validado
     * @throws httplibrary.util.validador.ValidadorException
     */
    public void valida(Object[] array) throws ValidadorException;
    //</editor-fold>
    
    
}
