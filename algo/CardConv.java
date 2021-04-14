import java.util.Scanner;

public class CardConv {
    static int cardConvR(int x, int r, char[] d){
        int digits = 0;
        String dchar = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

        do{
            d[digits++] = dchar.charAt(x % r);
            x /= r;
        }while(x!=0);
        return digits;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int no,cd,dno,retry;
        char[] cno = new char[32];

        System.out.println("10진수를 기수 변환합니다. ");
        do{
            do{
                System.out.print("변환하는 음이 아닌 정수 : ");
                no = sc.nextInt();
            }while(no<0);

            do{
                System.out.print("어떤 진수로 변환할까요? (2~36) : ");
                cd = sc.nextInt();
            }while(cd<2 || cd >37);

            dno = cardConvR(no,cd,cno);

            System.out.print(cd +"진수로는 ");
            for(int i=dno-1;i>=0;i--){
                System.out.print(cno[i]);
            }
            System.out.println();

            System.out.print("do you want more? (1 : yes, 2 : no) ");
            retry = sc.nextInt();
            sc.close();
        }while(retry == 1);
    }
}
