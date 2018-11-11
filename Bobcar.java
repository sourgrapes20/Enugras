import java.util.Scanner;
  public class Bobcar {
    public static void main(String[] args) {

    Scanner userInput = new Scanner(System.in);


    System.out.println("");
    System.out.println("Available cars: 1 for Economy, 2 for Compact, 3 for Standard");
    System.out.print("Please choose the rental car: ");
    int typeCarNum = userInput.nextInt();
    String typeCar = "";
    int carPrice = 0;

    if(typeCarNum==1){
      typeCar = "Economy";
      carPrice = 35;
    }
    if(typeCarNum==2){
      typeCar = "Compact";
      carPrice = 45;
    }
    if(typeCarNum==3){
      typeCar = "Standard";
      carPrice = 95;
    }


    System.out.print("Please enter the number of rental days: ");
    int numDays = userInput.nextInt();

    System.out.print("Club member?: 1 for yes, 0 for no: ");
    int clubMember = userInput.nextInt();

    int discount = 0;
    int platMember = 0;
    double platBonus = 0;

    if(clubMember == 1){

      discount = (numDays/7)*carPrice;

      System.out.print("Platinum Executive Package?: 1 for yes, 0 for no: ");
      platMember = userInput.nextInt();
    }

    System.out.print("Base: " + numDays + " days for a " + typeCar + " @ $" + carPrice +" per day:");
    System.out.println("        $ " + (carPrice * numDays));

    if(clubMember == 1){
      System.out.println("Club Member Discount:                           - $ " + discount);
    }

    if(platMember == 1){
      platBonus = carPrice * numDays * 0.15;
      System.out.println("Platinum Executive Package:                     + $ " + platBonus);
    }

    System.out.println("");
    System.out.println("Total Estimate for Rental:                        $ " + ((carPrice*numDays)-discount+platBonus));
    System.out.println("");


}
}
