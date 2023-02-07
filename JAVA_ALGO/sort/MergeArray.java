import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;

public class MergeArray {
    static void merge(int[] a, int na, int[] b,int nb, int[] c){
        int pa=0;
        int pb=0;
        int pc=0;

        while(pa<na && pb<nb)   // a 행렬의 값과 b행렬의 값을 하나씩 왼쪽으로 스캔해가면서
            c[pc++] = (a[pa]<=b[pb]) ? a[pa++] : b[pb++];   // 두 값을 비교해서 더 작은 값을 c행렬로 채워넣는다

        while(pa<na)    // 만약 a행렬이 b행렬보다 커서 남아있다면, 남은 값을 넣어주고
            c[pc++] = a[pa++];

        while(pb<nb)    // b행렬의 값들이 남아있다면 그 값들을 c행렬로 넣어준다
            c[pc++] = b[pb++];
    }
    
    public static void main(String[] args) throws IOException {
        int[] a = {2,4,6,8,11,13};
        int[] b = {1,3,5,7,12,15};
        int[] c = new int[12];

        System.out.println("merge of two array");
        merge(a, a.length, b, b.length, c);
        System.out.println("merge array A & array B, so saved array C");
        System.out.println("a : "+Arrays.toString(a));
        System.out.println("b : "+Arrays.toString(b));
        System.out.println("c : "+Arrays.toString(c));
    }
}
