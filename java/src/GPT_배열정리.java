import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();
        int n = fs.nextInt();

        List<Student> list = new ArrayList<>();

        for(int i = 0; i< n ; i++)
            list.add(new Student(fs.next(), fs.nextInt()));


        list.sort((x,y)->{
            if(x.getScore() == y.getScore())
                return x.getName().compareTo(y.getName());
            return Integer.compare(y.getScore(), x.getScore());
        });

        for(int i = 0; i< n ; i++){
            Student s = list.get(i);
            System.out.print(s.getName() + " ");
            System.out.println(s.getScore());
        }

    }
}

class Student{
    String name;
    int score;
    public Student(String name, int score){
        this.name = name;
        this.score = score;
    }

    public String getName(){
        return name;
    }

    public int getScore(){
        return score;
    }
}