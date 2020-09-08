class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        Set<Character> set = new HashSet<>();
        int len = 0 ,i=0 ,j = 0;
         while (i < n && j < n) {
            if(!set.contains(s.charAt(j))){
                set.add(s.charAt(j++));
                len = Math.max(len,j - i);
            }
            else{
                set.remove(s.charAt(i++));
            }
        }
        return len;
    }
}