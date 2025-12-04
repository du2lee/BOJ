import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner();

        int n = fs.nextInt();
        Integer[] arr = new Integer[n];
        for(int i = 0; i < n; i++)
            arr[i] = fs.nextInt();

        int m = fs.nextInt();
        Integer[] arrM = new Integer[m];
        for(int i = 0; i < m; i++)
            arrM[i] = fs.nextInt();

        int goal = fs.nextInt();

        Arrays.sort(arr);
        Arrays.sort(arrM, (x, y) -> {return Integer.compare(y, x); });

        int answer = 0;

        int nIdx = 0;
        int mIdx = 0;

        while(nIdx < n && mIdx < m){
            int cache = arr[nIdx] + arrM[mIdx];
            if(cache == goal){
                int nCount = 1;
                int mCount = 1;
                for(int j = nIdx + 1; j < n; j++){
                    if(!arr[nIdx].equals(arr[j]))
                        break;
                    nCount++;
                }

                for(int j = mIdx + 1; j < m; j++){
                    if(!arrM[mIdx].equals(arrM[j]))
                        break;
                    mCount++;
                }
                answer += nCount * mCount;
                nIdx += nCount;
                mIdx += mCount;
                continue;
            }

            if(cache < goal){
                nIdx += 1;
                continue;
            }

            mIdx += 1;

        }

        System.out.println(answer);
    }
}
