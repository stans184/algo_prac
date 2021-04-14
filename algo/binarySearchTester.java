import java.util.Scanner;
import java.util.Arrays;

public class binarySearchTester {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("number : ");
        int num = sc.nextInt();
        int x[] = new int[num];

        System.out.println("enter the value in sequence");

        System.out.print("x[0] : ");
        x[0] = sc.nextInt();

        for(int i=1;i<num;i++){
            do{
                System.out.print("x["+i+"] : ");
                x[i] = sc.nextInt();
            }while(x[i] < x[i-1]);
        }

        System.out.print("searching data : ");
        int ky = sc.nextInt();
        sc.close();
        int idx = Arrays.binarySearch(x, ky);

        if(idx<0)   System.out.println("the value is not exist in array");
        else    System.out.println(ky+" is in x["+idx+"]");
    }
}
