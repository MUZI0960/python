package day04;

import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;
import javax.swing.SwingConstants;

public class MySwing07_2 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private JButton btn1, btn2, btn3, btn4, btn5,btn6,btn7,btn8, btn9, btn0;
	private String result;
	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing07 frame = new MySwing07();
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
	public MySwing07_2() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 305, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setHorizontalAlignment(SwingConstants.RIGHT);
		tf.setBounds(44, 35, 196, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		btn1 = new JButton("1");
		btn1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				result += btn1.getText();
				tf.setText(result);
			}
		});
		btn1.setBounds(44, 82, 63, 23);
		contentPane.add(btn1);
		
		btn2 = new JButton("2");
		btn2.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				result += btn2.getText();
				tf.setText(result);
			}
		});
		btn2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn2.setBounds(119, 82, 55, 23);
		contentPane.add(btn2);
		
		btn3 = new JButton("3");
		btn3.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				result += btn3.getText();
				tf.setText(result);
			}
		});
		btn3.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn3.setBounds(186, 82, 55, 23);
		contentPane.add(btn3);
		
		btn4 = new JButton("4");
		btn4.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				result += btn4.getText();
				tf.setText(result);
			}
		});
		btn4.setBounds(44, 123, 63, 23);
		contentPane.add(btn4);
		
		btn5 = new JButton("5");
		btn5.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				result += btn5.getText();
				tf.setText(result);
			}
		});
		btn5.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn5.setBounds(119, 123, 55, 23);
		contentPane.add(btn5);
		
		btn6 = new JButton("6");
		btn6.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				result += btn6.getText();
				tf.setText(result);
			}
		});
		btn6.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn6.setBounds(186, 123, 55, 23);
		contentPane.add(btn6);
		
		btn7 = new JButton("7");
		btn7.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				result += btn7.getText();
				tf.setText(result);
			}
		});
		btn7.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn7.setBounds(44, 166, 63, 23);
		contentPane.add(btn7);
		
		btn8 = new JButton("8");
		btn8.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				result += btn8.getText();
				tf.setText(result);
			}
		});
		btn8.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn8.setBounds(119, 166, 55, 23);
		contentPane.add(btn8);
		
		btn9 = new JButton("9");
		btn9.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				result += btn9.getText();
				tf.setText(result);
			}
		});
		btn9.setBounds(186, 166, 55, 23);
		contentPane.add(btn9);
		
		btn0 = new JButton("0");
		btn0.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				JButton imsi = (JButton)e.getSource();
				System.out.println(e.getSource());
				
			}
		});
		btn0.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				result += btn0.getText();
				tf.setText(result);
			}
		});
		btn0.setBounds(44, 202, 63, 23);
		contentPane.add(btn0);
		
		JButton btnCall = new JButton("CALL");
		
		btnCall.setBounds(119, 202, 117, 23);
		contentPane.add(btnCall);
		
		btn1.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e)  { myclick(e);} });
		btn2.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e)  { myclick(e);} });
		btn3.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e)  { myclick(e);} });
		btn4.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e)  { myclick(e);} });
		btn5.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e)  { myclick(e);} });
		
		btn6.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e)  { myclick(e);} });
		btn7.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e)  { myclick(e);} });
		btn8.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e)  { myclick(e);} });
		btn9.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e)  { myclick(e);} });
		btn0.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e)  { myclick(e);} });
		
		btnCall.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e)  { mycall();} });
	}

	public void myclick(MouseEvent e) {
		JButton imsi = (JButton) e.getSource();
		String str_new = imsi.getText();
		String str_old = tf.getText();
		
		tf.setText(str_old+str_new);
	}
	
	public void mycall() {
		String str_tel = tf.getText();
		JOptionPane.showMessageDialog(this, "Calling\n"+str_tel);
	}
	
}
