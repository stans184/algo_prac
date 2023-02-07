import java.util.Scanner;

public class IntStackTest {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        intStack s = new intStack(64);

        while(true){
            System.out.println("current data : "+s.size()+"/"+s.capacity());
            System.out.println("(1) push  (2) pop  (3) peak  (4) dump  (5) quit");

            int menu = sc.nextInt();
            if(menu==5) {
                System.out.println("stackflow is quit");
                break;
            }
            int x;

            switch(menu){
                case 1:
                    System.out.print("data : ");
                    x = sc.nextInt();
                    try{
                        s.push(x);
                    }catch(intStack.overflowIntStackException e){
                        System.out.println("stack is full");
                    }
                    break;

                case 2:
                    try{
                        x=s.pop();
                        System.out.println("popped data  : "+x);
                    }catch(intStack.emptyIntStackException e){
                        System.out.println("stack is empty");
                    }
                    break;
                
                case 3:
                    try{
                        x=s.peak();
                        System.out.println("peak data : "+x);
                    }catch(intStack.emptyIntStackException e){
                        System.out.println("stack is empty");
                    }
                    break;

                case 4:
                    s.dump();
                    break;
            }

        }
    }
}
