import java.util.Scanner;

public class seqSersen {
    static int seqSearchSen(int[] a, int n, int key){
        a[n] = key; // add key data
        
        for(int i=0;i<=n;i++)
            if(a[i]==key) return i;
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("number : ");
        int num = sc.nextInt();
        int[] x = new int[num+1]; // +1 for key data

        for(int i=0;i<num;i++){
            System.out.print("data : ");
            x[i] = sc.nextInt();
        }

        System.out.print("searching data : ");
        int ky = sc.nextInt();
        sc.close();
        int idx = seqSearchSen(x, num, ky);

        if (idx == -1)  System.out.println("value is not exist");
        else    System.out.println("value is at x["+idx+"]");
    }
}
