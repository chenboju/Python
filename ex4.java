import java.util.Scanner;

public class ex4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
     Scanner in = new Scanner(System.in);
     System.out.print("請輸入任意正整數  : ");
      int a =in.nextInt();
      int sum =0;
      for(int i =1;i<=a;i++) {
     		   System.out.print(i+"*"+i+ "="+ i*i+"\t");
     	   
      }
            
	}

}
