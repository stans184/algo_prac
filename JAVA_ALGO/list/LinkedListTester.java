import java.util.Scanner;
import java.util.Comparator;

public class LinkedListTester {
    static Scanner sc = new Scanner(System.in);
    
    static class Data{                          // 데이터 (회원번호 + 이름)
        static final int NO = 1;                // 번호를 입력 받습니까?
        static final int NAME = 2;              // 이름을 입력 받습니까?

        private int no;                         // 회원번호
        private String name;                    // 이름

        public String toString(){               // 문자열 반환
            return "("+no+")"+name;
        }

        void scanData(String guide, int sw){    // 데이터 입력
            System.out.println("input data for "+guide);

            if((sw & NO)==NO){
                System.out.print("number : ");
                no = sc.nextInt();
            }
            if((sw & NAME) == NAME){
                System.out.print("name : ");
                name = sc.next();
            }
        }
                                                // 회원번호로 순서 정하는 COMPARATOR
        public static final Comparator<Data> NO_ORDER = new NoOrdereComparator();

        private static final class NoOrdereComparator implements Comparator<Data>{
            public int compare(Data d1, Data d2){
                return (d1.no > d2.no) ? 1 : (d1.no < d2.no) ? -1 : 0;
            }
        }
                                                // 이름으로 순서 정하는 COMPARATOR
        public static final Comparator<Data> NAME_ORDER = new NameOrderComparator();

        private static class NameOrderComparator implements Comparator<Data>{
            public int compare(Data d1, Data d2){
                return d1.name.compareTo(d2.name);
            }
        }
    }

    enum Menu{                                  // 메뉴 열거
        ADD_FIRST(      "insert node at head"),
        ADD_LAST(       "insert node at tail"),
        RMV_FIRST(      "remove node at head"),
        RMV_LAST(       "remove node at tail"),
        RMV_CRNT(       "remove currnt node"),
        CLEAR(          "remove all node"),
        SEARCH_NO(      "search with number"),
        SEARCH_NAME(    "serach witl name"),
        NEXT(           "move pointer next node"),
        PRINT_CRNT(     "print current node"),
        DUMP(           "print all node"),
        TERMINATE(      "quit");
    
        private final String messeage;          // 출력할 문자열

        static Menu MenuAt(int idx){            // 서수가 idx인 문자열 반환
            for(Menu m : Menu.values())
                if(m.ordinal() == idx)
                    return m;
            return null;
        }

        Menu(String string){                    // 생성자
            messeage = string;
        }

        String getMessage(){                    // 출력한 문자열을 반환
            return messeage;
        }
    }

    static Menu SelectMenu(){                   // 메뉴 선택
        int key;
        do{
            for(Menu m : Menu.values()){
                System.out.printf("(%d) %s  ",m.ordinal(), m.getMessage());
                if((m.ordinal() % 3) == 2 && m.ordinal() != Menu.TERMINATE.ordinal())
                    System.out.println();
            }
            System.out.println(" : ");
            key = sc.nextInt();
        }while(key<Menu.ADD_FIRST.ordinal() || key>Menu.TERMINATE.ordinal());
        return Menu.MenuAt(key);
    }

    public static void main(String[] args) {
        Menu menu;                              // 메뉴
        Data data;                              // 추가용 데이터 참조
        Data ptr;                               // 검색용 데이터 참조
        Data temp = new Data();                 // 입력용 데이터

        LinkedList<Data> list = new LinkedList<Data>();     // 리스트 생성

        do{
            switch(menu = SelectMenu()){

                case ADD_FIRST :
                    data = new Data();
                    data.scanData("insert at head", Data.NO | Data.NAME);
                    list.addFirst(data);
                    break;
                
                case ADD_LAST :
                    data = new Data();
                    data.scanData("insert at tail", Data.NO | Data.NAME);
                    list.addLast(data);

                case RMV_FIRST :
                    list.removeFirst();
                    break;

                case RMV_LAST :
                    list.removeLast();
                    break;
                
                case RMV_CRNT :
                    list.removeCurrntnode();
                    break;
                
                case SEARCH_NO :
                    temp.scanData("search", Data.NO);
                    ptr = list.search(temp, Data.NO_ORDER);
                    if(ptr == null) System.out.println("there is no data with that number");
                    else    System.out.println("search succed : "+ptr);
                    break;

                case SEARCH_NAME :
                    temp.scanData("search", Data.NAME);
                    ptr = list.search(temp, Data.NAME_ORDER);
                    if(ptr == null) System.out.println("there is no data with name");
                    else    System.out.println("search succed : "+ptr);
                    break;

                case NEXT :
                    list.next();
                    break;
                
                case PRINT_CRNT :
                    list.printCurrntnode();
                    break;
                
                case DUMP :
                    list.dump();
                    break;

                case CLEAR :
                    list.clear();
                    break;
            }
        }while(menu != Menu.TERMINATE);
    }
}
