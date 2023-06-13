package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing10 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private JTextArea ta;
	
	String com = "123";

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing10 frame = new MySwing10();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing10() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 272, 468);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("맞츨수:");
		lbl.setBounds(43, 54, 57, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(112, 51, 87, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("맞춰보기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(43, 91, 156, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(43, 141, 156, 246);
		contentPane.add(ta);
		
		randomCom();
		
	}

	
	public void randomCom() {
		
		int[] num = {
				1,2,3,4,5,   6,7,8,9
		};
		
		for(int i = 0; i<1000; i++) {
			int rnd = (int) (Math.random()*9);
			int a = num[rnd];
			int b = num[0];
			num[0] = a;
			num[rnd] = b;
		}
		
		String com1 = num[0]+"";
		String com2 = num[1]+"";
		String com3 = num[2]+"";
		
		com = com1 + com2 + com3;
		
		System.out.println("com : " + com);
	}
	
	public int getStrike(String com, String mine) {
		int ret = 0;
		String c1 = com.substring(0, 1);
		String c2 = com.substring(1, 2);
		String c3 = com.substring(2, 3);
		
		String m1 = mine.substring(0, 1);
		String m2 = mine.substring(1, 2);
		String m3 = mine.substring(2, 3);
		
		if(c1.equals(m1)) ret++;
		if(c2.equals(m2)) ret++;
		if(c3.equals(m3)) ret++;
		
		return ret;
	}
	
	public int getBall(String com, String mine) {
		int ret = 0;
		String c1 = com.substring(0, 1);
		String c2 = com.substring(1, 2);
		String c3 = com.substring(2, 3);
		
		String m1 = mine.substring(0, 1);
		String m2 = mine.substring(1, 2);
		String m3 = mine.substring(2, 3);
		
		if(c1.equals(m2) || c1.equals(m3)) ret++;
		if(c2.equals(m1) || c2.equals(m3)) ret++;
		if(c3.equals(m1) || c3.equals(m2)) ret++;
		
		return ret;
	}
	
	public void myClick() {
		String mine = tf.getText();
		int s = getStrike(com, mine);
		int b = getBall(com, mine);
		
		String str_old = ta.getText();
		String str_new = mine + " s : " + s + " b : " + b + "\n";
		
		ta.setText(str_old + str_new);
		tf.setText("");
		
		if(s==3) {
			JOptionPane.showMessageDialog(this, "게임 끝\n"+mine);
		}
		
		System.out.println(mine + " s : " + s + "b : " + b);
	}
	
}
