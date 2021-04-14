import java.util.Scanner;
import java.util.Scanner;

public class lastNElemets {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        final int N = 10;
        int[] a = new int[N];
        int cnt = 0;
        int retry;

        System.out.println("input the integer");

        do{
            System.out.printf("%d th integer ", cnt+1);
            a[cnt++ %N] = sc.nextInt();
        
            System.out.print("(1) go  (2) stop");
            retry = sc.nextInt();
        }while(retry==1);
    
        int i = cnt-N;
        if(i<0) i=0;

        for( ; i<cnt;i++)   System.out.printf("%d th integer = %d\n", i+1,a[i%N]);
    
    }
}
