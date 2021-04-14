
public class manager extends employee {
    
    private int managerID;
    String sqlUpdate = "UPDATE userDB "
    + "SET fName = ? "
    + "SET lName = ? "
    + "WHERE id = ?";
    public manager(String fName, String lName, int managerID){
        super(fName, lName);
        this.managerID = managerID;
    }

    /**
     * @return int return the managerID
     */
    public int getManagerID() {
        return managerID;
    }

    /**
     * @param managerID the managerID to set
     */
    public void setManagerID(int managerID) {
        this.managerID = managerID;
    }

 
    public void addUser(String fName, String lName,int id){
        
    }
   
    public boolean removeUser(int id){
        return false;

    }
    
    public boolean addEmployee(int empId){
        return false;

    }
    public boolean removeEmployee(int empId){
        return false;

    }
   


}
