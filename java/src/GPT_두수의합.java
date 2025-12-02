import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();

        int n = fs.nextInt();
        int[] arr = new int[n];

        for(int i = 0; i < n; i++)
            arr[i] = fs.nextInt();

        int v = fs.nextInt();

        Arrays.sort(arr);

        int left = 0;
        int right = n - 1;
        int answer = 0;

        while(left < right){
            int cache = arr[left] + arr[right];
            if(cache == v) {
                answer++;
                left++;
                right--;
            }
            else if(cache < v)
                left++;
            else
                right--;
        }

        System.out.println(answer);

    }
}
