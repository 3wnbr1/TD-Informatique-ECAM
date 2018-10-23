
public class RegulariteMensuelle {
	/**
	 * RegulariteMensuelle
	 * Version 1.17
	 */
	private int mois;
	private int annee;
	private Gare depart;
	private Gare arrivee;
	private double nbTotalTrains;
	private double nbTotalTrainsAnnules;
	private double nbTotalTrainsRetard;
	
	public RegulariteMensuelle(int mois, int annee, Gare depart, Gare arrivee,
			double nbTotalTrains, double nbTotalTrainsAnnules, double nbTotalTrainsRetard) {
		this.mois = mois;
		this.annee = annee;
		this.depart = depart;
		this.arrivee = arrivee;
		this.nbTotalTrains = nbTotalTrains;
		this.nbTotalTrainsAnnules = nbTotalTrainsAnnules;
		this.nbTotalTrainsRetard = nbTotalTrainsRetard;
	}

	public RegulariteMensuelle(int mois, int annee, Gare depart, Gare arrivee) {
		this.mois = mois;
		this.annee = annee;
		this.depart = depart;
		this.arrivee = arrivee;
		this.nbTotalTrains = 0;
		this.nbTotalTrainsAnnules = 0;
		this.nbTotalTrainsRetard = 0;
	}
	
	@Override
	public String toString() {
		return "RegulariteMensuelle [mois=" + mois + ", annee=" + annee
				+ ", depart=" + depart + ", arrivee=" + arrivee
				+ ", nbTotalTrains=" + nbTotalTrains
				+ ", nbTotalTrainsAnnules=" + nbTotalTrainsAnnules
				+ ", nbTotalTrainsRetard=" + nbTotalTrainsRetard + "]";
	}

	/*****************Accesseurs********************/
	

	public double getNbTotalTrains() {
		return nbTotalTrains;
	}

	public void setNbTotalTrains(double nbTotalTrains) {
		this.nbTotalTrains = nbTotalTrains;
	}

	public double getNbTotalTrainsAnnules() {
		return nbTotalTrainsAnnules;
	}

	public void setNbTotalTrainsAnnules(double nbTotalTrainsAnnules) {
		this.nbTotalTrainsAnnules = nbTotalTrainsAnnules;
	}

	public double getNbTotalTrainsRetard() {
		return nbTotalTrainsRetard;
	}

	public void setNbTotalTrainsRetard(double nbTotalTrainsRetard) {
		this.nbTotalTrainsRetard = nbTotalTrainsRetard;
	}

	public int getMois() {
		return mois;
	}

	public int getAnnee() {
		return annee;
	}

	public Gare getDepart() {
		return depart;
	}

	public Gare getArrivee() {
		return arrivee;
	}


}
