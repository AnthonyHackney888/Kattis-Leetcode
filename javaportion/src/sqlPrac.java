import java.sql.*;

public class sqlPrac {

    public static void main(String[] args) throws Exception {
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
        }catch(ClassNotFoundException e){
            e.printStackTrace();
        }
        try( 

        Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/ebookshop?allowPublicKeyRetrieval=true&useSSL=false&serverTimezone=UTC",
       "root", "A135");
       Statement stmt = con.createStatement();
       ){
           String strSelect = "select title, price, qty from books";
           System.out.println("The SQL statement is: "+ strSelect+"\n");
           ResultSet rset = stmt.executeQuery(strSelect);

           System.out.println("The records selected are:");
            int rowcount = 0;

            while(rset.next()){
                String title = rset.getString("title");
                double price = rset.getDouble("price");
                int qty = rset.getInt("qty");
                System.out.println(title + ", "+ price+", "+qty);
                ++rowcount;
            }
            System.out.println("Total number of records = " + rowcount);
        }catch(SQLException ex){
            ex.printStackTrace();
        }
       
       
    }
}
