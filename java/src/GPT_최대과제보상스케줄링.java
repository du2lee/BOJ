import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner();

        int N = fs.nextInt();
        int[][] arr = new int[N][2];

        for(int i = 0; i < N; i++){
            arr[i][0] = fs.nextInt();
            arr[i][1] = fs.nextInt();
        }

        Arrays.sort(arr, (x, y) -> {
            if(x[0] == y[0])
                return Integer.compare(y[1], x[1]);
            return Integer.compare(x[0], y[0]);
        });


        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for(int[] a : arr){
            int d = a[0];
            int p = a[1];

            pq.add(p);

            if(pq.size() > d)
                pq.poll();
        }

        int answer = 0;

        for(int a: pq)
            answer += a;

        System.out.println(answer);

    }
}
