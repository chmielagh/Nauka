package pl.kchmiel;

import java.util.List;

public class SingleTask {
   int x,y,n;
   List<Coords> coordsList;

   public SingleTask(int n, int x, int y, List<Coords> coordsList){
      this.n = n;
      this.x = x;
      this.y = y;
      this.coordsList = coordsList;
   }
}
