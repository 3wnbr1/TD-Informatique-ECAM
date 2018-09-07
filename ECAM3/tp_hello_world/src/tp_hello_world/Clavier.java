package tp_hello_world;

import java.io.*;


/**
 * Classe : Clavier                                                          
 *  Auteur :                                              
 *  Date de cr�ation : 12/09/2003                                             
 *  Description : la classe d�finie des m�thodes de saisie des types primitifs
 *                � partir du clavier   
 */
public class Clavier {
	/**
	 * M�thode de lecture d'une cha�ne de caract�res au clavier
	 * Param�tres : aucun  
	 * Retour : la cha�ne lue
	 */
	public  String lireChaine() {
		String sChaine = null;
		//System.out.println("Entrez un valeur ou une cha�ne :");
		try  {
			// lecture d'une cha�ne de carac�res au clavier
			BufferedReader brLecteur ;
			brLecteur = new BufferedReader(new InputStreamReader(System.in));
			sChaine = brLecteur.readLine();
		}
		catch (IOException ee) {
			System.out.println("Erreur de lecture clavier");
		}
		return sChaine;  // retourne la cha�ne lue
	}

	/**
	 * M�thode de lecture d'un entier au clavier
	 * @return : un entier
	 */
	public  int lireEntier() {
		String sChaine = lireChaine(); // appel de la m�thode lireCha�ne
		// conversion de la cha�ne en entier et retour de la valeur
		return Integer.parseInt(sChaine.trim());
	}

	/**
	 * M�thode de lecture d'un r�el simple au clavier
	 * @return : un r�el 
	 */
	public  float lireReelSimple() {
		String sChaine = lireChaine();
		// conversion de la cha�ne en r�el et retour de la valeur
		return Float.parseFloat(sChaine.trim());
	}

	/**
	 * M�thode de lecture d'un r�el double pr�cision au clavier
	 * @return : un r�el
	 */
	public  double lireReelDouble() {
		String sChaine = lireChaine();
		// conversion de la cha�ne en r�el et retour de la valeur
		return Double.parseDouble(sChaine.trim());
	}

}