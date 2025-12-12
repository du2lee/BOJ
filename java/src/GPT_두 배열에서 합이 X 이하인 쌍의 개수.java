import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner();

        int N = fs.nextInt();
        int M = fs.nextInt();
        int X = fs.nextInt();

        int[] A = new int[N];
        int[] B = new int[M];

        for(int i = 0; i < N; i++)
            A[i] = fs.nextInt();

        for(int i = 0; i < M; i++)
            B[i] = fs.nextInt();

        Arrays.sort(A);
        Arrays.sort(B);

        int left = 0;
        int right = M - 1;
        int answer = 0;

        while(left < N && right >= 0){

            if(A[left] + B[right] <= X){
                answer += (right + 1);
                left++;
            } else
                right--;
        }
        System.out.println(answer);
    }
}