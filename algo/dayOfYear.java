import java.util.Scanner;

public class dayOfYear {
    static int[][] mdays = {
        {31,28,31,30,31,30,31,31,30,31,30,31},
        {31,29,31,30,31,30,31,31,30,31,30,31}
    };

    static int isLeap(int year){
        return (year%4 == 0 && year % 100 !=0 || year%400==0) ? 1 : 0;
    }

    static int dayOfYear(int y, int m, int d){
        int days = d;

        for(int i=1;i<m;i++)
            days += mdays[isLeap(y)][i-1];
        return days;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int retry;

        System.out.println("calculate passed days of years");

        do{
            System.out.print("years : "); int year = sc.nextInt();
            System.out.print("monthss : "); int month = sc.nextInt();
            System.out.print("days : "); int day = sc.nextInt();

            System.out.println("passed days : "+dayOfYear(year, month, day));

            System.out.print("you want more ? (1:yes, 2:no) ");
            retry = sc.nextInt();
            sc.close();
        }while(retry == 1);

    }
}
