import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();

        int N = fs.nextInt();
        int[] arr = new int[N];

        int hour = 0;

        for(int i = 0; i < N; i++){
            hour += fs.nextInt();
            arr[i] = hour;
        }

        int Q = fs.nextInt();

        for(int i = 0; i < Q; i++){
            int K = fs.nextInt();
            System.out.println(lower_binary(arr, K, N));
        }

    }

    static int lower_binary(int[] arr, int K, int N){
        int left = 0;
        int right = N - 1;
        int answer = -1;

        while(left <= right){
            int mid = (left + right) / 2;
            if(arr[mid] < K){
                left = mid + 1;
            } else {
                answer = mid;
                right = mid - 1;
            }
        }
        
        if(answer != -1)
            answer++;

        return answer;
    }
}