import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();

        int n = fs.nextInt();

        PriorityQueue<Integer> pq = new PriorityQueue<>((x, y)->{
            if(Math.abs(x) == Math.abs(y))
                return Integer.compare(x, y);
            return Integer.compare(Math.abs(x), Math.abs(y));
        });

        for(int i = 0; i < n; i++){
            int input = fs.nextInt();
            if(input == 0){
                if(pq.size() == 0)
                    System.out.println(0);
                else
                    System.out.println(pq.poll());
            } else {
                pq.add(input);
            }


        }
    }
}