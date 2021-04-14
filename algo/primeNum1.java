import java.util.Scanner;

public class primeNum1 {
    public static void main(String[] args) {
        System.out.print("input maxinum number : ");
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int counter = 0;
        
        for(int n=2;n<=num;n++){
            int i;
            for(i=2;i<n;i++){
                counter++;
                if(n%i == 0)
                    break;
            }
            if(n==i)
                System.out.print(n+" ");
        }
        System.out.println("\ndivided count is "+counter);
    }
}
