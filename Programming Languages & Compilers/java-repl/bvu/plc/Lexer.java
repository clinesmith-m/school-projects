package edu.bvu.plc;

import java.util.ArrayList;
import java.util.Scanner;

public class Lexer {
    public ArrayList<Token> lex(String buf) {
        ArrayList<Token> tokens = new ArrayList<Token>();
        buf += " ";

        int i = 0;
        char currChar = buf.charAt(i);
        while (i < buf.length() - 1)
        {
            // First removing white space
            while (currChar == ' ')
            {
                i++;
                if (i == buf.length() - 1) break;
                currChar = buf.charAt(i);
            }

            // Then making tokens
            String currTokenVal = "";
            // Taking in letters the quick and dirty way
            while (Character.isLetter(currChar))
            {
                currTokenVal += currChar;
                i++;
                currChar = buf.charAt(i);
            }
            
            // If this if runs, it means some letters were picked up and a new
            // token needs to be made. It also means currTokenVal needs to be
            // reset to an empty string
            if (!currTokenVal.isEmpty())
            {
                Token newToken = new Token(Token.TID.ID, currTokenVal);
                tokens.add(newToken);
                currTokenVal = "";
            }

            // Repeating the same logic for numbers
            while (Character.isDigit(currChar))
            {
                currTokenVal += currChar;
                i++;
                currChar = buf.charAt(i);
            }

            if (!currTokenVal.isEmpty())
            {
                Token newToken = new Token(Token.TID.NUM, currTokenVal);
                tokens.add(newToken);
                currTokenVal = "";
            }

            // Now looking for all the tokens that are jsut one character
            if (currChar == '+')
            {
                currTokenVal += currChar;
                Token newToken = new Token(Token.TID.PLUS, currTokenVal);
                tokens.add(newToken);

                i++;
                currChar = buf.charAt(i);

                currTokenVal = "";
            }

            if (currChar == '-')
            {
                currTokenVal += currChar;
                Token newToken = new Token(Token.TID.MINUS, currTokenVal);
                tokens.add(newToken);

                i++;
                currChar = buf.charAt(i);

                currTokenVal = "";
            }

            if (currChar == '*')
            {
                currTokenVal += currChar;
                Token newToken = new Token(Token.TID.MULT, currTokenVal);
                tokens.add(newToken);

                i++;
                currChar = buf.charAt(i);

                currTokenVal = "";
            }

            if (currChar == '(')
            {
                currTokenVal += currChar;
                Token newToken = new Token(Token.TID.LPAREN, currTokenVal);
                tokens.add(newToken);

                i++;
                currChar = buf.charAt(i);

                currTokenVal = "";
            }

            if (currChar == ')')
            {
                currTokenVal += currChar;
                Token newToken = new Token(Token.TID.RPAREN, currTokenVal);
                tokens.add(newToken);

                i++;
                currChar = buf.charAt(i);

                currTokenVal = "";
            }

            // Notifying the user of an error if an invalid char is entered
            if (!Character.isLetter(currChar) && !Character.isDigit(currChar)
                && currChar != ' ' && currChar != '+' && currChar != '-'
                && currChar != '*' && currChar != '(' && currChar != ')')
            {
                System.out.println("Error: Illegal character '" 
                                    + currChar + "'");
                break;
            }
        }

        return tokens;
    }

    /**
     * This is a silly test method for the Lexer class.
     * Other classes will use the class def and methods
     * for Lexer but will never call this method directly.
     */
    public static void main(String[] args) {
        Lexer lexer = new Lexer();

        Scanner in = new Scanner(System.in);
        System.out.print("> ");
        String s = in.nextLine();
        while (!s.equals("")) {
            ArrayList<Token> tokens = lexer.lex(s);
            for (Token tok : tokens) {
                System.out.println(tok);
            }

            System.out.print("> ");
            s = in.nextLine();
        }
        System.out.println("\nBye!");
    }
}
