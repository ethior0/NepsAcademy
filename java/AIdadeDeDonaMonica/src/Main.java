import java.util.Scanner;

public class Main {

	public static void main( String[] args ) {
		
		Scanner ler = new Scanner( System.in );
		
		int M = ler.nextInt();
		int A = ler.nextInt();
		int B = ler.nextInt();
		int C = M - (A + B);
		
		int max = Math.max(A, B);
		int max2 = Math.max(max, C);
		
		System.out.println(max2);
		
		ler.close();
	}
}
