import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		int cc = 0, cc2 = 0, N = ler.nextInt();
		ArrayList<Integer> al = new ArrayList<Integer>();
		
		for (int i = 0; i < N; i++) {
			al.add(ler.nextInt());
		}
		
		int M = ler.nextInt();
		ArrayList<Integer> al2 = new ArrayList<Integer>();
		for (int j = 0; j < M; j++) {
			al2.add(ler.nextInt());
		}
		
		al.removeAll(al2);
//		al.forEach(i -> System.out.print(i + " "));
		for (int j = 0; j < N-M; j++) {
			System.out.print(al.get(j) + " ");
		}
		
		ler.close();
	}
}