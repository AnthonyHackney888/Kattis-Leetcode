import java.sql.Connection;
import java.sql.DriverManager;
public class bookConnection {
    //JDBC driver name and database
    static final String JDBC_DRIVER ="com.mysql.jdbc.Driver";
    static final String DB_URL = "jdbc:mysql://localhost:3306/libraryusers?allowPublicKeyRetrieval=true&useSSL=false&serverTimezone=UTC";
    //SQL: user and Pass
    final static String USER = "****";
    final static String PASS = "****";
    static Connection conn = null;


    public static Connection getConnection(){
        try{
            Class.forName(JDBC_DRIVER);
            conn =DriverManager.getConnection(DB_URL, USER, PASS);
            System.out.println("Connected");
        }catch(Exception e){
            e.printStackTrace();
        }
        return conn;
    }
}
