package edu.bvu.plc;

public class Token {
    public enum TID {
        ID,
        NUM,
        PLUS,
        MINUS,
        MULT,
        LPAREN,
        RPAREN
    }

    public TID tid;
    public String text;

    public Token(TID tid, String text) {
        this.tid = tid;
        this.text = text;
    }

    public String toString() {
        return "(Token: " + this.tid + ", " + this.text + ")";
    }


    /**
     * This is a silly test method for the Token class.
     * Other classes will use the class def and methods
     * for Token but will never call this method directly.
     */
    public static void main(String[] args) {
        System.out.println(new Token(TID.NUM, "34"));
        System.out.println(new Token(TID.PLUS, "+"));
    }
}
