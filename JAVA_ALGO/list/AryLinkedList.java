import java.util.Comparator;
                                                                            // 연결된 list, 배열 cursor 버전
public class AryLinkedList<E> {
    class node<E>{                                                          // 노드
        private E data;                                                     // data
        private int next;                                                   // list의 뒤쪽 pointer
        private int dnext;                                                  // free list의 뒤쪽 pointer

        void set(E data, int next){                                         // data와 next를 설정
            this.data = data;
            this.next = next;
        }
    }

    private node<E>[] n;                                                    // list 본체
    private int size, max, head, crnt, deleted;                             // 용량, 꼬리 record, 머리노드, 선택노드, free list의 머리 노드
    private static final int NULL = -1;                                     // 다음 노드가 없음 / list가 가득 참

    public AryLinkedList(int capacity){                                     // 생성자
        head = crnt = max = deleted = NULL;
        try{
            n = new node[capacity];
            for(int i = 0;i<capacity;i++){
                n[i] = new node<E>();
            }
            size = capacity;
        }catch(OutOfMemoryError e){                                         // 배열 생성에 실패할 경우
            size = 0;
        }
    }

    private int getInsertIndex(){                                           // 다음에 삽입하는 record의 인덱스를 구함
        if(deleted == NULL){                                                // 삭제할 record가 없을 경우
            if(max<size)    return ++max;                                   // 용량보다 작으면 record를 늘려주거나
            else    return NULL;                                            // 용량 넘으면 끝
        }else{
            int rec = deleted;                                              // free list에서
            deleted = n[rec].dnext;                                         // header를 꺼냄
            return rec;
        }
    }

    private void deleteIndex(int idx){
        if(deleted == NULL){                                                // 삭제할 record가 없음
            deleted = idx;                                                  // idx를 free list의
            n[idx].dnext = NULL;                                            // 머리에 등록
        }else{
            int rec = deleted;                                              // 삭제할 record가 있다면
            deleted = idx;                                                  // 머리 노드에 삽입
            n[idx].dnext = rec;
        }
    }

    public E search(E obj, Comparator<? super E> c){                        // 노드 검색
        int ptr = head;                                                     // 현재 스캔중인 노드

        while(ptr != NULL){
            if(c.compare(obj, n[ptr].data) == 0){
                crnt = ptr;
                return n[ptr].data;                                         // 검색 성공
            }
            ptr = n[ptr].next;                                              // 다음 노드에 주목
        }
        return null;                                                        // 검색 실패
    }

    public void addFirst(E obj){
        int ptr = head;                                                     // 삽입 전의 머리 노드
        int rec = getInsertIndex();
        if(rec != NULL){
            head = crnt = rec;                                              // 인덱스 rec인 record에 삽입
            n[head].set(obj, ptr);
        }
    }

    public void addLast(E obj){                                             
        if(head == NULL)    addFirst(obj);                                  // list가 비어있으면 머리에 삽입
        else{
            int ptr = head;
            while(n[ptr].next != NULL)
                ptr = n[ptr].next;
            int rec = getInsertIndex();
            if(rec != NULL){                                                // 인덱스 rec인 record에 삽입
                n[ptr].next = crnt = rec;
                n[rec].set(obj, NULL);
            }
        }
    }


    public void removeFirst(){
        if(head != NULL){                                                   // list가 비어있지 않으면
            int ptr = n[head].next;
            deleteIndex(head);
            head = crnt = ptr;
        }
    }

    public void removeLast(){
        if(head != NULL){                                                   // 노드가 하나만 있으면
            if(n[head].next == NULL)    removeFirst();                      // 머리 노드를 삭제
        }else{
            int ptr = head;                                                 // 스캔중인 노드
            int pre = head;                                                 // 스캔중인 노드의 앞쪽 노드

            while(n[ptr].next != NULL){
                pre = ptr;
                ptr = n[ptr].next;
            }
            n[pre].next = NULL;                                             // pre는 삭제 후의 꼬리 노드
            deleteIndex(ptr);
            crnt = pre;
        }
    }

    public void remove(int p){
        if(head != NULL){
            if(p == head)   removeFirst();
            else{
                int ptr = head;

                while(n[ptr].next != p){
                    ptr = n[ptr].next;
                    if(ptr == NULL) return;
                }
                n[ptr].next = NULL;
                deleteIndex(p);
                n[ptr].next = n[p].next;
                crnt = ptr;
            }
        }
    }

    public void removeCurrntnode(){
        remove(crnt);
    }

    public void clear(){
        while(head != NULL) removeFirst();
        crnt = NULL;
    }

    public boolean next(){
        if(crnt == NULL || n[crnt].next == NULL)    return false;
        crnt = n[crnt].next;
        return true;
    }

    public void printCurrntnode(){
        if(crnt == NULL)    System.out.println("you have to choose a node");
        else    System.out.println(n[crnt].data);
    }

    public void dump(){
        int ptr = head;

        while(ptr != NULL){
            System.out.println(n[ptr].data);
            ptr = n[ptr].next;
        }
    }
}
