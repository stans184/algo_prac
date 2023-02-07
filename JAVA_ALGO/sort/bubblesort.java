import java.util.Scanner;

public class bubblesort {
    static void swap(int[] a, int idx1, int idx2){
        int t = a[idx1];
        a[idx1] = a[idx2];
        a[idx2] = t;
    }

    static void bubblesort(int[] a, int n){
        int exch = 0;
        for(int i = 0;i<n-1;i++){
            for(int j=n-1;j>i;j--){
                if(a[j-1]>a[j]) {
                    swap(a, j-1, j);
                exch++;
                }
            }
            if(exch == 0) break;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("bubble sort (version 1)");
        System.out.print("count ");
        int nx = sc.nextInt();
        int[] x = new int[nx];

        for(int i = 0;i<nx;i++){
            System.out.print(i+" = ");
            x[i] = sc.nextInt();
        }

        bubblesort(x, nx);

        System.out.println("upstreaming");
        for(int i=0;i<nx;i++)   System.out.print(x[i]+" ");
    }
}
