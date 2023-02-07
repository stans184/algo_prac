import java.util.Scanner;

public class median {
    
    static int med3(int a, int b, int c){
        if (a>=b)
            if (b>=c)
                return b;
            else if (c>=a)
                return a;
            else
                return c;
        else if (a>c)
            return a;
        else if (b>c)
            return c;
        else
            return b;            
    }
// thick about difference between two method
    static int med3_2(int a, int b, int c){
        if(((b>=a)&&(c<=a)) || ((b<=a)&&(c>=a)))
            return a;
        else if (((a>b)&&(c<b)) || ((a<b)&&(c>b)))
            return b;
        else
            return c;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("middle of numbers ");
        System.out.print("a : ");
        int a = sc.nextInt();
        System.out.print("b : ");
        int b = sc.nextInt();
        System.out.print("c : ");
        int c = sc.nextInt();

        sc.close();

        System.out.println("middle number is "+med3(a, b, c));

        System.out.println((c==b) ? "c=b" : "c=|b");
    }
}
