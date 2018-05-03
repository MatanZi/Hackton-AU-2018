package mySQL;

import java.sql.SQLException;

/**
 * This class contains the main method to make test and run the things we need.
 * @author Samuel.
 */
public class Main {

	/**
	 * The main method.
	 * @param args
	 */
	public static void main(String[] args) {
		try {
			ExecuteQuery.pickFromDataBase(
					"SELECT * FROM teacher;" // this query doesn't work but we just check the connection.
					);
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
}