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

        Arrays.sort(arr);

        int Q = fs.nextInt();

        for(int i = 0 ; i < Q; i++){
            int A = fs.nextInt();

            System.out.println(lower_binary(arr,A,N));
        }
    }

    static int lower_binary(int[] arr, int A, int N){
        int left = 0;
        int right = N - 1;
        int answer = -1;

        while(left <= right){
            int mid = (left + right) / 2;

            if(arr[mid] < A)
                left = mid + 1;
            else{
                answer = arr[mid];
                right = mid - 1;
            }
                
        }

        return answer;
    }
}