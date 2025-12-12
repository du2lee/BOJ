import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner();

        int N = fs.nextInt();
        int M = fs.nextInt();

        int[] arr = new int[N];

        for(int i = 0; i < N; i++)
            arr[i] = fs.nextInt();

        Arrays.sort(arr);

        int left = 0;
        int right = 0;
        long answer = 2000000001;

        while(right < N){
            int value = arr[right];
            right++;

            while(left < right && value - arr[left] >= M){
                answer = Math.min(answer, value - arr[left]);
                left++;
            }

        }

        System.out.println(answer);

    }
}
