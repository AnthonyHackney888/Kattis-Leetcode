public class clerk extends employee {

    private int empId;
    public clerk(String fName, String lName, int empId){
        super(fName, lName);
        this.empId = empId;
    }

    

    /**
     * @return int return the empId
     */
    public int getEmpId() {
        return empId;
    }

    /**
     * @param empId the empId to set
     */
    public void setEmpId(int empId) {
        this.empId = empId;
    }


  
    public void addUser(int id){

    }
    
    public void removeUser(int id){

    }
}
