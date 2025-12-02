import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();

        int n = fs.nextInt();
        Integer[] arr = new Integer[n];

        for(int i = 0; i<n; i++){
            arr[i] = fs.nextInt();
        }

        Arrays.sort(arr, (x, y) -> {
            if(Math.abs(x) == Math.abs(y))
                return Integer.compare(x, y);
            return Integer.compare(Math.abs(x), Math.abs(y));
        });

        for(int i = 0; i < n; i++){
            System.out.print(arr[i] + " ");
        }
    }
}
