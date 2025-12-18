import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {

    static int MAX = 100000;
    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner();

        int[] dist = new int[MAX + 1];

        Arrays.fill(dist, -1);

        int N = fs.nextInt();
        int K = fs.nextInt();

        ArrayDeque<Integer[]> q = new ArrayDeque<>();

        q.add(new Integer[]{N, 0});

        dist[N] = 0;

        while(!q.isEmpty()){
            Integer[] arr = q.poll();

            if(arr[0] == K){
                System.out.println(arr[1]);
                return;
            }

            // 2배
            if(dist[arr[0] * 2] == -1 && arr[0] * 2 <= MAX){
                q.addFirst(new Integer[]{arr[0] * 2 ,arr[1]});
                dist[arr[0] * 2] = arr[1];
            }
                
            // 1 더하기
            if(dist[arr[0] + 1] == -1  && arr[0] + 1 <= MAX){
                q.addLast(new Integer[]{arr[0] + 1, arr[1] + 1});
                dist[arr[0] + 1] = arr[1]+ 1;
            }
                
            // 1 빼기
            if(dist[arr[0] - 1] == -1 && arr[0] - 1 >= 0){
                q.addLast(new Integer[]{arr[0] - 1 ,arr[1] + 1});
                dist[arr[0] -1] = arr[1] + 1;
            }
        }
    }
}