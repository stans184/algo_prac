import java.util.Scanner;

public class primeNum2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("input the maxinum number : ");
        int num = sc.nextInt();
        sc.close();
        int counter = 0;    // count of divide
        int ptr = 0;    // count of primeNumber
        int[] prime = new int[500]; // save prime number
        int n;
    
        prime[ptr++] = 2;   // 2 is only prime number in odd num

        for(n=3;n<num;n+=2){
            int i;
            for(i=1;i<=ptr;i++){
                counter++;
                if(n%prime[i] == 0) break;  // value가 0이 나오는 오류 발생,,, why??
            }
            if(ptr == i)
                prime[ptr++] = n;
        }

        for(int i=0;i<ptr;i++){
            System.out.print(prime[i]+" ");
        }
    
   
    }
}
