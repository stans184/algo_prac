import java.io.InputStream; // byte input
import java.io.InputStreamReader; // character input
import java.io.BufferedReader; // String input

import java.util.Scanner; //  more easiler input

public class streamTest {
    public static void main(String[] args) throws Exception{
        // InputStream in = System.in;
        // InputStreamReader reader = new InputStreamReader(in);
        // BufferedReader br = new BufferedReader(reader);

        // char[] a = new char[10]; // 배열의 크기로 입력 data의 크기를 설정
        // reader.read(a);

        // String a = br.readLine();
        // System.out.println(a);

        Scanner sc = new Scanner(System.in);
        System.out.println(sc.next());
        System.out.println(sc.nextLine());
        sc.close();
    }
}
