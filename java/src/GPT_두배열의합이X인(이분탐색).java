import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner();

        int n = fs.nextInt();
        int[] A = new int[n];
        for(int i = 0; i < n; i++)
            A[i] = fs.nextInt();

        int m = fs.nextInt();
        int[] B = new int[m];
        for(int i = 0; i < m; i++)
            B[i] = fs.nextInt();

        int goal = fs.nextInt();

        Arrays.sort(A);
        Arrays.sort(B);

        int answer = 0;

        for(int a : A){
            int b = goal - a;

            int small = lowerBinarySearch(B, b);
            int big = apperBinarySearch(B, b);

            answer += big - small;
        }

        System.out.println(answer);
    }


    static int lowerBinarySearch(int[] arr, int v){
        int left = 0;
        int right = arr.length;

        while(left < right){
            int mid = (left + right) / 2;

            if(arr[mid] >= v) right = mid;
            else left = mid + 1;
        }
        return left;
    }

        static int apperBinarySearch(int[] arr, int v){
        int left = 0;
        int right = arr.length;

        while(left < right){
            int mid = (left + right) / 2;

            if(arr[mid] > v) right = mid;
            else left = mid + 1;
        }
        return left;
    }
    
}
