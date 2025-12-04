import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner();

        int n = fs.nextInt();
        List<Integer> list = new ArrayList<> ();

        int[] arr2 = new int[n];

        for(int i = 0; i < n; i++){
            int cache = fs.nextInt();
            list.add(cache);
            arr2[i] = cache;
        }

        list.sort((x, y) -> { return Integer.compare(x, y);});

        HashMap<Integer, Integer> map = new HashMap<>();

        int rank = 0;

        for(int i = 0; i < n; i++){
            int key = list.get(i);
            if(map.get(key) == null){
                map.put(key, rank);
                rank += 1;
            }
                
        }

        for(int i = 0; i < n; i++){
            System.out.print(String.valueOf(map.get(arr2[i])) + " ");
        }
    }
}

