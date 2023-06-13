package day03;

public class OopTest {
	public static void main(String[] args) {
		Car c = new Car();
		System.out.println(c.cnt_wheel);
		System.out.println(c.amount_fuel);
		c.addWheel();
		c.mantank();
		c.onedoller();
		System.out.println(c.cnt_wheel);
		System.out.println(c.amount_fuel);
		
	}
}
