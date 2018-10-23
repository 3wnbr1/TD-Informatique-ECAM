import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.LinkedList;

public class LecteurFichierTrain {
	/**
	 * LecteurFichierTrain Version 1.17
	 */
	private LinkedList<Gare> gares;
	private ArrayList<RegulariteMensuelle> lignesRM;
	private boolean erreurLecture;

	public LecteurFichierTrain() {
		gares = new LinkedList<Gare>();
		lignesRM = new ArrayList<RegulariteMensuelle>();
		erreurLecture = false;
	}

	public RegulariteMensuelle[] getfichierTrain() {
		int i;
		if (lignesRM.size() < 1)
			lirefichier();
		if (erreurLecture)
			return null;
		RegulariteMensuelle[] tab = new RegulariteMensuelle[lignesRM.size()];
		for (i = 0; i < tab.length; i++) {
			tab[i] = lignesRM.get(i);
		}

		System.out.println("Lecture : " + gares.size() + " Gares, " + lignesRM.size() + " lignes");
		// System.out.println(gares);
		return tab;
	}

	// Le fichier doit �tre dans le dossier du projet (et non dans scr)
	private void lirefichier() {
		String nomFichier = "regularite-mensuelle-tgv.csv";
		// String nomFichier = "regularite-mensuelle-ter.csv";
		BufferedReader entree;
		RegulariteMensuelle rmTemp;
		try {
			entree = new BufferedReader(new FileReader(nomFichier));
			String ligne = entree.readLine();
			while (ligne != null) {
				ligne = entree.readLine();
				if (ligne != null) {
					rmTemp = traiterligne(ligne);
					if (rmTemp != null)
						lignesRM.add(rmTemp);
				}
			}
			entree.close();
		} catch (Exception e) {
			erreurLecture = true;
			e.printStackTrace();
		}
	}

	private RegulariteMensuelle traiterligne(String ligne) {
		// System.out.println(ligne);
		RegulariteMensuelle rmTemp;
		String[] tab = ligne.split(";");
		if (tab.length < 8) {
			// System.out.println("Non parsable : " + ligne);
			return null;
		}

		Gare depart = trouverAjouterGare(tab[3]);
		Gare arrivee = trouverAjouterGare(tab[4]);

		if (tab[7].length() < 1)
			tab[7] = "0.0";
		if (tab[13].length() < 1)
			tab[13] = "0.0";

		try {
			rmTemp = new RegulariteMensuelle((int) Double.parseDouble(tab[1]), Integer.parseInt(tab[0]), depart,
					arrivee, Double.parseDouble(tab[6]), Double.parseDouble(tab[7]), Double.parseDouble(tab[13]));
		} catch (Exception e) {
			System.out.println("Non parsable : " + ligne);
			rmTemp = null;
		}

		return rmTemp;
	}

	private Gare trouverAjouterGare(String nomGare) {
		Gare g = null;
		int i;
		int id;
		for (i = 0; i < gares.size(); i++) {
			if (gares.get(i).getNom().equals(nomGare)) {
				g = gares.get(i);
			}
		}
		if (g == null) {
			if (gares.size() == 0)
				id = 0;
			else
				id = gares.getLast().getIdGare() + 1;
			g = new Gare(id, nomGare);
			gares.add(g);
		}
		return g;
	}

}
