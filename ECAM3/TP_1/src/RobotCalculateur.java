
public class RobotCalculateur {
	
	private Clavier clavier = new Clavier();
	
	public double moyenne(double note_1, double note_2) {	
		return (note_1 + note_2) / 2;
	}
	
	public void moyenneEleves() {
		double note_1, note_2;
		double moyenne_classe = 0;
		
		System.out.println("[i] Entrez le nombre d'eleves :");
		int nombre_eleves = clavier.lireEntier();
		
		for (int i = 0; i<nombre_eleves; i++) {
			System.out.println("[i] Entrez la premiere note :");
			note_1 = clavier.lireReelDouble();
			System.out.println("[i] Entrez la seconde note :");
			note_2 = clavier.lireReelDouble();
			System.out.print("[+] La moyenne des 2 notes est : ");
			System.out.println(moyenne(note_1, note_2));
			moyenne_classe = (moyenne_classe + note_1 + note_2);
		}
		
		System.out.print("[+] La moyenne de la classe est : ");
		System.out.println(moyenne_classe / nombre_eleves);
	}
	
}
