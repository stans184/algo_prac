import java.util.Scanner;

public class digit {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int no;

        System.out.println("input positive two places number");

        do{
            System.out.print("input : ");
            no = sc.nextInt();
        }while(no<10 || no>99);

        sc.close();
    }    
}
