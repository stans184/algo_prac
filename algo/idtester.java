class Id {
    private static int counter = 0;
    private int id;

    public Id(){id = ++counter;} // 여기에 void가 들어갈때와 안들어갈때의 차이가 뭔가?

    public int getId(){return id;}

    public static int getCounter(){return counter;}
}

public class idtester{
    public static void main(String[] args) {
        Id a = new Id();
        Id b = new Id();

        System.out.println("id of a : "+a.getId());
        System.out.println("id of b : "+b.getId());

        System.out.println("total count of id : "+Id.getCounter());
    }    
}
