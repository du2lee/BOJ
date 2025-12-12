import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();

        int N = fs.nextInt();
        int[] arr = new int[N];

        for(int i = 0;i < N ;i++){
            arr[i] = fs.nextInt();
        }

        int S = fs.nextInt();

        int left = 0;
        int right = 0;

        int sum = 0;
        int answer = 100001;

        while(right < N){
            sum += arr[right];
            right++;

            while(sum >= S){
                answer = Math.min(answer,right - left);
                sum -= arr[left];
                left++;
            }

        }
        if(answer == 100001)
            System.out.println(0);
        else
            System.out.println(answer);
    }
}
