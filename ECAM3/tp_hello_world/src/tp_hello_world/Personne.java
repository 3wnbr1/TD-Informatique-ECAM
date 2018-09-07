package tp_hello_world;

public class Personne {

	private String name;
	private Clavier clavier = new Clavier();
	
	
	protected void welcome() {
		System.out.println("Commencez par entre votre nom :");
		name = clavier.lireChaine();
	}
	
	void hello() {
		welcome();
		System.out.println("Bonjour " + name);
	}
	
}
