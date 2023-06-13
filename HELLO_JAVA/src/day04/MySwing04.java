package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.ArrayList;
import java.util.List;

public class MySwing04 extends JFrame {

	private JPanel contentPane;
	private JLabel lbl1;
	private JLabel lbl2;
	private JLabel lbl3;
	private JLabel lbl4;
	private JLabel lbl5;
	private JLabel lbl6;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing04 frame = new MySwing04();
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
	public MySwing04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lbl1 = new JLabel("__");
		lbl1.setBounds(41, 25, 27, 15);
		contentPane.add(lbl1);
		
		lbl3 = new JLabel("__");
		lbl3.setBounds(119, 25, 27, 15);
		contentPane.add(lbl3);
		
		lbl4 = new JLabel("__");
		lbl4.setBounds(158, 25, 27, 15);
		contentPane.add(lbl4);
		
		lbl5 = new JLabel("__");
		lbl5.setBounds(197, 25, 27, 15);
		contentPane.add(lbl5);
		
		lbl6 = new JLabel("__");
		lbl6.setBounds(236, 25, 27, 15);
		contentPane.add(lbl6);
		
		lbl2 = new JLabel("__");
		lbl2.setBounds(80, 25, 27, 15);
		contentPane.add(lbl2);
		
		JButton btn = new JButton("로또생성하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				onClick();
			}
		});
		btn.setBounds(97, 85, 97, 23);
		contentPane.add(btn);
	}

	public void onClick() {
		int[] num = {
				1,2,3,4,5,   6,7,8,9,10,
			    11,12,13,14,15,   16,17,18,19,20,
			    21,22,23,24,25,   26,27,28,29,30,
			    31,32,33,34,35,   36,37,38,39,40,
			    41,42,43,44,45
		};
		
		for(int i = 0; i<1000; i++) {
			int rnd = (int) (Math.random()*45);
			int a = num[rnd];
			int b = num[0];
			num[0] = a;
			num[rnd] = b;
		}
		
		for(int i=0; i<num.length; i++) {
			System.out.println(i+":"+num[i]);
		}
		
		lbl1.setText(num[0]+"");
		lbl2.setText(num[1]+"");
		lbl3.setText(num[2]+"");
		lbl4.setText(num[3]+"");
		lbl5.setText(num[4]+"");
		lbl6.setText(num[5]+"");
		
		
		
	}
	
}
