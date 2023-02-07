import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class MergeSort {
    static int[] buff;  // 작업용 배열?

    static void __mergeSort(int[] a, int left, int right){
        if(left<right){
            int i;
            int center = (left+right)/2;
            int p=0;
            int j=0;
            int k=left;

            __mergeSort(a, left, center);       // 배열의 앞부분을 병합정렬
            __mergeSort(a, center+1, right);    // 배열의 뒷부분을 병합정렬

            for(i=left;i<=center;i++)   buff[p++]=a[i]; // 왼쪽 부분을 buff 배열에 차례대로 대입

            while(i<=right && j<p)  // 왼쪽부분을 옮긴 buff 배열과 기존의 a배열 오른쪽 부분을 비교하여 더 작은 값 병합 배열
                a[k++] = (buff[j]<a[i]) ? buff[j++] : a[i++];

            while(j<p)  // buff의 남은 값 a 배열로 대입
                a[k++] = buff[j++];
        }
    }

    static void MergeSort(int[] a, int n){
        buff = new int[n];

        __mergeSort(a, 0, n-1);

        buff = null;    //  작업용 배열을 해제
    }

    public static void main(String[] args) throws IOException{
        System.out.println("Merge Sort");
        System.out.print("numbers of array : ");
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int nx = Integer.parseInt(bf.readLine());
        int[] x = new int[nx];
        
        for(int i=0;i<nx;i++){
            System.out.print("x["+i+"] : ");
            x[i] = Integer.parseInt(bf.readLine());
        }

        MergeSort(x, nx);

        System.out.println("UpStreaming");
        System.out.println("x : "+Arrays.toString(x));
    }
}
