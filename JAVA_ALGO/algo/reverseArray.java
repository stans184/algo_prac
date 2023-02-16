import java.util.*;

public class reverseArray {
    static void swap(int[] a, int idx1, int idx2){
        int i = a[idx1];
        a[idx1] = a[idx2];
        a[idx2] = i;
    }

    static void reverse(int[] a){
        for(int i = 0;i<a.length/2;i++){
            swap(a, i, (a.length -1 -i));
        }
    }

    static int sum(int[] a){
        int sum = 0;
        for(int i = 0;i<a.length;i++){
            sum += a[i];
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("data : ");
        int num = sc.nextInt();
        int[] x = new int[num];

        for(int i = 0;i<num;i++){
            x[i] = sc.nextInt();
        }
        sc.close();
        reverse(x);

        System.out.println(Arrays.toString(x));

        System.out.println("sum of array is "+sum(x));
    }
}
