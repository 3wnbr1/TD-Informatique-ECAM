
public class Line {
	
	protected Point a;
	protected Point b;
	
	public Line(Point a, Point b) {
		this.a = a;
		this.b = b;
	}
	
	public double lenght() {
		return Math.sqrt(Math.pow((this.b.x - this.a.x), 2) + Math.pow((this.b.y - this.a.y), 2));
	}
	
	public boolean isShorterThan(double distance) {
		double len = this.lenght();
		if (len < distance) {
			return true;
		} else {
			return false;
		}
	}
	
}
