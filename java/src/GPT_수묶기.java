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

        Arrays.sort(arr, (x, y) -> {return Integer.compare(y, x); });

        int first = 0;
        boolean zeroFlag = false;
        int answer = 0;
        int idx = N;
        

        // 음수는 처리 X
        for(int i = 0; i < N; i++){
            int cache = arr[i];
            if(cache < 0){
                idx = i;
                break;
            }

            if(cache == 1){
                answer += cache;
                continue;
            }

            if(cache == 0){
                zeroFlag = true;
                continue;
            }

            if(first != 0){
                answer += (first * cache);
                first = 0;
                continue;
            }

            first = cache;
        }

        // 양수가 홀수 개
        answer += first;
        first = 0;

        // 음수처리
        for(int i = N - 1; i >= idx; i--){
            int cache = arr[i];
            if(first != 0){
                answer += (first * cache);
                first = 0;
                continue;
            }

            first = cache;
        }

        // 남은 음수 처리
        if(!zeroFlag)
            answer += first;

        System.out.println(answer);
    }
}