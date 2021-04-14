import java.util.Scanner;

public class Recur {
    static void recur(int n){  // 배열로 넣고자 했으나, 일단 pass
        if(n>0){
            recur(n-1);
            System.out.println(n);
            recur(n-2);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("input the integer : ");
        int x = sc.nextInt();
        sc.close();

        recur(x);
    }
}
