import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		String risadaR, risada = ler.next();
		risada = risada.replaceAll("[^aeiou]", "");
		sb.append(risada);
		risadaR = sb.reverse().toString();
		
		System.out.println(risada.equals(risadaR) ? "S" : "N");
		
		ler.close();
	}
}
