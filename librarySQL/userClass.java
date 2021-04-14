

public class userClass {
    private String fName;
    private String lName;
    private  int booksCheckedOut;
    private  int userID;

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

    /**
     * @return int return the booksCheckedOut
     */
    public int getBooksCheckedOut() {
        return booksCheckedOut;
    }

    /**
     * @param booksCheckedOut the booksCheckedOut to set
     */
    public void setBooksCheckedOut(int booksCheckedOut) {
        this.booksCheckedOut = booksCheckedOut;
    }

    /**
     * @return int return the userID
     */
    public int getUserID() {
        return userID;
    }

    /**
     * @param userID the userID to set
     */
    public void setUserID(int userID) {
        this.userID = userID;
    }
    public userClass(String fName, String lName, int booksCheckedOut, int userID) {
        this.fName = fName;
        this.lName = lName;
        this.booksCheckedOut = booksCheckedOut;
        this.userID = userID;
    }
   
}