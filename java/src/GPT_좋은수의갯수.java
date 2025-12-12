import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();

        int N = fs.nextInt();
        Integer[] arr = new Integer[N];

        for(int i = 0; i < N; i++)
            arr[i] = fs.nextInt();

        Arrays.sort(arr);

        int answer = 0;

        for(int i = 0; i < N; i++){
            int left = 0;
            int right = N - 1;
            int target = arr[i];

            while(left < right){
                if(left == i){
                    left++;
                    continue;
                }

                if(right == i){
                    right--;
                    continue;
                }
                    
                int cache = arr[left] + arr[right];

                if(cache == target){
                    answer += 1;
                    break;
                } else if(cache > target)
                    right--;
                else
                    left++;
            }
        }
        System.out.println(answer);
    }
}
