import java.util.Arrays;
import java.util.Comparator;

public class PhyscExamSort {
    static class PhyscData{
        String name;
        int height;
        double vision;

        PhyscData(String name, int height, double vision){
            this.name = name;
            this.height = height;
            this.vision = vision;
        }

        public String toString(){
            return name+" "+height+" "+vision;
        }

        static final Comparator<PhyscData> HEIGHT_ORDER = new HeightOrderComparator();

        private static class HeightOrderComparator implements Comparator<PhyscData>{
            public int compare(PhyscData d1, PhyscData d2){
                return (d1.height > d2.height) ? 1 : (d1.height<d2.height) ? -1 : 0;
            }
        }
    }

    public static void main(String[] args) {
        PhyscData[] x = {
            new PhyscData("jo", 168, 0.6),
            new PhyscData("sx", 181, 0.7),
            new PhyscData("vu", 176, 1.0),
            new PhyscData("da", 185, 0.8),
            new PhyscData("son", 168, 1.22),
            new PhyscData("kane", 179, 0.9),
        };

        Arrays.sort(x,PhyscData.HEIGHT_ORDER);

        System.out.println("physical test result");
        System.out.println("x : "+Arrays.toString(x));
    }
}
