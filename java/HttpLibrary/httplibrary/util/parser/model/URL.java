package httplibrary.util.parser.model;

/**
 * Especifica uma URL na aplicaçao.
 */
public class URL {

    // <editor-fold defaultstate="collapsed" desc="Atributos">
    private String host;
    private int porta;
    private String urlRelativa;
    private String parametros;
    // </editor-fold>
    
    // <editor-fold defaultstate="collapsed" desc="Construtores">
    public URL() {}
    
    public URL(String host, int porta) {
        this.host = host;
        this.porta = porta;
    }

    public URL(String host, int porta, String urlRelativa) {
        this.host = host;
        this.porta = porta;
        this.urlRelativa = urlRelativa;
    }

    public URL(String host, int porta, String urlRelativa, String parametros) {
        this.host = host;
        this.porta = porta;
        this.urlRelativa = urlRelativa;
        this.parametros = parametros;
    }
    // </editor-fold>
    
    // <editor-fold defaultstate="collapsed" desc="Metodos Getters">
    /**
     * Retorna o dominio da URL.
     * ex: localhost:8080/lala -> localhost
     * @return the host
     */
    public String getHost() {
        return host;
    }

    /**
     * Retorna a porta da URL
     * ex: localhost:8080/lala -> 8080
     * @return the porta
     */
    public int getPorta() {
        return porta;
    }

    /**
     * Retorna a url relativa (endereco relativo ao dominio).
     * ex: localhost:8080/lala -> lala
     * @return the porta
     */
    public String getUrlRelativa() {
        return urlRelativa;
    }

    /**
     * Retorna os parametros para metodos GET e POST do HTTP.
     * Exemplo:
     * localhost:8080/lala?nome=joao&sobrenome=pedro -> nome=joao&sobrenome=pedro
     * @return the parametros
     */
    public String getParametros() {
        return parametros;
    }
    // </editor-fold>
    
}
