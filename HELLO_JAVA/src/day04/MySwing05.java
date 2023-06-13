package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;


import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing05 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private JTextArea ta;
	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing05 frame = new MySwing05();
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
	public MySwing05() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 295, 388);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("출력단수:");
		lbl.setBounds(35, 53, 64, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(120, 50, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				onClick();
				
			}
		});
		btn.setBounds(83, 91, 97, 23);
		contentPane.add(btn);
		
		 ta = new JTextArea();
		ta.setBounds(35, 138, 201, 169);
		contentPane.add(ta);
	}
	
	public void onClick() {
		String num = tf.getText();
		int dan = Integer.parseInt(num);

		String txt = "";
		
		for(int i = 1; i<=9; i++) {
			txt += dan + "*" +i+ "="+ (dan*i)+"\n";
		}
		
		ta.setText(txt);
		
	}
	
}
