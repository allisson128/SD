/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package httplibrary.util.validador;

/**
 * Enumeração para o tipo de validador a ser retornado pela fábrica.
 * @author Ferreira
 */
public enum ValidadorFactoryEnum {
    
    /// <editor-fold defaultstate="collapsed" desc="Enumeração">
    /** Solicitação para um validador de portas TCP */
    VALIDADOR_PORTA_TCP,
    /** Solicitação para um validador de argumentos do programa servidor */
    VALIDADOR_ARGUMENTOS_SERVIDOR
    //</editor-fold>
    
}
