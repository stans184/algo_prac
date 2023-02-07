import java.util.Scanner;

public class binSearch {
    static int BinSearch(int[] a, int n,int key){
        int pl = 0; // first index of searching area
        int pr = n-1;   // last index of searching area

        do{
            int pc = (pl+pr)/2;
            if(a[pc] == key)    return pc;
            else if(a[pc]<key)  pl = pc+1;
            else pr = pc-1;
        }while(pl<=pr);
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("number : ");
        int num = sc.nextInt();
        int[] x = new int[num];

        System.out.println("enter the value in sequence");

        System.out.print("x[0] : ");
        x[0] = sc.nextInt();

        for(int i=1;i<num;i++){
            do{
                System.out.print("x["+i+"] : ");
                x[i] = sc.nextInt();
            }while(x[i]<x[i-1]);
        }

        System.out.print("searching data : ");
        int ky = sc.nextInt();
        sc.close();
        int idx = BinSearch(x, num, ky);

        if(idx == -1)   System.out.println("value is not exist");
        else    System.out.println(ky+" is in x["+idx+"]");
    }
}
