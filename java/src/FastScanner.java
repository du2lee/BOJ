import java.io.*;
import java.util.*;

class FastScanner {
    BufferedReader br;
    StringTokenizer st;

    public FastScanner(){
        br = new BufferedReader(new InputStreamReader(System.in));
    }

    String next() throws IOException {
        if(st == null || !st.hasMoreTokens())
            st = new StringTokenizer(br.readLine());

        return st.nextToken();
    }

    int nextInt() throws IOException {
        return Integer.parseInt(next());
    }

    long nextLong() throws IOException {
        return Long.parseLong(next());
    }

    double nextDouble() throws IOException {
        return Double.parseDouble(next());
    }

    String nextLine() throws IOException {
        return br.readLine();
    }
}