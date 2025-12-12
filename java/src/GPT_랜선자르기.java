import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner();

        int K = fs.nextInt();
        int N = fs.nextInt();
        int[] arr = new int[K];

        for(int i = 0; i < K; i++)
            arr[i] = fs.nextInt();

        Arrays.sort(arr);

        int low = 1;
        int high = arr[K - 1];
        long answer = 0;

        while(low <= high){
            int mid = (low + high) / 2;

            if(check(arr, mid, N)){
                answer = mid;
                low = mid + 1;
            } else
                high = mid - 1;
        }

        System.out.println(answer);
    }

    static boolean check(int[] arr, int d, int N){
        long count = 0;

        for(int stick : arr)
            count += stick / d;

        return count >= N;
    }

}
