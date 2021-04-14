public class Counter {
    static int count = 0;
    Counter(){
        this.count++;
        System.out.println(this.count);
    }

    public static int getCount(){
        return count;
    }

    public static void main(String[] args) {
        Counter c1 = new Counter();
        Counter c2 = new Counter();

        System.out.println(Counter.getCount());
    }
    
}
