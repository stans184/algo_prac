import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BFmatch {
    static int bfMatch(String txt, String pat){     //  브루트-포스 법으로 문자열을 검색하는 method
        int pt = 0;
        int pp = 0;

        while(pt != txt.length() && pp != pat.length()){
            if(txt.charAt(pt) == pat.charAt(pp)){
                pt++;
                pp++;
            }else{
                pt = pt-pp+1;
                pp = 0;
            }
        }

        if(pp == pat.length()){
            return pt-pp;
        }
        return -1;
    }

    public static void main(String[] args) throws IOException{
        System.out.print("text : ");
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String s1 = bf.readLine();

        System.out.print("pattern : ");
        String s2 = bf.readLine();

        int idx = bfMatch(s1, s2);

        if(idx == -1)   System.out.println("there isn't matching pattern in text");
        else{
            int len=0;
            for(int i=0;i<idx;i++)
                len += s1.substring(i, i+1).getBytes().length;
            len += s2.length();

            System.out.println("matching from "+(idx+1));
            System.out.println("text : "+s1);
            System.out.printf(String.format("pattern : %%%ds\n", len), s2);
        }
    }
}
