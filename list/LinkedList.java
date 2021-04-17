import java.util.Comparator;

public class LinkedList<E> {
    class node<E>{
        private E data;                             // data
        private node<E> next;                       // pointer to next data
    
        node(E data, node<E> next){                 // 생성자
            this.data = data;
            this.next = next;
        }
    }
    
    private node<E> head;                           // 머리 노드
    private node<E> crnt;                           // 현재 노드

    public LinkedList(){                            // 생성자
        head = crnt = null;
    }
                                                    // 검색
    public E search(E obj, Comparator<? super E> c){
        node<E> ptr = head;                         // 현재 검색중인 노드

        while(ptr != null){
            if(c.compare(obj, ptr.data) == 0){      // 검색 성공
                crnt = ptr;
                return ptr.data;
            }
            ptr = ptr.next;                         // 다음 노드를 선택
        }
        return null;                                // 검색 실패
    }

    public void addFirst(E obj){                    // 맨 앞에 노드 추가
        node<E> ptr = head;                         // 삽입 전 머리 노드
        head = crnt = new node<E>(obj, ptr);
    }

    public void addLast(E obj){                     // 맨 뒤에 노드 추가
        if(head == null)    addFirst(obj);          // 리스트가 비어있는지 확인
        else{
            node<E> ptr = head;
            while(ptr.next != null)                 // while문 종료 시, ptr은 꼬리 노드를 가르킴
                ptr = ptr.next;
            ptr.next = crnt = new node<E>(obj, null);
        }
    }

    public void removeFirst(){                      // 머리 노드를 삭제 -> list가 비어있지 않으면 삭제 진행
        if(head != null)    head = crnt = head.next;
    }

    public void removeLast(){
        if(head != null){
            if(head.next == null)   removeFirst();  // 노드가 하나만 있으면, 머리 노드를 삭제
        }
        else{
            node<E> ptr = head;                     // 스캔중인 노드
            node<E> pre = head;                     // 그 앞쪽 노드

            while(ptr.next != null){                // while문이 끝나면, ptr은 꼬리 노드를, pre는 그 앞의 노드를 가르키고 있는다
                pre = ptr;
                ptr = ptr.next;
            }
            pre.next = null;                        // pre는 삭제 후 의 꼬리 노드
            crnt = pre;
        }
    }

    public void remove(node p){                     // 노드 p를 삭제
        if(head != null){
            if(p == head)   removeFirst();          // p가 머리 노드면, 머리 노드를 삭제
        }
        else{
            node<E> ptr = head;

            while(ptr.next != p){
                ptr = ptr.next;
                if(ptr == null) return;             // p가 list에 없다
            }
            ptr.next = p.next;
            crnt = ptr;
        }
    }

    public void removeCurrntnode(){                 // 선택 노드를 삭제
        remove(crnt);
    }

    public void clear(){                            // 모든 노드를 삭제
        while(head != null)    removeFirst();       // head에 아무것도 없을 때까지, 머리 노드를 계속 삭제
        crnt = null;
    }

    public boolean next(){                          // 선택 노드를 하나 뒤로 이동
        if(crnt == null || crnt.next == null)   return false;   //  list가 비어있지 않고, 뒤편 노드도 비어있지 않을때, 노드를 뒤로 움직인다
        crnt = crnt.next;
        return true;
    }

    public void printCurrntnode(){                  // 현재 노드를 프린트
        if(crnt == null)    System.out.println("there is no node");
        else    System.out.println(crnt.data);
    }

    public void dump(){                             // 전체 list 출력
        node<E> ptr = head;                         // 머리에 포인터를 잡고

        while(ptr != head){                         // 계속 머리 노드로 땡겨오면서
            System.out.println(ptr.data);           // 머리 data를 출력하고
            ptr = ptr.next;                         // 한칸씩 뒤로 옮긴다
        }
    }
}