public class intStack {
    private int max;
    private int ptr;
    private int[] stk;

    public class emptyIntStackException extends RuntimeException{
        public emptyIntStackException(){}
    }   

    public class overflowIntStackException extends RuntimeException{
        public overflowIntStackException(){}
    }

    public intStack(int capacity){
        ptr = 0;
        max = capacity;
        try{
            stk = new int[max];
        }catch(OutOfMemoryError e){max = 0;}
    }

    public int push(int x) throws overflowIntStackException{
        if(ptr>=max)    throw new overflowIntStackException();
        return stk[ptr++] = x;
    }

    public int pop() throws emptyIntStackException{
        if(ptr<=0)  throw new emptyIntStackException();
        return stk[--ptr];
    }

    public int peak() throws emptyIntStackException{
        if(ptr<=0)  throw new emptyIntStackException();
        return stk[ptr -1];
    }

    public int indexOf(int x){
        for(int i=ptr-1;i>=0;i--){
            if(stk[i] == x) return i;
        }
        return -1;
    }

    public void clear(){ptr = 0;}

    public int capacity(){return max;}

    public int size(){return ptr;}

    public boolean isEmpty(){return ptr<=0;}

    public boolean isFull(){return ptr>=max;}

    public void dump(){
        if(ptr<=0)  System.out.println("stack is empty");
        else{
            for(int i=0;i<ptr;i++)  System.out.print(stk[i]+" ");
            System.out.println();
        }
    }
}