import java.util.Scanner;

public class factorial{
    static int factorial(int n){
        if(n>0) return n*factorial(n-1);
        else    return 1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("input the number : ");
        int num = sc.nextInt();
        sc.close();
        System.out.println("factorial of "+num+" is "+factorial(num));
    }
}