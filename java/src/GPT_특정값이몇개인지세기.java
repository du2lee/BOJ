import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();

        int N = fs.nextInt();
        Integer[] arr = new Integer[N];

        for(int i = 0 ; i < N; i++)
            arr[i] = fs.nextInt();

        Arrays.sort(arr, (x, y) -> { return Integer.compare(x, y);});

        int Q = fs.nextInt();
        for(int i = 0; i < Q; i ++){
            int query = fs.nextInt();
            int upper = upper_binary(arr, query, N);
            int lower = lower_binary(arr, query, N);

            System.out.println(upper - lower);
        }


    }

    static int upper_binary(Integer[] arr, int query, int N){

        int left = 0;
        int right = N - 1;

        while(left <= right){
            int mid = (left + right) / 2;

            if(arr[mid] <= query){
                left = mid + 1;
            } else{
                right = mid - 1;
            }
        }
        return left;
    }

    static int lower_binary(Integer[] arr, int query, int N){

        int left = 0;
        int right = N - 1;

        while(left <= right){
            int mid = (left + right) / 2;

            if(arr[mid] < query){
                left = mid + 1;
            } else{
                right = mid - 1;
            }
        }
        return left;
    }
}
