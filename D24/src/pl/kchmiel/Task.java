package pl.kchmiel;

import java.util.ArrayList;
import java.util.List;

public class Task {
   int t;
   List<SingleTask> taskList;
   String size;

   public Task(int t, List<SingleTask> taskList) {
      this.t = t;
      this.taskList = taskList;
   }

   public Task() {
      this.taskList = new ArrayList<>();
   }

   public void setSize(String size) {
      this.size = size;
   }

   public void addTask(SingleTask sTask) {
      this.taskList.add(sTask);
   }

   @Override
   public String toString() {
      return super.toString();
   }

   public void print(){

   }

   public void setT(int t){
      this.t = t;
   }
}
