import java.sql.*;     // Use classes in java.sql package
 
public class bookInsertTest implements bookConnection{    // Save as "JdbcUpdateTest.java"
final static String SQLdatabase = "userDb";   
   public static void main(String[] args) {
      try (
         // Step 1: Allocate a database 'Connection' object
         Connection conn = DriverManager.getConnection(bookConnection.JDBC_DRIVER,
            bookConnection.USER,bookConnection.pass);
 
         // Step 2: Allocate a 'Statement' object in the Connection
         Statement stmt = conn.createStatement();
      ) {
         // Step 3 & 4: Execute a SQL INSERT|DELETE statement via executeUpdate(),
         //   which returns an int indicating the number of rows affected.
         
         // DELETE records with id>=1 and id<2
         int countDeleted = stmt.executeUpdate(strDelete());
         System.out.println(countDeleted + " records deleted.\n");
 
         // INSERT a record
         /*
         String sqlInsert = "insert into userDb values (4, 'Anthony', 'Hackney', 3, 4)";
         System.out.println("The SQL statement is: " + sqlInsert + "\n");  // Echo for debugging
         int countInserted = stmt.executeUpdate(sqlInsert);
         System.out.println(countInserted + " records inserted.\n");
 */
         // INSERT multiple records
        String sqlInsert = "insert userDb info values "
               + "(5, 'Firstname5', 'Lastname5', 0, 3),"
               + "(6, 'Firstname6', 'Lastname6', 1, 4)";
         System.out.println("The SQL statement is: " + sqlInsert + "\n");  // Echo for debugging

 
         // INSERT a partial record
         sqlInsert = "insert into userDb (id, fname, lname) values (7, 'John', 'Doe')";
         System.out.println("The SQL statement is: " + sqlInsert + "\n");  // Echo for debugging
        int countInserted = stmt.executeUpdate(sqlInsert);
         System.out.println(countInserted + " records inserted.\n");
 
        
         ResultSet rset = stmt.executeQuery( strSelect());

         while(rset.next()){
            System.out.println(rset.getInt("id") + ", "
            + rset.getString("fName") + ", "
            + rset.getString("lName") + ", "
            + rset.getDouble("numBookCheckedOut")+", "+rset.getInt("qty"));
         }
      } catch(SQLException ex) {
         ex.printStackTrace();
      }  // Step 5: Close conn and stmt - Done automatically by try-with-resources
   }

   protected static String strDelete(){
      String sqlDelete = "delete from "+SQLdatabase+" where id >= 1 and id < 2";
      String returnDelete="The SQL statement is: " + sqlDelete + "\n";  // Echo for debugging
      return returnDelete;
   }

   protected static String strSelect(){
      String strSelect = "select * from"+ SQLdatabase;
      String returnString = "The SQL statement is: "+ strSelect+"\n";
      return returnString;
   }
}