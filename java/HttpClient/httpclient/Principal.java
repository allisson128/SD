package httpclient;

import java.io.IOException;
import java.net.Socket;
import httplibrary.util.HttpSocketHandler;
/**
 * Classe principal onde verifica os argumentos e inicia aplicação cliente.
 */
public class Principal {
    public static void main(String args[]) throws IOException
    {
        String host = "127.0.0.1";
        int porta = 5000;
        
        try {
            HttpSocketHandler handler = HttpSocketHandler.getInstance();
            Socket socket = new Socket(host, porta);
            System.out.println("Iniciado conexao com cliente para servidor de IP: "+ host + " e porta "+ porta);
            
            handler.sendAllMessage(socket, "ENVIANDO MENSAGEM AO SERVIDOR: ");
            String resposta = handler.readAllMessage(socket);
            System.out.println("SERVIDOR: " + resposta);
            
        } catch (IOException ex) {
            System.out.println("Erro ao criar socket: " + ex.getMessage());
        }
        
            
    }
}
