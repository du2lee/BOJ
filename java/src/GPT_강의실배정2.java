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

        List<Integer> rooms = new ArrayList<>();
        rooms.add(0);

        Arrays.sort(arr, (x, y) -> {
            if(x[1] == y[1])
                return Integer.compare(x[0], y[0]);
            return Integer.compare(x[1], y[1]);
        });

        for(int i = 0; i < N; i++){
            boolean flag = true;

            for(int j = 0; j < rooms.size(); j++){
                if(rooms.get(j) <= arr[i][0]){
                    rooms.set(j, arr[i][1]);
                    flag = false;
                    break;
                }
            }

            if(flag){   // 방 추가
                rooms.add(arr[i][1]);
            }
        }

        System.out.println(rooms.size());

    }
}