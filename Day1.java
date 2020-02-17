import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
	
    public static void main(String[] args) {
        int i = 4;
        double d = 4.0;
        String s = "HackerRank ";
		
        Scanner scan = new Scanner(System.in);

        int varInt;
        double varDouble;
        String varString;

        varInt = scan.nextInt();
        varDouble = scan.nextDouble();  
        varString = scan.next();
        varString += scan.nextLine();
        
        System.out.println(varInt+i);
        System.out.println(varDouble+d);

        s = s.concat(varString);
        System.out.println(s);

        scan.close();