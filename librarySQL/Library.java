import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;

public class Library {
    static Connection conn=null;

    public void creatTable(String tableName){
        conn = bookConnection.getConnection();
        Statement stmt;
        try {
            stmt = conn.createStatement();
            stmt.execute(tableName);
            System.out.println("Table created");
        } catch (SQLException e) {
            e.printStackTrace();
        }finally{

            try {
                conn.close();
            } catch (Exception e) {
                //TODO: handle exception
            }
        }
        
    }
    public static void main(String args[]){
        employee.addUser();
    }
}
