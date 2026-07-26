public class Solution {
    public bool IsPalindrome(string s) {
        //reverse input string
        string reversed = "";
        string sCopy = "";
        for(int i = s.Length-1; i>=0; i-- )
        {
           //get rid of non-alphanumeric characters
           if(Char.IsAsciiLetterOrDigit(s[i]))
           {
            reversed+=s[i];
           }   
        }
        for(int i = 0; i<s.Length; i++)
        {
            //get rid of non-alphanumeric characters
           if(Char.IsAsciiLetterOrDigit(s[i]))
           {
            sCopy+=s[i];
           } 
        }
        //compare reversed string to original
        sCopy = sCopy.ToLower();
        reversed = reversed.ToLower();
        //Console.WriteLine(sCopy+" "+reversed);
        for(int i = 0; i<sCopy.Length; i++)
        {
            //if any character does not match at a position, exit
            if(reversed[i]!=sCopy[i])
            {
                return false;
            }

        }
        //if the loop finishes, the palindrome is valid
        return true;
    }
}
