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

public class MySwing09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_first;
	private JTextField tf_last;
	private JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing09 frame = new MySwing09();
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
	public MySwing09() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 345, 467);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl_first = new JLabel("첫번째수 :");
		lbl_first.setBounds(46, 34, 71, 15);
		contentPane.add(lbl_first);
		
		JLabel lbl_last = new JLabel("끝번째수 :");
		lbl_last.setBounds(46, 76, 71, 15);
		contentPane.add(lbl_last);
		
		tf_first = new JTextField();
		tf_first.setBounds(154, 31, 116, 21);
		contentPane.add(tf_first);
		tf_first.setColumns(10);
		
		tf_last = new JTextField();
		tf_last.setColumns(10);
		tf_last.setBounds(154, 73, 116, 21);
		contentPane.add(tf_last);
		
		JButton btn = new JButton("별그리기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(83, 123, 157, 23);
		contentPane.add(btn);
		
		 ta = new JTextArea();
		ta.setBounds(46, 178, 210, 216);
		contentPane.add(ta);
	}
	
	public String drawStar(int cnt) {
		String ret = "";
		for(int i = 0; i<cnt; i++) {
			ret += "*";
		}
		ret += "\n";
		return ret;
	}
	
	public void myClick() {
		String first = tf_first.getText();
		int first_num = Integer.parseInt(first);
		
		String last = tf_last.getText();
		int last_num = Integer.parseInt(last);
		
		String star = "";
		
		for(int i=first_num; i<=last_num; i++) {
		star += drawStar(i);
		}
		
		
//		for(int i = first_num; i<last_num; i++) {
//			for(int j = first_num; j<last_num; j++) {
//				star += "*";
//			}
//			star += "\n";
//		}
		
		ta.setText(star);
		
	}
	
	
}
