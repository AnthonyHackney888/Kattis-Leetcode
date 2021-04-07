public class Library {
    public static void main(String args[]){
        bookUpdateTest update = new bookUpdateTest();
        bookInsertTest insert = new bookInsertTest();
        bookSelectTest select = new bookSelectTest();

        System.out.println(update);
        System.out.println(insert);
        System.out.println(select);

    }
}
