import java.util.Scanner;

public class sunWhile {

    public static int gausian(int n){
        int sum = n*(n+1)/2;

        return sum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        sc.close();

        do{
            if (a>b)
                System.out.println("please intput bigger b than a");
            else{
                System.out.println("total sum from "+a+" to "+b);

                int sum = 0;
                
                for (int i=a;i<=b;i++){
                    sum += i;
                }
                System.out.println("total sum is " + sum);
                System.out.println("gausian formula " +gausian(b));
            }
        }while(a<=b);
    }
}
