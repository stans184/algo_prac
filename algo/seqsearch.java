import java.util.Scanner;

public class seqsearch {
    static int seqSearch(int[] a, int n, int key){
        for (int i = 0;i<n;i++){
            if(a[i]==key) return i;
        }
        return -1;
    }
    

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("number : ");
        int num = sc.nextInt();
        int[] x = new int[num];

        for(int i = 0;i<num;i++){
            System.out.print("x["+i+"] : ");
            x[i] = sc.nextInt();
        }

        System.out.print("search data : ");
        int ky = sc.nextInt();
        sc.close();
        int idx = seqSearch(x, num, ky);

        if (idx == -1){
            System.out.println("value is not in array");
        }else{
            System.out.println("value is in"+idx);
        }
    }
}
