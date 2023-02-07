import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;

public class partition{
    static void swap(int[] a, int idx1, int idx2){
        int temp = a[idx1];
        a[idx1] = a[idx2];
        a[idx2] = temp;
    }

    static void partition(int[] a, int n){
        int pl = 0;
        int pr = n-1;
        int x = a[n/2];

        do{
            while(a[pl] < x) pl++;  // 배열의 왼쪽에서부터, 중간값보다 작으면 계속 오른쪽으로 이동, 중간값보다 큰 data가 나오면 멈춤
            while(a[pr] > x) pr--;  // 배열의 오른쪽에서부터, 중간값보다 크면 계속 왼쪽으로 이동, 중간값보다 작은 data가 나오면 멈춤
            if(pl <= pr)            // 왼쪽 포인터가 오른쪽 포인터보다 작으면
                swap(a, pl++, pr--);    // pl과 pr의 위치를 바꿈
        }while(pl<=pr); // pl(left data) 가 pr(right data) 보다 작으면 계속 실행

        System.out.println("pivot data is "+x);

        System.out.println("group under pivot data");
        for(int i=0;i<pl-1;i++) System.out.print(a[i]+ " ");    // 왜 pl-1 까지지?
        System.out.println();

        if(pl>pr+1){
            System.out.println("pivot group");
            for(int i = pr+1;i<=pl-1;i++)    System.out.print(a[i] + " ");
            System.out.println();
        }

        System.out.println("group over the pivot data");
        for(int i=pr+1;i<n;i++)   System.out.print(a[i] + " "); // 왜 pr+1 부터인가?
        System.out.println();
    }

    public static void main(String[] args) throws IOException{
        System.out.println("divide array");
        System.out.print("number of array : ");

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int nx = Integer.parseInt(bf.readLine());
        int[] x = new int[nx];

        for(int i=0;i<nx;i++){
            System.out.print("x["+i+"] : ");
            x[i] = Integer.parseInt(bf.readLine());
        }
        
        partition(x, nx);
    }
}