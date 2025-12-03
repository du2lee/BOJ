import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner();

        int N = fs.nextInt();

        int[][] arr = new int[N][2];

        for(int i = 0; i < N; i++){
            arr[i][0] =  fs.nextInt();
            arr[i][1] =  fs.nextInt();
        }

        Arrays.sort(arr, (x,y) -> {return Integer.compare(x[0], y[0]);});

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        pq.add(arr[0][1]);

        for(int i = 1; i < N; i++){
            if(pq.peek() <= arr[i][0])
                pq.poll();

            pq.add(arr[i][1]);
        }

        System.out.println(pq.size());

    }
}