import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();

        int n = fs.nextInt();
        int[][] arr = new int[n][2];

        for(int i = 0; i < n; i++){
            arr[i][0] = fs.nextInt();
            arr[i][1] = fs.nextInt();
        }

        Arrays.sort(arr, (x, y) -> {
            if(x[1] == y[1])
                return Integer.compare(x[0], y[0]);
            return Integer.compare(x[1], y[1]);
        });

        int time = 0;
        int answer = 0;

        for(int[] t : arr){
            if(time <= t[0]){
                time = t[1];
                answer += 1;
            }
        }

        System.out.println(answer);
    }
}