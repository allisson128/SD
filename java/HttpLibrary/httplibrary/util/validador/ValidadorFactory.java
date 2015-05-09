/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package httplibrary.util.validador;

import java.util.HashMap;

/**
 * Fábrica de métodos de validação. Esta classe retorna métodos para validação
 * de objetos informando qual o tipo de validação deseja realizar
 */
public class ValidadorFactory {
    
    // <editor-fold defaultstate="collapsed" desc="Atributos">
    private HashMap<ValidadorFactoryEnum, Validador> factory;
    //</editor-fold>
    
    // <editor-fold defaultstate="collapsed" desc="Singleton">
    private static ValidadorFactory instance;
    /**
     * Retorna uma instancia de ValidadorFactory.
     * Desta forma haverá apenas uma instancia na memória, 
     * respeitando o padrão Singleton
     * @return ValidadorFactory
     */
    
    public static ValidadorFactory getInstance()
    {
        if(instance == null)
            instance = new ValidadorFactory();
        
        return instance;
    }
    //</editor-fold>
    
    // <editor-fold defaultstate="collapsed" desc="Construtor">
    public ValidadorFactory()
    {
        iniciaFabrica();
    }
    //</editor-fold>
    
    // <editor-fold defaultstate="collapsed" desc="Métodos">
    private void iniciaFabrica()
    {
        this.factory = new HashMap<>();
        this.factory.put(ValidadorFactoryEnum.VALIDADOR_PORTA_TCP, 
                         ValidadorPortaTCP.getInstance());
        this.factory.put(ValidadorFactoryEnum.VALIDADOR_ARGUMENTOS_SERVIDOR, 
                         ValidadorArgumentosServidor.getInstance());
    }
    
    public Validador getValidador(ValidadorFactoryEnum tipo)
    {
        return this.factory.get(tipo);
    }
    //</editor-fold>
}
