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

        int M = fs.nextInt();

        Arrays.sort(arr);

        System.out.println(upper_binary(arr, N, M));
    }


    static int upper_binary(int[] arr, int N, int M){
        int left = 0;
        int right = arr[N - 1];
        int answer = 0;

        while(left <= right){
            int mid = (left + right) / 2;
            int cache = 0;

            for(int money : arr){
                cache += Math.min(money, mid);
            }
            
            if(cache > M)
                right = mid - 1;
            else{
                answer = mid;
                left = mid + 1;
            }
        }
        return answer;
    }
}
