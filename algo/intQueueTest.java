import java.util.Scanner;

public class intQueueTest {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        intQueue q = new intQueue(64);

        while(true){
            System.out.println("current data capacity : "+q.size()+"/"+q.capacity());
            System.out.println("(1) enqueue  (2) dequeue  (3) peak  (4) dump  (5) quit");

            int menu = sc.nextInt();
            if(menu == 5)    break;

            int x;
            switch(menu){
                case 1:
                    System.out.print("data : ");
                    x = sc.nextInt();
                    try{
                        q.enque(x);
                    }catch(intQueue.overflowQueueException e){
                        System.out.println("Queue is full");
                    }
                    break;

                case 2:
                    try{
                        x =q.deque();
                        System.out.println("dequeed data is "+x);
                    }catch(intQueue.emptyintQueueException e){
                        System.out.println("Queue is emtpy");
                    }
                    break;
                case 3:
                    try{
                        x = q.peek();
                        System.out.println("peak data of Queue is "+x);
                    }catch(intQueue.emptyintQueueException e){
                        System.out.println("Queue is empty");
                    }
                    break;

                case 4:
                    q.dump();
                    break;
            }
        }
    }
}
