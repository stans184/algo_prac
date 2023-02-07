public class Tiger extends animal implements Predator, Barkable{
    public String getFood(){
        return "apple";
    }

    public void bark(){
        System.out.println("TTTTT");
    }
}