import java.util.Scanner;

public class GuGu {
    public static void main(String[] args) {
        int num = 0;  

        Scanner sc = new Scanner(System.in);
        System.out.println("The number is "+sc.nextInt());
        num = sc.nextInt();

        while(num>0){
            for(int i=1;i<10;i++){
                System.out.println(num+" x "+i+" = "+num*i+"\r\n");
            }
            if(num<=0) break;
        }
    sc.close();
    }
}