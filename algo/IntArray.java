public class IntArray {
    public static void main(String[] args) {
        int[] a = new int[5];
        // int[] b = {4,345,123,7456,34,2};

        a[1] = 14;
        a[2] = 345;
        a[4] = a[1]*2;

        for(int i = 0;i<5;i++){
            System.out.println(a[i]);
        }
        int[] c = a.clone();

        int max = a[0];
        for(int i=1;i<c.length;i++){
            if(a[i]>max) max = a[i];
        }
        System.out.println(max);
    }
    
}
