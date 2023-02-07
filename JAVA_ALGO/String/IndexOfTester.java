import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class IndexOfTester {
    public static void main(String[] args) throws IOException {
        System.out.print("text : ");
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String s1 = bf.readLine();

        System.out.print("pattern : ");
        String s2 = bf.readLine();

        int idx1 = s1.indexOf(s2);
        int idx2 = s1.lastIndexOf(s2);

        if(idx1 == -1)  System.out.println("there is no pattern in text");
        else{
            int len1 = 0;
            for(int i=0;i<idx1;i++){
                len1 += s1.substring(i, i+1).getBytes().length;
            }
            len1 += s2.length();

            int len2 = 0;
            for(int i = 0;i<idx2;i++)
                len2 += s1.substring(i, i+1).getBytes().length;
            len2 += s2.length();

            System.out.println("text : "+s1);
            System.out.printf(String.format("pattern : %%%ds\n", len1), s2);
            System.out.println("text : "+s1);
            System.out.printf(String.format("pattern : %%%ds\n", len2), s2);
        }
    }
}
