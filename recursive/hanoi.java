import java.util.Scanner;

public class hanoi {
    static void move(int no, int x, int y){
        if(no>1)    move(no-1, x, 6-x-y);
        System.out.println("원반["+no+"] 이동하여 "+y+"기둥으로 옮김");
        if(no>1)    move(no-1, 6-x-y, y);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("tower of hanoi");
        System.out.print("input the number of plate : ");
        int n = sc.nextInt();

        move(n, 1, 3);
    }
}
