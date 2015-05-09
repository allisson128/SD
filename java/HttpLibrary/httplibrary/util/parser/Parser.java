/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package httplibrary.util.parser;

/**
 * Interface para realizar parser
 * @author a11111BCC031
 */
public interface Parser {
    /**
     * Realiza o parser de um objeto, retornando um outro objeto com os valores
     * obtidos
     * @param str a string original
     * @return o objeto com valores obtidos pela analise da string
     * @throws httplibrary.util.parser.ParserException
     */
    public Object parse(String str) throws ParserException;
}
