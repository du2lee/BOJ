import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner();

        int N = fs.nextInt();

        int[] arr = new int[N];

        for(int i = 0; i < N; i++){
            arr[i] = fs.nextInt();
        }

        int X = fs.nextInt();

        int left = 0;
        int right = 0;
        int sum = 0;
        int answer = 0;
        int answerLeft = 0;
        int answerRight = 0;

        while(right < N){

            // 오른쪽 포인터 이동
            sum += arr[right];
            right++;

            // 왼쪽 포인터 이동
            while(sum > X && left < right){
                sum -= arr[left];
                left++;
            }

            // 최대 길이 계산
            int len = right - left;
            if(answer < len){
                answer = len;
                answerLeft = left;
                answerRight = right;
            }


        }

        System.out.println(answer);

        for(int i = answerLeft; i < answerRight; i++)
            System.out.printf("%d ", arr[i]);
    }
}
