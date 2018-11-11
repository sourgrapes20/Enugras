import java.util.Scanner;
  public class DataAnalyze{
    public static void main(String[] args) {

    Scanner userInput = new Scanner(System.in);
    System.out.print("Please enter sample size: ");
    int sampleSize = userInput.nextInt();
    int[][] dataArray = new int[sampleSize][4];


    if(sampleSize==0){
      return;
    }


    for(int counter=0;counter<4;counter++){
      System.out.println("Enter the numbers for Trial " + counter);
        for(int counter2 =0;counter2<sampleSize;counter2++){
          System.out.print("Enter sample #" + counter2 + ": ");
          Integer sampleData = userInput.nextInt();
          dataArray[counter2][counter] = sampleData;
        }
      }
    System.out.print("\n");

    /*
    for(int i=0;i<dataArray.length;i++){
      for(int j=0;j<4;j++){
        System.out.println(dataArray[i][j]);
      }
    }
    printing the stored values to see if they were caught
    */


    System.out.println("\tSample # \t Trial 1 \t Trial 2 \t Trial 3 \t Trial 4");
    System.out.println("\t-------------------------------------------------------------------------");

    for(int counter3=0;counter3<sampleSize;counter3++){
      System.out.print("\t" + (counter3) + "\t" + "\t" + " "+ dataArray[counter3][0]);
      System.out.print("\t" +  "\t" + " " + dataArray[counter3][1]);
      System.out.print("\t" +  "\t" + " " + dataArray[counter3][2]);
      System.out.println("\t" +  "\t" + " " + dataArray[counter3][3]);
      }


    int average1 = 0;
    int[] averageSet = new int[4];

    for(int counter5=0;counter5<4;counter5++){
      for(int counter4=0;counter4<sampleSize;counter4++){
        average1+=dataArray[counter4][counter5];
      }
      averageSet[counter5] = (average1/sampleSize);
      average1 = 0;
    }

    System.out.print("\tAverage: \t ");
    for(int counter6 = 0;counter6<4;counter6++){
      System.out.print(averageSet[counter6]+ "\t\t ");
    }

    System.out.println("\n");


    int highestValue = averageSet[0];
    int lowestValue = averageSet[0];
    for(int counter6=0;counter6<averageSet.length;counter6++){
        if(averageSet[counter6]>highestValue){
          highestValue = averageSet[counter6];
        }
        if(averageSet[counter6]<lowestValue){
          lowestValue = averageSet[counter6];
        }
    }
    System.out.println("Min average: " + lowestValue);
    System.out.println("Max average: " + highestValue);

    if(highestValue==lowestValue){
      System.out.println("The trials match EXACTLY!");
    }
    else if(highestValue < (lowestValue*2)){
      System.out.println("The trials concur with each other!");
    }
    else{
      System.out.println("The trials do NOT concur.");
    }

    System.out.println("");



    }
  }
