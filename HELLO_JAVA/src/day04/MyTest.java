package day04;

public class MyTest {
	
	public static void showDan(int dan) {
		System.out.println(dan + "*" + 1 + "=" + (1*dan));
		System.out.println(dan + "*" + 2 + "=" + (2*dan));
		System.out.println(dan + "*" + 3 + "=" + (3*dan));
		System.out.println(dan + "*" + 4 + "=" + (4*dan));
		System.out.println(dan + "*" + 5 + "=" + (5*dan));
		
		System.out.println(dan + "*" + 6 + "=" + (6*dan));
		System.out.println(dan + "*" + 7 + "=" + (7*dan));
		System.out.println(dan + "*" + 8 + "=" + (8*dan));
		System.out.println(dan + "*" + 9 + "=" + (9*dan));
	}
	
	public static void main(String[] args) {
		
		showDan(9);
		showDan(7);
		showDan(5);
		showDan(2);
		
//		for(int i = 9; i>=5; i-=2) {
//			
//			for(int j =1; j<=9; j++) {
//				System.out.println(i+"*"+j +"="+i*j);
//			}
//			
//		}
		
		
	}
}
