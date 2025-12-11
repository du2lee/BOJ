import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner();

        int N = fs.nextInt();
        int[] arr = new int[N];

        for(int i = 0; i < N; i++)
            arr[i] = fs.nextInt();

        int K = fs.nextInt();

        int left = 0;
        int right = 0;
        int answer = 0;
        int answerleft = 0;
        int answerright = 0;


        HashMap<Integer, Integer> map = new HashMap<>();
        int distict = 0;

        while(right < N){
            // 오른쪽 올리기
            map.put(arr[right], map.getOrDefault(arr[right], 0) + 1);
            if(map.get(arr[right]) == 1)
                distict++;
            right++;

            // 왼쪽 올리기
            while(distict > K && left < right){
                map.put(arr[left], map.get(arr[left]) - 1);
                if(map.get(arr[left]) < 1)
                    distict--;
                left++;
            }

            int cache = right - left;

            // 값 비교
            if(answer < cache) {
                answer = cache;
                answerleft = left;
                answerright =right;
            }
        }

        System.out.println(answer);

        for(int i = answerleft; i < answerright; i++)
            System.out.printf("%d ", arr[i]);
    }
}
