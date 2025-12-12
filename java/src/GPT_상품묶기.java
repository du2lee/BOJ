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

        Arrays.sort(arr, (x, y) -> {
            return Integer.compare(y, x);
        });

        int answer = 0;

        for(int i = 0; i < N; i++){
            if(i % 3 == 2)
                continue;
            answer += arr[i];
        }

        System.out.println(answer);

    }
}
