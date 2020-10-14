import java.awt.Component;
import java.awt.EventQueue;
import javax.swing.JFrame;

public class Main extends JFrame {
   public Main() {
      this.initUI();
   }

   private void initUI() {
      this.add(new Game());
      this.setTitle("Snake 1.1");
      this.setSize(800, 600);
      this.setLocationRelativeTo((Component)null);
      this.setResizable(false);
      this.setDefaultCloseOperation(3);
   }

   public static void main(String[] var0) {
      EventQueue.invokeLater(() -> {
         Main va3 = new Main();
         va3.setVisible(true);
      });
   }
}
