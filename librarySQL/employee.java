import java.sql.*;
import java.util.Scanner;




public class employee  {
    static Connection conn=null;



    public employee(){
    }
   
       public static void addUser(){
        conn = bookConnection.getConnection();
        Library li = new Library();
        li.creatTable("create table if not exists userDB( name varchar(50), booksCheckedOut int,  userID int)");
    
        Scanner scnr = new Scanner(System.in);
        System.out.println("Eneter new users name: ");
        String name = scnr.next();
        System.out.println("Eneter how many books checkedout: ");
        int booksCheckedOut = scnr.nextInt();
        System.out.println("Eneter new users id: ");
        int userID = scnr.nextInt();
    
    
        String insertData = "insert into UserDB values(?,?,?)";
        //String insertData = "insert into Manager values(?,?,?)";
        //String insertData = "insert into employee values(?,?,?)";
    
            try {
                PreparedStatement ps = conn.prepareStatement(insertData);
                ps.setString(1, name);
                ps.setInt(2, booksCheckedOut);
                ps.setInt(3, userID);
                int sucess = ps.executeUpdate();
                if(sucess>0){
                    System.out.println("Insert sucessfull");
                }
            } catch (Exception e) {
                //TODO: handle exception
            }finally{
                try {
                   conn.close();
                } catch (Exception e) {
                    //TODO: handle exception
                }
            }
    scnr.close();
        }
           
}
