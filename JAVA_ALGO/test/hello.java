import java.util.ArrayList; // necessary to use arraylist
import java.util.HashMap; // necessary to use map

public class hello{
    public static void main(String[] args){
        System.out.println("hello,world");
        

        // string
        String a = "subway";
        String b = new String("subway");
        // System.out.println(a.equals(b));
        // System.out.println(a==b);


        //StringBuffer
        StringBuffer sb = new StringBuffer();
        sb.append("hello");
        sb.append(" ");
        sb.append("jump to java");
        // System.out.println(sb);
        sb.insert(0, "i wanna go home ");
        // System.out.println(sb);
        // System.out.println(sb.substring(4,9));


        // String can save more memory then StringBuffer
        String temp = "";
        temp += "hello";
        temp += " ";
        temp += "jump to java";
        // System.out.println(temp);


        //Array
        String[] weeks = {"월", "화", "수", "목", "금", "토", "일"};
        for (int i=0; i<weeks.length; i++){
            // System.out.println(weeks[i]);
        }


        //ArrayList
        ArrayList pitches = new ArrayList();
        pitches.add("138");
        pitches.add("143");
        pitches.add("153");
        // System.out.println(pitches);
        // System.out.println(pitches.get(2));
        // System.out.println(pitches.size());
        // System.out.println(pitches.contains("149"));


        //generics -> array with type
        ArrayList<String> alist = new ArrayList<String>();
        alist.add("hello");
        alist.add("java");
        String hello = alist.get(0);
        String java = alist.get(1);
        // System.out.println(hello + java);


        // map (similar with dictionary)
        HashMap<String, String>map = new HashMap<String, String>();
        map.put("people", "사람");
        map.put("baseball", "야구");
        map.put("uniform", "유니폼");
        map.put("fans", "팬");
        System.out.println(map);
        // System.out.println(map.containsKey("fans"));
        // System.out.println(map.size());


        // if
        int money = 1800;
        boolean hasCard = true;
        if (money > 2000 && hasCard == true){
            // System.out.println("you can ride taxi");
        }else{
            // System.out.println("you have to walk");
        }
        // System.out.println(4>2);

        ArrayList<String> pocket = new ArrayList<String>();
        pocket.add("paper");
        pocket.add("mobile");
        pocket.add("card");

        if (pocket.contains("money")){
            // System.out.println("Go riding taxi");
        }else if (pocket.contains("card")){
            // System.out.println("Go riding taxi");
        }else{
            // System.out.println("you have to walk");
        }


        // switch / case
        // while
        int x = 0;
        while (x<10){
            x++;
            if(x%2 ==0){
                continue;
            }
            System.out.println(x);
        }

        
        // for each
        ArrayList<String> numbers = new ArrayList<String>();
        numbers.add("one");
        numbers.add("two");
        numbers.add("three");
        for(String number: numbers) {
            System.out.println(number);
        }










    }
}