import java.util.Scanner;

public class Main {

	public static void main( String[] args ) {
		
		Scanner ler = new Scanner( System.in );
		
		String sen = ler.nextLine();
		String array[] = sen.split(" ");
		
		// talvez tinha jeitos mais faceis, mas a vida nem sempre e um morango
		for ( int i = 0; i < array.length; i++ ) {
			String word = "";
			for (int j = 0; j < array[i].length(); j++) {
				if (j == 0) {
					word += array[i].toUpperCase().charAt(0);
				} else {
					word += array[i].toLowerCase().charAt(j);
				}
			}
			System.out.print(word + " ");
		}
		
		
		ler.close();
	}
}
