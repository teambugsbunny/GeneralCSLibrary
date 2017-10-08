import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// The part of the program involving reading from STDIN and writing to STDOUT has been provided by us.
public class Solution {

    public static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    public static int lcm(int a, int b) {
        return a * (b/gcd(a,b)); 
    }

    public static boolean subset(int[] numbers) {
        for (int i = 1; i < numbers.length; i++) {
            numbers[i] = gcd(numbers[i - 1], numbers[i]);
            if (gcd(numbers[i - 1], numbers[i]) == 1) {
                return true;
            }
        }
        return false;
    }
