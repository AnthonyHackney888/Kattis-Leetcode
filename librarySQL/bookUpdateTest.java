import java.sql.*;  // Using 'Connection', 'Statement' and 'ResultSet' classes in java.sql package
 
public class bookUpdateTest {   // Save as "JdbcSelectTest.java"
   public static void main(String[] args) {
      try (
         // Step 1: Construct a database 'Connection' object called 'conn'
         Connection conn = DriverManager.getConnection(
               "jdbc:mysql://localhost:3306/libraryusers?allowPublicKeyRetrieval=true&useSSL=false&serverTimezone=UTC",
               "root", "****");   // For MySQL only
               // The format is: "jdbc:mysql://hostname:port/databaseName", "username", "password"
 
         // Step 2: Construct a 'Statement' object called 'stmt' inside the Connection created
         Statement stmt = conn.createStatement();
      ) {
         // Step 3: Write a SQL query string. Execute the SQL query via the 'Statement'.
         //  The query result is returned in a 'ResultSet' object called 'rset'.
         String strUpdate = "update userDb qty = qty+1 where id = 1 ";
         System.out.println("The SQL statement is: " + strUpdate + "\n"); // Echo For debugging
         

         String strSelect = "select * from userDb where id = 2";
         System.out.println("The SQL statement is: "+ strSelect+"\n");
         ResultSet rset = stmt.executeQuery(strSelect);
         while(rset.next()){
            System.out.println(rset.getInt("id") + ", "
            + rset.getString("fName") + ", "
            + rset.getString("lName") + ", "
            + rset.getDouble("numBookCheckedOut")+", "+ rset.getInt("qty"));
 }
} catch(SQLException ex){
    ex.printStackTrace();
}
   }
}