package httplibrary.util.parser;

import java.util.HashMap;

/**
 * Fabrica de parser
 */
public class ParserFactory {
    
    // <editor-fold defaultstate="collapsed" desc="Atributos">
    private HashMap<ParserFactoryEnum, Parser> factory;
    //</editor-fold>
    
    // <editor-fold defaultstate="collapsed" desc="Singleton">
    private static ParserFactory instance;
    /**
     * Retorna uma instancia de ValidadorFactory.
     * Desta forma haverá apenas uma instancia na memória, 
     * respeitando o padrão Singleton
     * @return ValidadorFactory
     */
    
    public static ParserFactory getInstance()
    {
        if(instance == null)
            instance = new ParserFactory();
        
        return instance;
    }
    //</editor-fold>
    
    // <editor-fold defaultstate="collapsed" desc="Construtor">
    public ParserFactory()
    {
        iniciaFabrica();
    }
    //</editor-fold>
    
    // <editor-fold defaultstate="collapsed" desc="Métodos">
    private void iniciaFabrica()
    {
        this.factory = new HashMap<>();
        this.factory.put(ParserFactoryEnum.PARSER_URL_FACTORY,
                         ParserURL.getInstance());
    }
    
    public Parser getParser(ParserFactoryEnum tipo)
    {
        return this.factory.get(tipo);
    }
    //</editor-fold>    
}
