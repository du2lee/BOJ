import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();

        int N = fs.nextInt();
        int[][] arr = new int[N][2];

        for(int i = 0; i < N; i++){
            arr[i][0] = fs.nextInt();
            arr[i][1] = fs.nextInt();
        }

        Arrays.sort(arr, (x, y) -> {
            if(x[1] == y[1])
                return Integer.compare(x[0], y[0]);
            return Integer.compare(x[1], y[1]);
        });

        int answer = 0;
        int hour = 0;

        for(int[] a : arr){
            if(a[0] >= hour){
                hour = a[1];
                answer += 1;
            }
        }
        System.out.println(answer);
    }
}
