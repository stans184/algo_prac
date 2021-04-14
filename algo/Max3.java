import java.util.Scanner;

public class Max3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("i will check max number");
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        sc.close();

        max3m(a, b, c);
    }

    static void max3m(int a, int b, int c){
        int max = a;
        if (b>max)
            max = b;
        if (c>max)
            max = c;
        
        System.out.println("max number is "+max);
    }
}
