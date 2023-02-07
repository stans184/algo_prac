public class testTry {
    public void shouldBeRun(){
        System.out.println("ok thanks.");
    }

    public void sayNick(String nick){
        if("fool".equals(nick)){
            throw new FoolException();
        }
        System.out.println("Your nickname is "+nick);
    }

    public static void main(String[] args) {
        testTry test1 = new testTry();
        int c;

        try{
            c = 4/0;
            test1.shouldBeRun();
        }catch(ArithmeticException e){
            c = -1;
        }finally{
            test1.shouldBeRun();
        }

        System.out.println(c);

        testTry test2 = new testTry();
        test2.sayNick("fool");
        test2.sayNick("genious");
    }
}
