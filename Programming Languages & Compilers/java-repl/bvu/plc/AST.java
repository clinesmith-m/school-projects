package edu.bvu.plc;

import java.util.ArrayList;

/**
 * This class is an abstract syntax tree node in our
 * integer-only arithmetic language.  Operators supported
 * are +, -, and *.
 */
public class AST {
    public Object param;
    public AST left;
    public AST right;

    public AST(Object param) {
        this(param, null, null);
    }

    public AST(Object param, AST left, AST right) {
        this.param = param;
        this.left = left;
        this.right = right;
    }

    public static Object eval(AST t) {
        if (t.left != null)
            System.out.println(eval(t.left));
        if (t.right != null)
            System.out.println(eval(t.right));
        return t.param;
    }

    /**
     * This is a silly test method for the AST class.
     * Other classes will use the class def and methods
     * for AST but will never call this method directly.
     */
    public static void main(String[] args) {
        // Build two simple trees.
        AST tSimple = new AST(3);
        AST tAdd = new AST("+", new AST(1), new AST(3));

        // Build a tree one way.
        AST tMult = new AST("*",
                            new AST(1),
                            new AST("+",
                                    new AST(2),
                                    new AST(3)));

        // Build a tree another way.
        AST tMult2 = new AST("*");
        tMult2.left = new AST("+", new AST(1), new AST(1));
        tMult2.right = new AST("+", new AST(1), new AST(2));

        // Throw the trees in a list and eval them all.
        ArrayList<AST> ts = new ArrayList<AST>();
        ts.add(tSimple);
        ts.add(tAdd);
        ts.add(tMult);
        ts.add(tMult2);

        for (AST t : ts) {
            System.out.println(AST.eval(t));
        }
    }
}
