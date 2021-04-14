import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;

public class FileWrite {
    public static void main(String[] args) throws Exception{
        // FileOutputStream output = new FileOutputStream("C:/Users/life4/Documents/SW certi/workplace/out.txt");
        FileWriter fw = new FileWriter("C:/Users/life4/Documents/SW certi/workplace/out.txt");

        for(int i=1;i<11;i++){
            String data = i+" th line.\r\n";
            // output.write(data.getBytes());
            fw.write(data);
        }

        fw.close();

        FileWriter fw2 = new FileWriter("C:/Users/life4/Documents/SW certi/workplace/out.txt", true);

        for(int i=11; i<21; i++){
            String data = i+" 번째 줄입니다.\r\n";
            fw2.write(data);
        }

        fw2.close();

    }
}
