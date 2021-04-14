public class Lion extends animal implements BarkablePredator{
    public String getFood(){
        return "banana";
    }

    public void bark(){
        System.out.println("LLLL");
    }
}
