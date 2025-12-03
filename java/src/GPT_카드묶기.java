import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner();

        int n = fs.nextInt();
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        long cost = 0;

        for(int i = 0; i < n; i++){
            pq.add(fs.nextInt());
        }

        while(true){
            if(pq.size() < 2){
                System.out.println(cost);
                break;
            }

            int a = pq.poll();
            int b = pq.poll();
            cost += a+b;
            pq.add(a+b);
        }
        
    }
}