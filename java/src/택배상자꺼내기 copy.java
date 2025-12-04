import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner();

        int n = fs.nextInt();
        int[][] arr = new int[n * 2][2];

        for(int i = 0; i < 2*n; i+=2){
            // 시작
            arr[i][0] = fs.nextInt();
            arr[i][1] = 1;

            // 끝
            arr[i+1][0] = fs.nextInt();
            arr[i+1][1] = -1;
        }

        Arrays.sort(arr, (x, y) -> {
            if(x[0] == y[0])
                return Integer.compare(x[1], y[1]);
            return Integer.compare(x[0], y[0]);
        });

        int count = 0;
        int max = 0;

        for(int[] a : arr){
            count += a[1];
            if(count > max)
                max = count;
        }

        System.out.println(max);

    }
}