/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package httplibrary.util;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * Métodos úteis para manipulação de sockets
 * @author Ferreira
 */
public class HttpSocketHandler {
    
    // <editor-fold defaultstate="collapsed" desc="Singleton">
    private static HttpSocketHandler instance;
    
    public static HttpSocketHandler getInstance()
    {
        if(instance == null)
            instance = new HttpSocketHandler();
        
        return instance;
    }
    // </editor-fold>
    
    // <editor-fold defaultstate="collapsed" desc="Metodos">
    /**
     * Obtem o endereco IP
     * @param socket
     * @return obtem endereco IP
     */
    public String getEnderecoIP(Socket socket)
    {
        return socket.getInetAddress().getHostName();
    }
    
    
    /**
     * Obtem o endereco IP
     * @param socket
     * @return obtem endereco IP
     */
    public String getEnderecoIP(ServerSocket socket)
    {
        return socket.getInetAddress().getHostName();
    }
    
    /**
     * Obtem a porta a ser utilizada
     * @param socket
     * @return 
     */
    public int getPorta(Socket socket)
    {
        return socket.getPort();
    }

    /**
     * Obtem a porta a ser utilizada
     * @param socket
     * @return 
     */
    public int getPorta(ServerSocket socket)
    {
        return socket.getLocalPort();
    }
    // </editor-fold>
    
    /**
     * Envia uma mensagem completa via socket.
     * @param socket
     * @param message
     * @return true se sucesso e false se fracasso
     */
    public boolean sendAllMessage(Socket socket, String message)
    {
        try {
            //recuperando stream
            OutputStream out = socket.getOutputStream();
            out.write(message.getBytes());
            /*
            
            //tamanho do buffer do stream
            int buffer = socket.getSendBufferSize();
            //tamanho da mensagem
            int tamanho = message.getBytes().length;
            //offset para a leitura
            int offset = 0;
            
            //escreve no servidor os bytes da mensagem enviando ao poucos 
            //respeitando o tamanho do buffer
            do
            {
                if(tamanho < buffer)
                    out.write(message.getBytes(), offset, (tamanho - offset));
                else
                    out.write(message.getBytes(), offset, buffer);
                
                
                out.flush();
                offset += buffer;
            }while(offset < tamanho);
            */
            
        } catch (IOException ex) {
            return false;
        }
        
        return true;
    }
    
    /**
     * Recebe a mensagem de um socket
     * @param socket
     * @return 
     */
    public String readAllMessage(Socket socket) throws IOException
    {
        //classe builder, onde concatena diversas strings inseridas em sequencia
        StringBuilder builder = new StringBuilder();
        //tamanho do buffer do stream
        InputStream in = socket.getInputStream();
        //tamanho do buffer
        int buffer = socket.getReceiveBufferSize();
        //vetor de bytes que será lido do stream
        byte[] bytes = new byte[buffer];
        //le do stream e guarda bytes
        in.read(bytes);
        //retorna variavel
        return new String(bytes);
        /*
        //tamanho do buffer
        int buffer = socket.getReceiveBufferSize();
        //vetor de bytes que será lido do stream
        byte[] bytes = new byte[buffer];
        //offset inicial para leitura
        int offset = 0;
        //a leitura é realizada e valor armazenado em 'bytes'.
        //in.read(..) retorna -1 se não existe mais nada a ser lido
        while(in.read(bytes, offset, buffer) != -1)
        {
            builder.append(new String(bytes));
            offset += buffer;
        }
        */
        
    }
}
