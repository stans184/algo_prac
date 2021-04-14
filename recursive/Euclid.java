import java.util.Scanner;
// 유클리드 호제법, 최대공약수를 구하는 방법
// x,y로 된 직사각형을 정사각형으로 쪼개다가, 가장 작은 정사각형이 되면, 그게 최대공약수다
public class Euclid {
    static int gcd(int x, int y){
        if(y==0)    return x;
        else    return gcd(y, x%y);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("get maxinum division of two integer");

        System.out.print("input the integer 1 : "); int a = sc.nextInt();
        System.out.print("input the integer 2 : "); int b = sc.nextInt();
        sc.close();
        System.out.println("maxinum division is "+gcd(a, b));

    }
}
