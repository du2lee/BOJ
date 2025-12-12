import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner();

        int N = fs.nextInt();
        int C = fs.nextInt();

        int[] arr = new int[N];

        for(int i = 0; i < N ; i++)
            arr[i] = fs.nextInt();

        Arrays.sort(arr);

        int low = 1;
        int high = arr[N - 1] - arr[0];
        int answer = 0;

        while(low <= high){
            int mid = (low + high) / 2;

            if(check(arr, N, mid, C)){
                answer = mid;
                low = mid + 1;
            } else
                high = mid - 1;
        }
        
        System.out.println(answer);
    }


    static boolean check(int[] arr, int N, int d, int C){
        int count = 1;
        int last = arr[0];

        for(int i = 1; i < N; i++){
            if(arr[i] - last >= d){
                count++;
                last = arr[i];
            }
        }

        return count >= C;

    }
}
