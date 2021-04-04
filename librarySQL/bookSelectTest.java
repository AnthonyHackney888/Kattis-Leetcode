import java.sql.*;  // Using 'Connection', 'Statement' and 'ResultSet' classes in java.sql package
 //notfinished nned to create new sql for users
public class bookSelectTest implements bookConnection {   // Save as "JdbcSelectTest.java"
final static String SQLdatabase = "userDb";   
   public static void main(String[] args) {
      try (
         // Step 1: Construct a database 'Connection' object called 'conn'
         Connection conn = DriverManager.getConnection(bookConnection.JDBC_DRIVER,
         bookConnection.USER,bookConnection.pass);
               // The format is: "jdbc:mysql://hostname:port/databaseName", "username", "password"
 
         // Step 2: Construct a 'Statement' object called 'stmt' inside the Connection created
         Statement stmt = conn.createStatement();
      ) {
         // Step 3: Write a SQL query string. Execute the SQL query via the 'Statement'.
         //  The query result is returned in a 'ResultSet' object called 'rset'.

 
         ResultSet rset = stmt.executeQuery(strSelect());
 
         // Step 4: Process the 'ResultSet' by scrolling the cursor forward via next().
         //  For each row, retrieve the contents of the cells with getXxx(columnName).
         System.out.println("The records selected are:");
         int rowCount = 0;
         // Row-cursor initially positioned before the first row of the 'ResultSet'.
         // rset.next() inside the whole-loop repeatedly moves the cursor to the next row.
         // It returns false if no more rows.
         while(rset.next()) {   // Repeatedly process each row
            String fname = rset.getString("fname");  // retrieve a 'String'-cell in the row
            String lname = rset.getString("lname");  // retrieve a 'String'-cell in the row
            double numBookCheckedOut = rset.getDouble("numBookCheckedOut");  // retrieve a 'double'-cell in the row
            int    qty   = rset.getInt("qty");       // retrieve a 'int'-cell in the row
            System.out.println(fname + ", "+ lname +", " + numBookCheckedOut + ", " + qty);
            ++rowCount;
         }
         System.out.println("Total number of records = " + rowCount);
 
      } catch(SQLException ex) {
         ex.printStackTrace();
      }  // Step 5: Close conn and stmt - Done automatically by try-with-resources (JDK 7)
   }

   protected static String strSelect(){
      String strSelect = "select fname, lname,numBookCheckedOut, qty from "+ SQLdatabase;
      String returnString = "The SQL statement is: "+ strSelect+"\n";
      return returnString;
   }
}