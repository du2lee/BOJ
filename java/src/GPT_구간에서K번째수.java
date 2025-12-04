import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();

        int N = fs.nextInt();
        int[] arr = new int[N];

        for(int i = 0; i < N; i++)
            arr[i] = fs.nextInt();

        int Q = fs.nextInt();
        for(int i = 0; i < Q; i++){
            int L = fs.nextInt();
            int R = fs.nextInt();
            int K = fs.nextInt();
            int[] cache = Arrays.copyOfRange(arr, L - 1, R);
            Arrays.sort(cache);
            System.out.println(cache[K - 1]);
        }

    }
}