import java.util.Scanner;

public class selectsort {
    static void swap(int[] a, int idx1, int idx2){
        int t = a[idx1];
        a[idx1] = a[idx2];
        a[idx2] = t;
    }

    static void selectsort(int[] a, int n){
        for(int i=0;i<n-1;i++){
            int min = i;
            for(int j=i+1;j<n; i++){
                if(a[j] < a[min])   min=j;
            }
            swap(a, i, min);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("select sort (version 1)");
        System.out.print("count ");
        int nx = sc.nextInt();
        int[] x = new int[nx];

        for(int i = 0;i<nx;i++){
            System.out.print(i+" = ");
            x[i] = sc.nextInt();
        }

        selectsort(x, nx);

        System.out.println("upstreaming");
        for(int i=0;i<nx;i++)   System.out.print(x[i]+" ");
    }
}
