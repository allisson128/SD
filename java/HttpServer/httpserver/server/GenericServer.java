package httpserver.server;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import httplibrary.util.HttpSocketHandler;

/**
 * Classe abstrata contendo implementação básica de um servidor socket.
 * Demais classes que herdarem desta classe devem implementar seu metodo, no
 * qual ao receber uma String de requisicao do cliente ele retorna a resposta
 * desejada
 */
abstract class GenericServer {
    
    // <editor-fold defaultstate="collapsed" desc="Atributos">
    private final ServerSocket serverSocket;
    private final String diretorioArquivos;
    private final int porta;
    // </editor-fold>
    
    // <editor-fold defaultstate="collapsed" desc="Construtores">
    public GenericServer(int porta, String diretorioArquivos) throws IOException
    {
        this.porta = porta;
        this.diretorioArquivos = diretorioArquivos;
        
        //inicia um socket servidor
        this.serverSocket = new ServerSocket(this.porta);
        iniciaServidor();
    }
    // </editor-fold>

    // <editor-fold defaultstate="collapsed" desc="Metodos">
    /**
     * Método responsável por iniciar o servidor
     * @throws IOException 
     */
    private void iniciaServidor() throws IOException
    {
        HttpSocketHandler handler = HttpSocketHandler.getInstance();
        System.out.println("Servidor foi inicializado em IP " + 
                            handler.getEnderecoIP(serverSocket) + 
                            "e porta "+ 
                            handler.getPorta(serverSocket));
        
        System.out.println("Recebendo conexoes...");
        while(true)
        {
            Socket client = serverSocket.accept();
            System.out.println("Conexao obtida de IP "+handler.getEnderecoIP(client)+" e porta "+handler.getPorta(client));
            new Thread(new GenericServerRunnable(client)).start();
        }
    }

    /**
     * Obtem a porta de diretorio de arquivos
     * @return 
     */
    public String getDiretorioArquivos()
    {
        return this.diretorioArquivos;
    }
    // </editor-fold>

    // <editor-fold defaultstate="collapsed" desc="Classe privada cliente">
    /**
     * Implementa o que a thread do cliente irá executar.
     */
    private class GenericServerRunnable implements Runnable 
    {
        private Socket client;
        
        public GenericServerRunnable(Socket client)
        {
            this.client = client;
        }
        
        @Override
        public void run() {
            HttpSocketHandler handler = HttpSocketHandler.getInstance();

            try {
                //le requisicao do cliente
                String mensagem = handler.readAllMessage(client);
                //criando objeto de requisicao
                RequisicaoSocket requisicao = new RequisicaoSocket(this.hashCode(),
                                                       mensagem,
                                                       handler.getEnderecoIP(client),
                                                       handler.getPorta(client));
                //executa servico especificado
                String resposta = performService(requisicao);
                //envia resposta ao cliente
                handler.sendAllMessage(client, resposta);
            } catch (IOException ex) {
                //Logger.getLogger(GenericServer.class.getName()).log(Level.SEVERE, null, ex);
            }
            
        }
        
    }
    
    // </editor-fold>
    
    // <editor-fold defaultstate="collapsed" desc="Método template">
    /**
     * Executa um serviço para a classe que herdar de GenericServer através de
 uma requisição recebida pelo cliente.
     * Através da mensagem recebida pelo cliente, este método executará o protocolo especificado
     * devolvendo a resposta a ser enviada para o cliente
     * @param requisicao
     * @return 
     */
    protected abstract String performService(RequisicaoSocket requisicao);
    // </editor-fold>
    
}
