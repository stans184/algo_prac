import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.io.IOException;

public class HeapSort {
    static void swap(int[] a, int idx1, int idx2){
        int temp = a[idx1];
        a[idx1] = a[idx2];
        a[idx2] = temp;
    }

    // 주어진 배열을 heap 상태로 가공
    static void downheap(int[] a, int left, int right){
        int temp = a[left];
        int child, parent;

        for(parent = left;parent<(right+1)/2;parent=child){
            int cl = parent*2+1;
            int cr = cl+1;
            child = (cr<=right && a[cr] > a[cl]) ? cr : cl; //  큰 값을 가지는 node를 child에 대입
            if(temp>=a[child])  break;
            a[parent] = a[child];
        }
        a[parent] = temp;
    }
    // heap sort
    static void heapSort(int[] a,int n){
        for(int i=(n-1)/2;i>=0;i--) downheap(a, i, n-1);
        for(int i=n-1;i>0;i--){
            swap(a, 0, i);
            downheap(a, 0, i-1);
        }
    }

    public static void main(String[] args) throws IOException{
        System.out.println("Heap Sort");
        System.out.print("number of array : ");
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int nx = Integer.parseInt(bf.readLine());
        int[] x = new int[nx];

        for(int i=0;i<nx;i++){
            System.out.print("x["+i+"] : ");
            x[i] = Integer.parseInt(bf.readLine());
        }

        heapSort(x, nx);

        System.out.println("UpStreaming");
        System.out.println("x : "+Arrays.toString(x));
    }
}
