import java.util.Random;
// import java.util.Scanner;

public class maxArrayRand {
    static int maxOf(int[] a){
        int max = a[0];
        for(int i=0;i<a.length;i++){
            if(a[i]>max) max = a[i];
        }
        return max;
    }

    public static void main(String[] args) {
        Random rd = new Random();
        // Scanner sc = new Scanner(System.in);

        System.out.println("maximun value of height");
        System.out.print("how many people ? ");
        // int num = sc.nextInt();
        int num = rd.nextInt(20);
        // sc.close();

        int[] height = new int[num];

        System.out.println("height value is...");
        for(int i=0;i<num;i++){
            height[i] = 100 + rd.nextInt(100);
            // System.out.println("height[ "+i+" ] "+height[i]);
        }

        System.out.println("max height is "+maxOf(height));
    }
}
