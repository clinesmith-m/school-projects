package edu.bvu.plc;

import java.util.ArrayList;

public class Parser {
    // My code starts here
    public AST F(ArrayList<Token> tokens) {
        if (tokens.size() == 0)
            Utils.barf("Premature end of expression");

        Token token = tokens.remove(0);

        // Making sure there a legit value for F
        if (!token.tid.equals(Token.TID.NUM)
            && !token.tid.equals(Token.TID.ID)
            && !token.tid.equals(Token.TID.LPAREN))
        {
           Utils.barf("Expected ID, number or parenthetical expression, got '"
                        + token.text + "'");
        }
        else if (token.tid.equals(Token.TID.NUM))
        {
            Integer newInt = Integer.parseInt(token.text);
            return new AST(newInt, null, null);
        }
        else if (token.tid.equals(Token.TID.ID))
        {
            Utils.barf("ID's are currently unsupported: " + token.text);
        }
        else if (token.tid.equals(Token.TID.LPAREN))
        {
            AST childAST = this.E(tokens);

            if (tokens.size() == 0)
                Utils.barf("Premature end of expression");

            Token rpcheck = tokens.remove(0);
            if (!rpcheck.tid.equals(Token.TID.RPAREN))
                Utils.barf("Expected ')', got '" + rpcheck.text + "'");

            return childAST;
        }

        System.out.println("If this ever runs, something's wrong");
        return null;
    }

    public AST RestT(ArrayList<Token> tokens) {
        if (tokens.size() == 0)
            return null;

        Token token = tokens.get(0);

        // Return empty if it isn't a multiplier
        if (!token.tid.equals(Token.TID.MULT))
            return null;

        // Removing the MULT token and making the AST node
        tokens.remove(0);
        String opString = token.text;
        AST opNode = new AST(opString);

        // Making the children for the opnode
        AST Fthing = this.F(tokens);
        AST RestTthing = this.RestT(tokens);

        // If there isn't another MULT token next, then the F token needs to be
        // the right child so that it can be multiplied with the F token to the
        // left of the multiplier
        if (RestTthing == null)
        {
            opNode.right = Fthing;
            return opNode;
        }

        RestTthing.left = Fthing;
        opNode.right = RestTthing;
        return opNode;
    }

    public AST T(ArrayList<Token> tokens) {
        if (tokens.size() == 0)
            Utils.barf("Premature end of expression");

        Token token = tokens.get(0);

        AST Fthing = this.F(tokens);
        AST RestTthing = this.RestT(tokens);

        if (RestTthing == null)
            return Fthing;

        RestTthing.left = Fthing;
        return RestTthing;
    }

    public AST RestE(ArrayList<Token> tokens) {
        if (tokens.size() == 0)
            return null;

        Token token = tokens.get(0);

        if (!token.tid.equals(Token.TID.PLUS)
            && !token.tid.equals(Token.TID.MINUS))
        {
            return null;
        }

        tokens.remove(0);
        String opString = token.text;
        AST opNode = new AST(opString);

        AST Tthing = this.T(tokens);
        AST RestEthing = this.RestE(tokens);

        if (RestEthing == null)
        {
            opNode.right = Tthing;
            return opNode;
        }

        RestEthing.left = Tthing;
        opNode.right = RestEthing;
        return opNode;
    }

    public AST E(ArrayList<Token> tokens) {
        if (tokens.size() == 0)
            Utils.barf("Premature end of expression");

        Token token = tokens.get(0);

        AST Tthing = this.T(tokens);
        AST RestEthing = this.RestE(tokens);

        if (RestEthing == null)
            return Tthing;

        RestEthing.left = Tthing;
        return RestEthing;
    }
    // And ends here

    /**
     * Consume tokens and generate AST.
     * 'tokens' is a list reference, so we can pop from the front
     * as we consume the tokens.
     */
    public AST parse(ArrayList<Token> tokens) {
        AST ast = E(tokens);

        if (tokens.size() > 0)
            Utils.barf("Extra symbols found at end of expression");
    
        return ast;
    }
}

