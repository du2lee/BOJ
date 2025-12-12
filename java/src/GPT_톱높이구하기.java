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

        int low = 1;
        int high = arr[N - 1];

        int answer = 0;

        while(low <= high){
            int mid = (low + high) / 2;
            if(check(arr, mid, M)){
                answer = Math.max(mid, answer);
                low = mid + 1;
            } else {
                high = mid - 1;
            }   
        }
        System.out.println(answer);
    }

    static boolean check(int[] arr, int h, int M){
        int length = 0;

        for(int tree : arr){
            int cache = tree - h;
            if(cache < 0)
                cache = 0;
            length += cache;
        }
        return length >= M;
    }
}
