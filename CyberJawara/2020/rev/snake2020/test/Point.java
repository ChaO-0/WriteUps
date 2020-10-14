public class Point {
   private int x;
   private int y;

   public Point(int var1, int var2) {
      this.x = var1;
      this.y = var2;
   }

   public Point(Point var1) {
      this.x = var1.getX();
      this.y = var1.getY();
   }

   public void move(Direction var1, int var2) {
      switch(var1) {
      case UP:
         this.y -= var2;
         break;
      case DOWN:
         this.y += var2;
         break;
      case RIGHT:
         this.x += var2;
         break;
      case LEFT:
         this.x -= var2;
      }

   }

   public int getX() {
      return this.x;
   }

   public int getY() {
      return this.y;
   }

   public Point setX(int var1) {
      this.x = var1;
      return this;
   }

   public Point setY(int var1) {
      this.y = var1;
      return this;
   }

   public boolean equals(Point var1) {
      return this.x == var1.getX() && this.y == var1.getY();
   }

   public String toString() {
      return "(" + this.x + ", " + this.y + ")";
   }

   public boolean intersects(Point var1) {
      return this.intersects(var1, 10);
   }

   public boolean intersects(Point var1, int var2) {
      int var3 = Math.abs(this.x - var1.getX());
      int var4 = Math.abs(this.y - var1.getY());
      return this.equals(var1) || var3 <= var2 && var4 <= var2;
   }
}
