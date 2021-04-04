import java.sql.*;  // Using 'Connection', 'Statement' and 'ResultSet' classes in java.sql package
 
public class bookUpdateTest implements bookConnection  {   // Save as "JdbcSelectTest.java"
final static String SQLdatabase = "userDb";   
public static void main(String[] args) {
      try (
         Connection conn = DriverManager.getConnection(bookConnection.JDBC_DRIVER,
            bookConnection.USER,bookConnection.pass);
          Statement stmt = conn.createStatement();
         
          ) {
         // Step 3: Write a SQL query string. Execute the SQL query via the 'Statement'.
         //  The query result is returned in a 'ResultSet' object called 'rset'.


         strUpdate();
         ResultSet rset = stmt.executeQuery(strSelect());


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
protected static void strUpdate(){
   String query = "update"+ SQLdatabase + "qty = qty+1 where id = 1 ";
   System.out.println("The SQL statement is: " + query + "\n"); // Echo For debugging
   
}
protected static String strSelect(){
   String strSelect = "select * from"+ SQLdatabase+ " where id = 2";
   String returnString = "The SQL statement is: "+ strSelect+"\n";
   return returnString;
}

}