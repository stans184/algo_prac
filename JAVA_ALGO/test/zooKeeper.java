public class zooKeeper {
    public void feed(Predator predator){
        System.out.println("feed "+predator.getFood());
    }
    // interface의 선언으로 해당 method의 개수가 줄어듬, main class가 조금더 단순해짐
    // 동물들의 종류에서 벗어난, 조금더 독자적인 class로 사용가능

    public static void main(String[] args){
        zooKeeper zk = new zooKeeper();
        Tiger tiger = new Tiger();
        Lion lion = new Lion();
        Crocodile crocodile = new Crocodile();
        zk.feed(tiger);
        zk.feed(lion);
        zk.feed(crocodile);
    }
}