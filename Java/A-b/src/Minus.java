import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Minus {
    public static void main(String[] args) {
        try {

            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));//System.in = 콘솔 입력 // static InputStream 변수명 in

            String[] b = br.readLine().split("\\s+" + "");
            for (String i : b){
                Integer.parseInt(i);
            }
//            System.out.println());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
