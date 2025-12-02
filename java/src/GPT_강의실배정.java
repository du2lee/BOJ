import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();

        int n = fs.nextInt();

        List<Integer[]> list = new ArrayList<>();

        for(int i =0; i<n; i++){
            list.add(new Integer[]{fs.nextInt(), fs.nextInt()});
        }


        list.sort((x, y) -> {
            int flag = Integer.compare(x[1], y[1]);
            if(flag !=0) return flag;
            return Integer.compare(x[0], y[0]);
        });

        int end = 0;
        int answer = 0;

        for(Integer[] x : list){
            if(x[1] >= end && x[0] >= end){
                end = x[1];
                answer += 1;
            }
        }
        System.out.println(answer);
    }
}