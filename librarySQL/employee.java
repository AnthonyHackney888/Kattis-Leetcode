import java.sql.*;




public class employee implements bookConnection {
    private String fName;
    private String lName;
    public employee(String fName, String lName){
        this.fName = fName;
        this.lName = lName;
        
    }
   
    /**
     * @return String return the fName
     */
    public String getFName() {
        return fName;
    }

    /**
     * @param fName the fName to set
     */
    public void setFName(String fName) {
        this.fName = fName;
    }

    /**
     * @return String return the lName
     */
    public String getLName() {
        return lName;
    }

    /**
     * @param lName the lName to set
     */
    public void setLName(String lName) {
        this.lName = lName;
    }
    public static void not(){

    


        try{
        Connection conn = DriverManager.getConnection(bookConnection.JDBC_DRIVER,
        bookConnection.USER,bookConnection.pass);
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery("select * from userDB");
        
            
            while(rs.next()){
            userClass user = new userClass(rs.getString(1), rs.getString(2), rs.getInt(3), rs.getInt(4));
            
            String sqlUpdate = "UPDATE userDB "
            + "SET"+user.getFName()+ "= ? "
            + "SET"+user.getLName()+ "= ? "
            + "WHERE"+user.getUserID() +" = ?";
            }
            
        }catch(SQLException ex) {
            ex.printStackTrace();
         } 
        }
           
}
