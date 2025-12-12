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

        int wait = 0;
        int answer = 0;

        for(int a: arr){
            answer += wait; // 웨이팅시간
            answer += a;    // 작업시간
            wait += a;      // 웨이팅시간 추가해주기
        }

        System.out.println(answer);

    }
}
