package httplibrary.util.validador;

/**
 * Valida argumentos passados por linha de comando
 * @author Ferreira
 */
class ValidadorArgumentosServidor implements Validador{
    // <editor-fold defaultstate="collapsed" desc="Atributos estaticos">
    private final int MAXIMO = 2;
    private final int MINIMO = 1;
    // 
    
    // <editor-fold defaultstate="collapsed" desc="Singleton">
    private static ValidadorArgumentosServidor instance;
    
    public static ValidadorArgumentosServidor getInstance()
    {
        if(instance == null)
            instance = new ValidadorArgumentosServidor();
        
        return instance;
    }
    // </editor-fold>
    
    @Override
    public void valida(Object o) throws ValidadorException { }

    /**
     * Valida todos os argumentos passados como parametro
     * @param array O array de argumentos a serem validados
     * @throws ValidadorException 
     */
    @Override
    public void valida(Object[] array) throws ValidadorException {
        if(array.length > MAXIMO)
            throw new ValidadorException(ValidadorCodigoErroEnum.MUITOS_ARGUMENTOS_PASSADOS);
        if(array.length < MINIMO)
            throw new ValidadorException(ValidadorCodigoErroEnum.POUCOS_ARGUMENTOS_PASSADOS);
        //valida porta
        ValidadorPortaTCP.getInstance().valida(array[0]);
    }
    
}
