/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package httplibrary.util.parser;

import httplibrary.util.parser.model.URL;
import httplibrary.util.validador.Validador;
import httplibrary.util.validador.ValidadorException;
import httplibrary.util.validador.ValidadorFactory;
import httplibrary.util.validador.ValidadorFactoryEnum;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author a11111BCC031
 */
public class ParserURL implements Parser{
    
    // <editor-fold defaultstate="collapsed" desc="Constantes">
    /** Porta padrao do protocolo HTTP */
    private static final int PORTA_PADRAO = 80;
    // <editor-fold>
    
    
    // <editor-fold defaultstate="collapsed" desc="Singleton">
    private static ParserURL instance;
    /**
     * Retorna uma instancia de ValidadorFactory.
     * Desta forma haverá apenas uma instancia na memória, 
     * respeitando o padrão Singleton
     * @return ValidadorFactory
     */
    
    public static ParserURL getInstance()
    {
        if(instance == null)
            instance = new ParserURL();
        
        return instance;
    }
    //</editor-fold>
    
    @Override
    public Object parse(String str) throws ParserException{
        String host = "", urlRelativa = "", parametros = "";
        String url = str;
        int porta = PORTA_PADRAO;
        int i;

        url = verificaSeIniciaHttp(url);
        host = url;
        
        if(contemUrlRelativa(url))
        {
            i = url.indexOf("/");
            host = url.substring(0, i);
            urlRelativa = url.substring(i + 1);
            
            if(contemParametros(urlRelativa))
            {
                i = urlRelativa.indexOf("?");
                parametros = urlRelativa.substring(i+1);
                urlRelativa = urlRelativa.substring(0, i);
            }
            
            if(contemExtensaoArquivo(urlRelativa))
                urlRelativa += '/';
        }
        
        if(contemPorta(host))
        {
            i = host.indexOf(":");
            porta = validaPorta(host);
            host = host.substring(0, i);
        }
        
        return new URL(host, porta, urlRelativa, parametros);
    }
    
    /**
     * 
     * @param host
     * @return o numero da porta
     * @throws ParserException se a porta for invalida
     */
    private int validaPorta(String host) throws ParserException {
        int i;
        String porta;
        
        i = host.indexOf(":");
        Validador v = ValidadorFactory.getInstance().getValidador(ValidadorFactoryEnum.VALIDADOR_PORTA_TCP);
        
        porta = host.substring(i+1);
        try {
            v.valida(porta);
        } catch (ValidadorException ex) {
            throw new ParserException(ParserCodigoErroEnum.PORTA_INVALIDA);
        }
        
        return Integer.parseInt(porta);
    }

    private static boolean contemPorta(String host) {
        return host.contains(":");
    }

    /**
     * Retorna se a url relativa contem no final uma extensao como html, jsp e 
     * entre outras.
     * @param urlRelativa
     * @return 
     */
    private boolean contemExtensaoArquivo(String urlRelativa) {
        return urlRelativa.contains(".");
    }

    
    /**
     * Verifica se a url inicia com 'http://' ou 'https://'.
     * Caso contem, remove do prefixo
     * @param url a string da url
     * @return a url sem o prefixo 'http://' ou 'https://'
     */
    private String verificaSeIniciaHttp(String url) {
        if(url.startsWith("http://"))
            url = url.substring(7);
        if(url.startsWith("https://"))
            url = url.substring(8);
        
        return url;
    }
    
    /**
     * Retorna se contem parametros na url
     * @param url
     * @return 
     */
    private boolean contemParametros(String url) {
        return url.contains("?");
    }
    
    /**
     * Retorna se possui URL relativa
     * @param url
     * @return 
     */
    private boolean contemUrlRelativa(String url) {
        return url.contains("/");
    }

    
}
