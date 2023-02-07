import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Fsort {
    static void fSort(int[] a, int n, int max){
        int[] f = new int[max+1];
        int[] b = new int[n];
    

    for(int i=0;    i<n;    i++)    f[a[i]]++;
    for(int i=1;    i<=max; i++)    f[i]+=f[i-1];
    for(int i=n-1;  i>=0;   i--)    b[--f[a[i]]] = a[i];
    for(int i=0;    i<n;    i++)    a[i]=b[i];
    }

    public static void main(String[] args) throws IOException{
        System.out.println("도수정렬");
        System.out.print("number of Array : ");
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int nx = Integer.parseInt(bf.readLine());
        int[] x = new int[nx];

        for(int i=0;i<nx;i++){
            System.out.print("x["+i+"] : ");
            x[i] = Integer.parseInt(bf.readLine());
        }

        int max=x[0];
        for(int i=1;i<nx;i++)
            if(x[i]>max)    max=x[i];

        fSort(x, nx, max);

        System.out.println("Upstreaming");
        System.out.println("x : "+Arrays.toString(x));
    }
}
