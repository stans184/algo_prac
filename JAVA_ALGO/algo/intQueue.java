public class intQueue {
    private int max;
    private int front;
    private int rear;
    private int num;
    private int[] que;
    
    public class emptyintQueueException extends RuntimeException{
        public emptyintQueueException(){}
    }

    public class overflowQueueException extends RuntimeException{
        public overflowQueueException(){}
    }

    public intQueue(int capacity){
        num = front = rear = 0;
        max = capacity;
        try{
            que = new int[max];
        }catch(OutOfMemoryError e){max =0;}
    }

    public int enque(int x) throws overflowQueueException{
        if(num>=max)    throw new overflowQueueException(); // 용량을 벗어나는 에러를 감지
        que[rear++]=x;
        num++;
        if(rear==max)    rear=0;    // rear data를 맨 처음으로 돌림
        return x;
    }

    public int deque() throws emptyintQueueException{
        if(num<=0)  throw new emptyintQueueException();
        int x = que[front++];
        num--;
        if(front==max)  front=0;
        return x;
    }

    public int peek() throws emptyintQueueException{
        if(num<=0)  throw new emptyintQueueException();
        return que[front];
    }

    public int indexOf(int x){
        for(int i=0;i<num;i++){
            int idx = (i+front)%max;
            if(que[idx]==x) return idx;
        }
        return -1;
    }

    public void clear(){num=front=rear=0;}

    public int capacity(){return max;}

    public int size(){return num;}

    public boolean isEmpty(){return num<=0;}

    public boolean isFull(){return num>=max;}

    public void dump(){
        if(num<=0)  System.out.println("queue is empty");
        else{
            for(int i=0;i<num;i++)  System.out.print(que[(i+front)%max]+" ");
            System.out.println();
        }
    }
}
