import java.io.InputStreamReader;
import java.nio.Buffer;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;

public class QuickSort {
    static void swap(int[] a, int idx1, int idx2){
        int temp = a[idx1];
        a[idx1] = a[idx2];
        a[idx2] = temp;
    }

    static void quickSort(int[] a, int left, int right){
        int pl = left;
        int pr = right;
        int x = a[(pl+pr)/2];

        do{
            while(a[pl] < x)    pl++;
            while(a[pr] > x)    pr--;
            if(pr>=pl)  swap(a, pl++, pr--);    // 양끝에서 한칸씩 검사하다가, 중간값보다 큰 pl, 중간값보다 작은 pr을 찾으면, 그 위치를 바꿔준다 -> 중간값 기준으로 작은게 왼쪽, 큰게 오른쪽으로 오게
        }while(pr>=pl);
        // 주어진 배열 a의 중간값 기준으로 작은게 왼쪽, 큰게 오른쪽으로 정리가 다 되면 pr은 왼쪽 구역의 제일 오른쪽값을, pl은 오른쪽 구역의 제일 왼쪽값을 가르킨다
        if(left<pr)    quickSort(a, left, pr);  // 정리된 배열의 왼쪽 구역을 한번 더 quicksort
        if(right>pl)   quickSort(a, pl, right); // 정리된 배열의 오른쪽 구역을 한번 더 quick sort
    }

    // non-recursive method
    static void quickSort2(int[] a, int left, int right){
        intStack lstack = new intStack(right - left +1);
        intStack rstack = new intStack(right -left+1);

        lstack.push(left);
        rstack.push(right);

        while(lstack.isEmpty() != true){
            int pl = left = lstack.pop();
            int pr = right = rstack.pop();
            int x = a[(pl+pr)/2];
            
            do{
                while(a[pl]<x)  pl++;
                while(a[pr]>x)  pr--;
                if(pl<=pr)  swap(a, pl++, pr--);
            }while(pr>=pl);

            if(left<pr){
                lstack.push(left);
                rstack.push(pr);
            }
            if(pl<right){
                lstack.push(pl);
                rstack.push(right);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.out.println("Quick Sort");
        System.out.print("number of array : ");

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int nx = Integer.parseInt(bf.readLine());
        int[] x = new int[nx];
        
        for(int i=0;i<nx;i++){
            System.out.print("x["+i+"] : ");
            x[i] = Integer.parseInt(bf.readLine());
        }

        System.out.println(Arrays.toString(x)); // input된 배열의 data 확인시, 정상

        quickSort2(x, 0, nx-1);

        System.out.println("upstreaming");
        for(int i=0;i<nx;i++)   System.out.print("x["+i+"] : "+x[i]+" ");
    }
}
