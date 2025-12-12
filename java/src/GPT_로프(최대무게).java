import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner();

        int N = fs.nextInt();
        Integer[] arr = new Integer[N];

        for(int i = 0; i < N; i++)
            arr[i] = fs.nextInt();

        Arrays.sort(arr);

        int weight = 0;

        for(int i = 0; i < N; i++){
            int cache = arr[i] * (N - i);
            if(cache > weight)
                weight = cache;
        }

        System.out.println(weight);
    }
}
