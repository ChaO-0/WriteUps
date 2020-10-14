import java.util.ArrayList;

public class Snake {
   private Direction direction;
   private Point head;
   private ArrayList<Point> tail;

   public Snake(int var1, int var2) {
      this.head = new Point(var1, var2);
      this.direction = Direction.RIGHT;
      this.tail = new ArrayList();
      this.tail.add(new Point(0, 0));
      this.tail.add(new Point(0, 0));
      this.tail.add(new Point(0, 0));
   }

   public void move() {
      ArrayList var1 = new ArrayList();
      int var2 = 0;

      for(int var3 = this.tail.size(); var2 < var3; ++var2) {
         Point var4 = (Point)this.tail.get(var2);
         Point var5 = var2 == 0 ? this.head : (Point)this.tail.get(var2 - 1);
         var1.add(new Point(var5.getX(), var5.getY()));
      }

      this.tail = var1;
      this.head.move(this.direction, 10);
   }

   public void addTail() {
      Point var1 = (Point)this.tail.get(this.tail.size() - 1);
      this.tail.add(new Point(-10, -10));
   }

   public void turn(Direction var1) {
      if (var1.isX() && this.direction.isY() || var1.isY() && this.direction.isX()) {
         this.direction = var1;
      }

   }

   public ArrayList<Point> getTail() {
      return this.tail;
   }

   public Point getHead() {
      return this.head;
   }
}
