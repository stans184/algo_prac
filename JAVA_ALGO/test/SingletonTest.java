class Singleton{
    private static Singleton one;
    private Singleton(){
    }

    public static Singleton getInstatnce(){
        if(one==null){
            one = new Singleton();
        }
        return one;
    }
}

public class SingletonTest {
    public static void main(String[] args) {
        Singleton singleton1 = Singleton.getInstatnce();
        Singleton singleton2 = Singleton.getInstatnce();
        System.out.println(singleton1 == singleton2);
    }
}
