package edu.bvu.plc;

import java.util.ArrayList;
import java.util.Scanner;

public class REPL {

    public Integer eval(AST t) {
        if (t.param.equals("*"))
        {
            return this.eval(t.left) * this.eval(t.right);
        }
        else if (t.param.equals("+"))
        {
            return this.eval(t.left) + this.eval(t.right);
        }
        else if (t.param.equals("-"))
        {
            return this.eval(t.left) - this.eval(t.right);
        }
        else
            return (Integer) t.param;
    }

    /**
     * Read-eval-print loop.
     * Repeatedly asks for expressions, tokenizes them, parses them,
     * and evaluates the expression to print a result.
     */
    public static void main(String[] args) {
        REPL repl = new REPL();
        Lexer lexer = new Lexer();
        Parser parser = new Parser();
        Scanner in = new Scanner(System.in);
        System.out.print("> ");
        String s = in.nextLine();
        while (!s.equals("")) {
            ArrayList<Token> tokens = lexer.lex(s);
            AST ast = parser.parse(tokens);
            System.out.println(repl.eval(ast));
            System.out.print("> ");
            s = in.nextLine();
        }
        System.out.println("\nBye!");
    }
}
