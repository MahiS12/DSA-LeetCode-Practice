class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        
        n = len(s)
        
        if n%2 ==0:

            v_count = 0
            other= 0
            for i in range(n//2):
                if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                    v_count+=1
                else:
                    other+=1
            
            v_count_1=0
            other_1=0
            for i in range((n//2),n):
                if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                    v_count_1+=1
                else:
                    other_1+=1
            
            if v_count == v_count_1 and other== other_1:
                return True
            else:
                return False
    
             
        else:
            return False