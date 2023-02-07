import java.util.Scanner;

public class arraySum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double[] a = new double[5];

        for(int i=0;i<a.length;i++){
            a[i] = sc.nextDouble();
        }
        sc.close();

        double sum = 0;
        for(double i : a)
            sum += i;

        System.out.println("total data is "+sum);
    }
    
}
