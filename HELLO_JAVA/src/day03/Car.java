package day03;

public class Car extends Vehicle{
	int amount_fuel = 0;
	
	public Car() {
		super();
	}
	
	public void mantank() {
		amount_fuel = 100;
	}
	
	public void onedoller() {
		if(amount_fuel>=100) {
			System.out.println("만땅이유");
			return;
		}
		amount_fuel++;
	}
	
}
