import java.util.Scanner;

public class shellSort {
    static void shellSort(int[] a, int n){
        for(int h = n/2;h>0;h/=2){
            for(int i=h;i<n;i++){
                int j;
                int temp = a[i];
                for(j=i-h;j>=0 && a[j]>temp;j-=h)
                    a[j+h] = a[j];
                a[j+h] = temp;
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Shell Sort (version 1)");
        System.out.print("count : ");
        int nx = sc.nextInt();
        int[] x = new int[nx];

        for(int i=0;i<nx;i++){
            System.out.print("x["+i+"] : ");
            x[i] = sc.nextInt();
        }

        shellSort(x, nx);

        System.out.println("upstream");
        for(int i=0;i<nx;i++){
            System.out.print(x[i]+" ");  
        }
    }

}
