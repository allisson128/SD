package httpserver;

import httplibrary.util.parser.Parser;
import httplibrary.util.parser.ParserException;
import httplibrary.util.parser.ParserFactory;
import httplibrary.util.parser.ParserFactoryEnum;
import httplibrary.util.parser.model.URL;
import httplibrary.util.validador.Validador;
import httplibrary.util.validador.ValidadorException;
import httplibrary.util.validador.ValidadorFactory;
import httplibrary.util.validador.ValidadorFactoryEnum;
import httpserver.server.HttpServer;
import java.io.IOException;


/**
 * Classe responsável por verificar os argumentos do programa e inicializar o servidor
 */
public class Principal {
    
    // <editor-fold defaultstate="collapsed" desc="Atributos estáticos">
    
    private static int porta;
    private static String diretorio = "www";

    // </editor-fold>
    
    // <editor-fold defaultstate="collapsed" desc="Métodos privados de inicialização">
 
    /**
     * Realiza a validaçao do argumentos passados pelo usuario
     * @param args
     * @throws ValidadorException 
     */
    private static void validarArgumentos(String[] args) throws ValidadorException {
        ValidadorFactory factory = ValidadorFactory.getInstance();
        Validador validador = factory.getValidador(ValidadorFactoryEnum.VALIDADOR_ARGUMENTOS_SERVIDOR);
        
        validador.valida(args);
    }

    /**
     * Carrega os argumentos para as variaveis estaticas para inicio do servidor
     * @param args
     * @throws NumberFormatException 
     */
    private static void carregarArgumentos(String[] args) throws NumberFormatException {
        porta = Integer.parseInt(args[0]);
        if(args.length == 2)
            diretorio = args[1];
    }
    
    /**
     * Cria e inicia o servidor. 
     * @throws IOException 
     */
    private static void criarIniciarServidor() throws IOException {
        new HttpServer(porta, diretorio);
    }
    // </editor-fold> 
    
    // <editor-fold defaultstate="collapsed" desc="Método Main">    
    /**
     * @param args os argumentos passados por linha de comando
     */
    public static void main(String[] args) throws ParserException {
        /*
        ParserFactory factory = ParserFactory.getInstance();
        Parser parser = factory.getParser(ParserFactoryEnum.PARSER_URL_FACTORY);
        
        URL url = (URL) parser.parse("http://blog.pengyifan.com/how-to-extend-enum-in-java?nome=lala&email=popo@gmail.com");
        
        System.out.println(url.getHost());
        System.out.println(url.getPorta());
        System.out.println(url.getUrlRelativa());
        System.out.println(url.getParametros());
        */
        try {
            validarArgumentos(args);
            carregarArgumentos(args);
            criarIniciarServidor();
            
        } catch (ValidadorException ex) {
            System.out.println(ex.toString());
            System.exit(1);
        } catch (IOException ex) {
            System.out.println("Falha ao criar socket do servidor\n" + ex.getMessage());
        }
    } 
    // </editor-fold>

}
