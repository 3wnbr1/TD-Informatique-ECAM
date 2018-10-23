
public class Main {

	public static void main(String[] args) {
		regulariteMensuelle();
		processTrains();
	}
	
	public static void regulariteMensuelle() {
		LecteurFichierTrain trainData = new LecteurFichierTrain();
		System.out.println(trainData.getfichierTrain().length);
	}
	
	public static void processTrains() {
		LecteurFichierTrain trainData = new LecteurFichierTrain();
		TraitementTrain trainProcessor = new TraitementTrain(trainData.getfichierTrain());
		System.out.println("Nombre de RM entre Paris et Lyon");
		System.out.println(trainProcessor.nombreDeRM(0, 19));
		
		System.out.println("Plus petite RM");
		System.out.println(trainProcessor.minDate());
		
		System.out.println("Plus grande RM");
		System.out.println(trainProcessor.maxDate());
		
		System.out.println("Pourcentage de regularite");
		System.out.println(trainProcessor.pcRegularite(0, 19));
		
		AffichageHisto histogramme = new AffichageHisto(trainProcessor.histogrammeRetardsMensuels());
		
		System.out.println("Pourcentage de regularite moyen");
		System.out.println(trainProcessor.pcRegulariteAveraged());
		
		System.out.println("Couple ayant la plus faible regularitee");
		System.out.println(trainProcessor.lowestPunctuality());
	}

}
