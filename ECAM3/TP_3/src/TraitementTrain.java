import java.util.ArrayList;

public class TraitementTrain {
	
	
	private RegulariteMensuelle[] tabRM;
	
	
	public TraitementTrain(RegulariteMensuelle[] tabRMParam) {
		this.tabRM = tabRMParam;
	}
	
	public void afficher() {
		for (int i = 0; i < this.tabRM.length; i++) {
			System.out.println(this.tabRM[i]);
		}
		System.out.println(this.tabRM.length);
	}
	
	public int nombreDeRM(int idGareDepart, int idGareArrivee) {
		ArrayList<RegulariteMensuelle> matching = new ArrayList<RegulariteMensuelle>();
		for (int i = 0; i < this.tabRM.length; i++) {
			if ((tabRM[i].getDepart().getIdGare() == idGareDepart) && (tabRM[i].getArrivee().getIdGare()) == idGareArrivee) {
				matching.add(tabRM[i]);
			}
		}
		return matching.size();
	}
	
	public String minDate() {
		int monthsNumber = tabRM[0].getMois() + tabRM[0].getAnnee() * 12;
		RegulariteMensuelle smallestRM = tabRM[0];
		for (int i = 1; i < this.tabRM.length; i++) {
			if ((tabRM[i].getMois() + tabRM[i].getAnnee() * 12) < monthsNumber) {
				monthsNumber = (tabRM[i].getMois() + tabRM[i].getAnnee() * 12);
				smallestRM = tabRM[i];
			}
		}
		return smallestRM.getMois() + " " + smallestRM.getAnnee();
	}
	
	public String maxDate() {
		int monthsNumber = tabRM[0].getMois() + tabRM[0].getAnnee() * 12;
		RegulariteMensuelle maxRM = tabRM[0];
		for (int i = 1; i < this.tabRM.length; i++) {
			if ((tabRM[i].getMois() + tabRM[i].getAnnee() * 12) > monthsNumber) {
				monthsNumber = (tabRM[i].getMois() + tabRM[i].getAnnee() * 12);
				maxRM = tabRM[i];
			}
		}
		return maxRM.getMois() + " " + maxRM.getAnnee();
	}
	
	public double pcRegularite(int idGareDepart, int idGareArrivee) {
		double nombreTrainsPonctuels = 0;
		double nombreTrainsTotal = 0;
		for (int i = 0; i < this.tabRM.length; i++) {
			if ((tabRM[i].getDepart().getIdGare() == idGareDepart) && (tabRM[i].getArrivee().getIdGare()) == idGareArrivee) {
				nombreTrainsTotal += tabRM[i].getNbTotalTrains();
				nombreTrainsPonctuels += (tabRM[i].getNbTotalTrains() - tabRM[i].getNbTotalTrainsAnnules() - tabRM[i].getNbTotalTrainsRetard());
			}
		}
		return (nombreTrainsPonctuels / nombreTrainsTotal * 100);
	}
	
	public int[] histogrammeRetardsMensuels() {
		int[] retardsMensuels = new int[tabRM.length];
		for (int i = 0; i < this.tabRM.length; i++) {
			retardsMensuels[i] = (int) this.tabRM[i].getNbTotalTrainsRetard();
		}
		int[] histo = new int[221];
		int count = 0;
		for (int value = 0; value < 220; value++) {
			count = 0;
			for (int i = 0; i < retardsMensuels.length; i ++) {
				if (retardsMensuels[i] == value) {
					count += 1;
				}
			}
			histo[value] = count;
		}
		return histo;
	}
	
	public double pcRegulariteAveraged() {
		double nombreTrainsPonctuels = 0;
		double nombreTrainsTotal = 0;
		for (int i = 0; i < this.tabRM.length; i++) {
			nombreTrainsTotal += tabRM[i].getNbTotalTrains();
			nombreTrainsPonctuels += (tabRM[i].getNbTotalTrains() - tabRM[i].getNbTotalTrainsAnnules() - tabRM[i].getNbTotalTrainsRetard());
		}
		return (nombreTrainsPonctuels / nombreTrainsTotal * 100);
	}
	
	public String lowestPunctuality() {
		int lowest_arrivee = 0;
		int lowest_depart = 0;
		double lowest_rate = 100;
		Double tmp = (double) lowest_rate;
		for (int depart = 0; depart < 58; depart++) {
			for (int arrivee = 0; arrivee < 58; arrivee++) {
				tmp = (Double) this.pcRegularite(depart, arrivee);
				if ((tmp < lowest_rate) && (!tmp.isNaN())) {
					lowest_arrivee = arrivee;
					lowest_depart = depart;
				}
			}
		}
		return lowest_depart + " " + lowest_arrivee;
	}
	
}
