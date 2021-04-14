import java.util.Scanner;

public class insertSort {
    static void insertSort(int[] a, int n){
        for(int i=1;i<n;i++){
            int j;
            int temp = a[i];
            for(j=i;j>0 && a[j-1]>temp;j--){
                a[j] = a[j-1];
            }
            a[j] = temp;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("insert sort");
        System.out.print("maxinum number : ");
        int nx = sc.nextInt();
        int[] x = new int[nx];

        for(int i=0;i<nx;i++){
            System.out.println("x["+i+"] : ");
            x[i] = sc.nextInt();
        }
        sc.close();
        insertSort(x, nx);

        System.out.println("upstream");
        for(int i=0;i<nx;i++)   System.out.print(x[i]+" ");
    }
}
