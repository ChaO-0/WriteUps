import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Toolkit;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.image.BufferedImage;
import java.awt.image.ImageObserver;
import java.io.File;
import java.io.IOException;
import java.util.Iterator;
import java.util.Random;
import java.util.Timer;
import java.util.TimerTask;
import javax.imageio.ImageIO;
import javax.swing.JPanel;

public class Game extends JPanel {
   private Timer timer;
   private Snake snake;
   private Point cherry;
   private int points = 0;
   private int best = 0;
   private int pivot = 0;
   private int lastPivot = 0;
   private BufferedImage image;
   private GameStatus status;
   private boolean didLoadCherryImage = true;
   private String letters = "";
   private static Font FONT_M = new Font("ArcadeClassic", 0, 24);
   private static Font FONT_M_ITALIC = new Font("ArcadeClassic", 2, 24);
   private static Font FONT_L = new Font("ArcadeClassic", 0, 84);
   private static Font FONT_XL = new Font("ArcadeClassic", 0, 150);
   private static int WIDTH = 760;
   private static int HEIGHT = 520;
   private static int DELAY = 50;
   private static int[] MILESTONES = new int[]{5191, 5271, 5385, 5490, 5612, 5713, 5771, 5803, 5870, 5944, 5994, 6042, 6092, 6140, 6263, 6362, 6466, 6517, 6569, 6685, 6734, 6844, 6947, 7042, 7091, 7144, 7239, 7292, 7344, 7460, 7509, 7562, 7664, 7785, 7834, 7944, 8047, 8172};

   public Game() {
      try {
         this.image = ImageIO.read(new File("cherry.png"));
      } catch (IOException var2) {
         this.didLoadCherryImage = false;
      }

      this.addKeyListener(new Game.KeyListener());
      this.setFocusable(true);
      this.setBackground(Color.black);
      this.setDoubleBuffered(true);
      this.snake = new Snake(WIDTH / 2, HEIGHT / 2);
      this.status = GameStatus.NOT_STARTED;
      this.repaint();
   }

   public void paintComponent(Graphics var1) {
      super.paintComponent(var1);
      this.render(var1);
      Toolkit.getDefaultToolkit().sync();
   }

   private void update() {
      this.snake.move();
      if (this.cherry != null && this.snake.getHead().intersects(this.cherry, 20)) {
         this.snake.addTail();
         this.cherry = null;
         ++this.points;
         if (this.pivot < MILESTONES.length && this.points == MILESTONES[this.pivot]) {
            if (this.pivot > 0) {
               this.letters = this.letters + (char)(MILESTONES[this.pivot] - this.lastPivot);
            }

            this.lastPivot = MILESTONES[this.pivot];
            ++this.pivot;
         }
      }

      if (this.cherry == null) {
         this.spawnCherry();
      }

      this.checkForGameOver();
   }

   private void reset() {
      this.points = 0;
      this.cherry = null;
      this.snake = new Snake(WIDTH / 2, HEIGHT / 2);
      this.setStatus(GameStatus.RUNNING);
   }

   private void setStatus(GameStatus var1) {
      switch(var1) {
      case RUNNING:
         this.timer = new Timer();
         this.timer.schedule(new Game.GameLoop(), 0L, (long)DELAY);
         break;
      case PAUSED:
         this.timer.cancel();
      case GAME_OVER:
         this.timer.cancel();
         this.best = this.points > this.best ? this.points : this.best;
      }

      this.status = var1;
   }

   private void togglePause() {
      this.setStatus(this.status == GameStatus.PAUSED ? GameStatus.RUNNING : GameStatus.PAUSED);
   }

   private void checkForGameOver() {
      Point var1 = this.snake.getHead();
      boolean var2 = var1.getX() <= 20 || var1.getX() >= WIDTH + 10 || var1.getY() <= 40 || var1.getY() >= HEIGHT + 30;
      boolean var3 = false;

      Point var5;
      for(Iterator var4 = this.snake.getTail().iterator(); var4.hasNext(); var3 = var3 || var1.equals(var5)) {
         var5 = (Point)var4.next();
      }

      if (var2 || var3) {
         this.setStatus(GameStatus.GAME_OVER);
      }

   }

   public void drawCenteredString(Graphics var1, String var2, Font var3, int var4) {
      FontMetrics var5 = var1.getFontMetrics(var3);
      int var6 = (WIDTH - var5.stringWidth(var2)) / 2;
      var1.setFont(var3);
      var1.drawString(var2, var6, var4);
   }

   private void render(Graphics var1) {
      Graphics2D var2 = (Graphics2D)var1;
      var2.setColor(new Color(53, 220, 8));
      var2.setFont(FONT_M);
      if (this.status == GameStatus.NOT_STARTED) {
         this.drawCenteredString(var2, "SNAKE", FONT_XL, 200);
         this.drawCenteredString(var2, "GAME", FONT_XL, 300);
         this.drawCenteredString(var2, "Press  any  key  to  begin", FONT_M_ITALIC, 330);
      } else {
         Point var3 = this.snake.getHead();
         var2.drawString("SCORE: " + String.format("%04d", this.points), 20, 30);
         var2.drawString("BEST: " + String.format("%04d", this.best), 660, 30);
         if (this.cherry != null) {
            if (this.didLoadCherryImage) {
               var2.drawImage(this.image, this.cherry.getX(), this.cherry.getY(), 60, 60, (ImageObserver)null);
            } else {
               var2.setColor(Color.RED);
               var2.fillOval(this.cherry.getX(), this.cherry.getY(), 10, 10);
               var2.setColor(new Color(53, 220, 8));
            }
         }

         if (this.pivot == MILESTONES.length) {
            this.drawCenteredString(var2, this.letters, FONT_M_ITALIC, 330);
            this.drawCenteredString(var2, "Nice", FONT_L, 300);
         }

         if (this.status == GameStatus.GAME_OVER) {
            this.drawCenteredString(var2, "Press  enter  to  start  again", FONT_M_ITALIC, 330);
            this.drawCenteredString(var2, "GAME OVER", FONT_L, 300);
         }

         if (this.status == GameStatus.PAUSED) {
            var2.drawString("Paused", 600, 14);
         }

         var2.setColor(new Color(74, 245, 14));
         var2.fillRect(var3.getX(), var3.getY(), 10, 10);
         int var4 = 0;

         for(int var5 = this.snake.getTail().size(); var4 < var5; ++var4) {
            Point var6 = (Point)this.snake.getTail().get(var4);
            var2.fillRect(var6.getX(), var6.getY(), 10, 10);
         }

         var2.setColor(new Color(71, 128, 0));
         var2.setStroke(new BasicStroke(4.0F));
         var2.drawRect(20, 40, WIDTH, HEIGHT);
      }
   }

   public void spawnCherry() {
      this.cherry = new Point((new Random()).nextInt(WIDTH - 60) + 20, (new Random()).nextInt(HEIGHT - 60) + 40);
   }

   private class GameLoop extends TimerTask {
      public void run() {
         Game.this.update();
         Game.this.repaint();
      }
   }

   private class KeyListener extends KeyAdapter {
      public void keyPressed(KeyEvent var1) {
         int var2 = var1.getKeyCode();
         if (Game.this.status == GameStatus.RUNNING) {
            switch(var2) {
            case 37:
               Game.this.snake.turn(Direction.LEFT);
               break;
            case 38:
               Game.this.snake.turn(Direction.UP);
               break;
            case 39:
               Game.this.snake.turn(Direction.RIGHT);
               break;
            case 40:
               Game.this.snake.turn(Direction.DOWN);
            }
         }

         if (Game.this.status == GameStatus.NOT_STARTED) {
            Game.this.setStatus(GameStatus.RUNNING);
         }

         if (Game.this.status == GameStatus.GAME_OVER && var2 == 10) {
            Game.this.reset();
         }

         if (var2 == 80) {
            Game.this.togglePause();
         }

      }
   }
}
