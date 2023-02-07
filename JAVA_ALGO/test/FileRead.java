import java.io.FileInputStream;
import java.io.IOException;

import java.io.BufferedReader;
import java.io.FileReader;

public class FileRead{
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new FileReader("C:/Users/life4/Documents/SW certi/workplace/out.txt"));
        while(true){
            String line = bf.readLine();
            if(line == null) break;
            System.out.println(line);
        }
        bf.close();
    }
}