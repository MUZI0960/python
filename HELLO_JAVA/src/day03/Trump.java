package day03;

public class Trump {
	int cnt_building = 50;
	
	public void maemae(int cnt) {
		cnt_building += cnt;
	}
	
	public static void main(String[] args) {
		Trump t = new Trump();
		System.out.println(t.cnt_building);
		t.maemae(7);
		System.out.println(t.cnt_building);
	}
	
}
