
public class App {

	public static void main(String[] args) {
	
		RobotCalculateur calculateur = new RobotCalculateur();
		calculateur.moyenneEleves();
		
		Point a = new Point(1, 2.5);
		Point b = new Point(6, 7);
		Line line = new Line(a, b);
		
		System.out.println(line.isShorterThan(10));
		System.out.println(line.isShorterThan(5));
	}
	
	

}
