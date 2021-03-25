import java.sql.*;  // Using 'Connection', 'Statement' and 'ResultSet' classes in java.sql package
 
public class JdbcUpdateTest {   // Save as "JdbcSelectTest.java"
   public static void main(String[] args) {
      try (
         // Step 1: Construct a database 'Connection' object called 'conn'
         Connection conn = DriverManager.getConnection(
               "jdbc:mysql://localhost:3306/ebookshop?allowPublicKeyRetrieval=true&useSSL=false&serverTimezone=UTC",
               "root", "A135");   // For MySQL only
               // The format is: "jdbc:mysql://hostname:port/databaseName", "username", "password"
 
         // Step 2: Construct a 'Statement' object called 'stmt' inside the Connection created
         Statement stmt = conn.createStatement();
      ) {
         // Step 3: Write a SQL query string. Execute the SQL query via the 'Statement'.
         //  The query result is returned in a 'ResultSet' object called 'rset'.
         String strUpdate = "update books set price = price*1.07, qty = qty+1 where id = 1001";
         System.out.println("The SQL statement is: " + strUpdate + "\n"); // Echo For debugging
         int countUpdated = stmt.executeUpdate(strUpdate);
         System.out.println(countUpdated + "records affected. \n");

         String strSelect = "select * from books where id = 1001";
         System.out.println("The SQL statement is: "+ strSelect+"\n");
         ResultSet rset = stmt.executeQuery(strSelect);
         while(rset.next()){
            System.out.println(rset.getInt("id") + ", "
            + rset.getString("author") + ", "
            + rset.getString("title") + ", "
            + rset.getDouble("price") + ", "
            + rset.getInt("qty"));
 }
} catch(SQLException ex){
    ex.printStackTrace();
}
   }
}