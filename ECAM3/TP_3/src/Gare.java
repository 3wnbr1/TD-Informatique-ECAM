
public class Gare {
	
	private int idGare;
	private String nom;
	
	public Gare(int idGareP, String nomP) {
		this.idGare = idGareP;
		this.nom = nomP;
	}
	
	public int getIdGare() {
		return idGare;
	}
	
	public String getNom() {
		return nom;
	}

	@Override
	public String toString() {
		return "Gare [idGare=" + idGare + ", nom=" + nom + "]";
	}

}
