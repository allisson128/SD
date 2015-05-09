
package httpserver.server;

import java.io.IOException;

/**
 * Servidor HTTP implementando o servidor generico.
 */
public class HttpServer extends GenericServer {

    /**
     * Inicia um servidor HTTP. O servidor já é inicializado assim que 
     * é criado o construtor
     * @param porta
     * @param diretorioArquivos
     * @throws IOException 
     */
    public HttpServer(int porta, String diretorioArquivos) throws IOException {
        super(porta, diretorioArquivos);
    }

    @Override
    protected String performService(RequisicaoSocket requisicao) {
        return "SEJA BEM VINDO "+ requisicao.getId() +", CLIENTE DE IP "+requisicao.getEnderecoIP();
    }
    
}
