package pl.kchmiel;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

   private static List<String> files;

   public static void main(String[] args) throws IOException {
      initFileNames();
      String input = readInput();
      Scanner scanner = new Scanner(input);
      int t = Integer.parseInt(scanner.nextLine());
      int tTemp = t;
      List<SingleTask> tasks = new ArrayList<>();

      int[] sizeInt = new int[2];

      Task task = new Task();
      task.setT(t);
      while(t>0){
         String size = (scanner.nextLine());
         int n = Integer.parseInt(scanner.nextLine());
         List<Coords> coordsList = new ArrayList<>();
         int m = n;
         while(m>0){
            coordsList.add(parseCoordLine(scanner.nextLine()));
            m--;
         }
         sizeInt[0] = Integer.parseInt(size.split(" ")[0]);
         sizeInt[1] = Integer.parseInt(size.split(" ")[1]);
         SingleTask sTask = new SingleTask(n, sizeInt[0], sizeInt[1], coordsList);
         tasks.add(sTask);
         task.addTask(sTask);
         t--;
      }
      System.out.println(task);

      writeOutput();
   }

   private static void writeOutput() throws FileNotFoundException, UnsupportedEncodingException {
      PrintWriter writer = new PrintWriter("flow001.ans", "UTF-8");
      writer.println("5");
      writer.println("EESEN");
      writer.println("E");
      writer.println("E");
      writer.println("SSENEEN");
      writer.println("E");
      writer.println("5");
      writer.println("EESEN");
      writer.println("EESEN");
      writer.println("EESEN");
      writer.println("EESEN");
      writer.println("EESEN");
      writer.println("7");
      writer.println("EESEN");
      writer.println("EESEN");
      writer.println("EESEN");
      writer.println("EESEN");
      writer.println("EESEN");
      writer.println("EESEN");
      writer.println("EESEN");
      writer.close();
   }

   private static Coords parseCoordLine(String next) {
      String[] coords = next.split(" ");
      Coords result = new Coords(
            Integer.parseInt(coords[0]),
            Integer.parseInt(coords[1]),
            Integer.parseInt(coords[2]),
            Integer.parseInt(coords[3]));
      return result;
   }

   private static void initFileNames() {
      files = new ArrayList<>();
      files.add("flow01.in");
   }

   private static String readInput() throws IOException {
      BufferedReader br = new BufferedReader(new FileReader("res_flow/"+files.get(0)));
      try {
         StringBuilder sb = new StringBuilder();
         String line = br.readLine();

         while (line != null) {
            sb.append(line);
            sb.append(System.lineSeparator());
            line = br.readLine();
         }
         String everything = sb.toString();
         return everything;
      } catch (IOException e) {

      } finally {
         br.close();
      }
      return "";
   }
}
