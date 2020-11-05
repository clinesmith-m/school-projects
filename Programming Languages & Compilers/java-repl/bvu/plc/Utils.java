package edu.bvu.plc;

public class Utils {
    public static void barf(String msg) {
        System.err.println("Error: " + msg);
        System.exit(1);
    }
}
