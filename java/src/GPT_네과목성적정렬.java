import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();

        int n = fs.nextInt();

        List<Student> list = new ArrayList<>();

        for(int i = 0; i < n; i++){
            Student s = new Student(fs.next(), fs.nextInt(), fs.nextInt(), fs.nextInt());
            list.add(s);
        }

        list.sort((x,y)->{
            if(y.getKor() == x.getKor()){
                if(x.getEng() == y.getEng()){
                    if(x.getMath() == y.getMath())
                        return x.getName().compareTo(y.getName());
                    return Integer.compare(y.getMath(), x.getMath());
                }
                return Integer.compare(x.getEng(), y.getEng());
            }
            return Integer.compare(y.getKor(), x.getKor());
        });

        for(int i = 0; i< list.size(); i++){
            System.out.print(list.get(i).getName() + " ");
            System.out.print(list.get(i).getKor() + " ");
            System.out.print(list.get(i).getEng() + " ");
            System.out.println(list.get(i).getMath());
        }
    }
}

class Student{
    String name;
    int kor;
    int eng;
    int math;

    public Student(String name, int kor, int eng, int math){
        this.name = name;
        this.kor = kor;
        this.eng = eng;
        this.math = math;
    }

    public String getName(){
        return name;
    }

    public int getKor(){
        return kor;
    }

    public int getEng(){
        return eng;
    }

    public int getMath(){
        return math;
    }
}
