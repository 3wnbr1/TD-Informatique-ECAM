import java.io.*;



/**
 * Classe : Clavier                                                          
 *  Auteur :                                              
 *  Date de création : 12/09/2003                                             
 *  Description : la classe définie des méthodes de saisie des types primitifs
 *                à partir du clavier   
 */
public class Clavier {
	/**
	 * Méthode de lecture d'une chaîne de caractères au clavier
	 * Paramètres : aucun  
	 * Retour : la chaîne lue
	 */
	public  String lireChaine() {
		String sChaine = null;
		//System.out.println("Entrez un valeur ou une chaîne :");
		try  {
			// lecture d'une chaîne de caracères au clavier
			BufferedReader brLecteur ;
			brLecteur = new BufferedReader(new InputStreamReader(System.in));
			sChaine = brLecteur.readLine();
		}
		catch (IOException ee) {
			System.out.println("Erreur de lecture clavier");
		}
		return sChaine;  // retourne la chaîne lue
	}

	/**
	 * Méthode de lecture d'un entier au clavier
	 * @return : un entier
	 */
	public  int lireEntier() {
		String sChaine = lireChaine(); // appel de la méthode lireChaîne
		// conversion de la chaîne en entier et retour de la valeur
		return Integer.parseInt(sChaine.trim());
	}

	/**
	 * Méthode de lecture d'un réel simple au clavier
	 * @return : un réel 
	 */
	public  float lireReelSimple() {
		String sChaine = lireChaine();
		// conversion de la chaîne en réel et retour de la valeur
		return Float.parseFloat(sChaine.trim());
	}

	/**
	 * Méthode de lecture d'un réel double précision au clavier
	 * @return : un réel
	 */
	public  double lireReelDouble() {
		String sChaine = lireChaine();
		// conversion de la chaîne en réel et retour de la valeur
		return Double.parseDouble(sChaine.trim());
	}

}