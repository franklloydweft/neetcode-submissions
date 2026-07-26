class Solution:
    def isValid(self, s: str) -> bool:
        #the strings have to be even length for matches
        if len(s)%2 != 0:
            return False
        else:
            stack = []
            #keys are all closers
            match_map = {")":"(","]":"[","}":"{"}
            #iterate through string
            for char in s:
                #is the character a closer
                if char in match_map:
                    #check if empty and if the top val matches opener
                    if stack and stack[-1] == match_map[char]:
                        #pop from stack, valid order satisfied
                        stack.pop()
                    else:
                        #order incorrect
                        return False
                else:
                    #add to the stack
                    stack.append(char)
            #if the stack is empty then everything matches, else order is wrong
            if not stack:
                return True
            return False 