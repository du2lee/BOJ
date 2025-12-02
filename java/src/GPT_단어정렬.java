import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();

        int n = fs.nextInt();

        Set<String> set = new HashSet<>();

        for(int i = 0; i < n; i++)
            set.add(fs.next());

        List<String> list = new ArrayList<>(set);

        list.sort((x, y) ->{
            if(x.length() == y.length())
                return x.compareTo(y);
            return Integer.compare(x.length(), y. length());
        });

        for(String s : list)
            System.out.println(s);

    }
}
