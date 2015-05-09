/**
 * Pacote utilizado para métodos úteis para a aplicação
 */
package httplibrary.util.validador;

/**
 * Realiza a validação da porta. Implemeta a interface Validador.
 * @author Ferreira
 */
class ValidadorPortaTCP implements Validador
{
    // <editor-fold defaultstate="collapsed" desc="Singleton">
    private static ValidadorPortaTCP instance;
    
    public static ValidadorPortaTCP getInstance()
    {
        if(instance == null)
            instance = new ValidadorPortaTCP();
        
        return instance;
    }
    // </editor-fold>
    
    //<editor-fold defaultstate="collapsed" desc="Métodos de verificação">
    @Override
    public void valida(Object o) throws ValidadorException {
        try
        {
            int porta = Integer.parseInt(o.toString());
            if(porta < 0 || porta > 65535)
                throw new ValidadorException(ValidadorCodigoErroEnum.PORTA_TCP_FORA_INTERVALO);
        } catch(NumberFormatException e) {
            throw new ValidadorException(ValidadorCodigoErroEnum.PORTA_TCP_NAO_NUMERICA);
        }
    }
    //</editor-fold>

    @Override
    public void valida(Object[] array) throws ValidadorException {}
    
}
