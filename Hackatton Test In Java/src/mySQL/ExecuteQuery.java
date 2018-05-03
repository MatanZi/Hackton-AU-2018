package mySQL;

/** Imports. */
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * This class handle the passage from "mysql" to java.
 *
 * @author Samuel.
 */
public class ExecuteQuery {

	/** All the data that the user need to put to be connect with the database. */
	private static final String
	port 		= "4306",
	user	 	= "remote",
	password 	= "remotetoor",
	ip 			= "erlichsefi.mooo.com", 		//127.0.0.1
	schema 		= "Hackatton"; 

	/** The object connection from @see {@link Connection} */
	private static Connection connection = null;

	/**
	 * This function try to connect with the "my_Hospital" schema.
	 * If the connection is a success, a query is made :
	 * For a given doctor_id display on the doctor's computer the patients which are waiting for him,
	 * and the queue time sorted by the queue_time.
	 * !! We are not doing any manipulation here, only the queries are important to us !!
	 * 
	 * 
	 * @throws SQLException
	 * @throws ClassNotFoundException
	 */
	public static void pickFromDataBase(String query) throws SQLException, ClassNotFoundException {
		Statement statement = null;
		ResultSet resultSet = null;
		String url = "jdbc:mysql://" + ip + ":" + port + "/" + schema + "?useSSL=false";
		Class.forName("com.mysql.jdbc.Driver"); //If any error is located here, please do check the jar file. See README.
		System.out.println("hello");
		connection = DriverManager.getConnection(url, user, password); 
		statement = connection.createStatement();
		//resultSet = statement.executeQuery("SELECT UPDATE_TIME FROM information_schema.tables WHERE TABLE_SCHEMA ="
		//		+ " '" + schema + "' AND TABLE_NAME = 'Queue_Reserved'"); //Doing an update is safer before to do any query.
		//if (resultSet.next())
		//	System.out.println("Update on : " + resultSet.getString(1)); //resultSet begin from 1 and not from 0.
		PreparedStatement preparedStatement = connection.prepareStatement(query); //The query we use to get what needed.
		resultSet = preparedStatement.executeQuery();
		printTheResult(resultSet);
		try {
			if (resultSet != null)
				resultSet.close();
			if (statement != null)
				statement.close();
			if (connection != null)
				connection.close();
		} catch (SQLException exception) {
			Logger logger = Logger.getLogger(ExecuteQuery.class.getName());
			logger.log(Level.WARNING, exception.getMessage(), exception);
		}
	}

	/**
	 * This method print the result.
	 * @param resultSet
	 * @throws SQLException
	 */
	private static void printTheResult(ResultSet resultSet) throws SQLException {
		System.out.println();
		System.out.println("--------------------------------------");
		System.out.println("--------------------------------------");
		java.sql.ResultSetMetaData resultSetMetaData = resultSet.getMetaData();
		int column = resultSetMetaData.getColumnCount();
		if (column != 0) {
			while (resultSet.next()) {
				System.out.println("--------------------------------------");
				for (int i = 1; i <= column; i++) 
					System.out.print(resultSet.getString(i) + " | ");
				System.out.println();
			}
			System.out.println("--------------------------------------");
			System.out.println("--------------------------------------");
			System.out.println();
		}
	}

}
