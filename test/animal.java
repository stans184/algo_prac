public class animal {
    String name;

    public void setName(String name){
        this.name = name;
    }
}

class dog extends animal{
    public void sleep(){
        System.out.println(this.name + " zzz");
    }
}

class HouseDog extends dog{
    public HouseDog(String name){
        this.setName(name);
    }

    public HouseDog(int type){
        if(type ==1){
            this.setName("yorkshire");
        }else if(type==2){
            this.setName("maltiz");
        }
    }

    public void sleep(){
        System.out.println(this.name+ " zzz");
    }

    public void sleep(int hour){
        System.out.println(this.name+" zzz in house for "+hour+" hours");
    }

    public static void main(String[] args){
        HouseDog housedog1 = new HouseDog("happy");
        HouseDog housedog2 = new HouseDog(2);
        System.out.println(housedog1.name);
        System.out.println(housedog2.name);

    }
}
