
# class Solution:

#     def __init__(self):
#               self.Roman={"I":1 ,"V":5 ,"X":10 ,"L":50 ,"C":100 , "D":500 ,"M":1000,}


#     def romanToInt(self):
#         self.n=input("Enter Roman no to get Integer:")
        
#         convert=0
#         for i in self.n:   
            
#             convert=convert+self.Roman.get(i)
            
#         print(convert)    
            
            
# t=Solution()
# t.RomanToInt()            
            


class Solution:
    
    def __init__(self):
        self.Roman={"I":1 ,"V":5 ,"X":10 ,"L":50 ,"C":100 , "D":500 ,"M":1000,}


    def romanToInt(self, s: str) -> int:
        
        length=len(s)
        convert=0
        
        for  i in range (length) :
            
            a=self.Roman[s[i]]
            b=self.Roman[s[i+1]] if i + 1 < length else 0
            
            if a < b :
                convert= convert - a
            else:
                
                convert=convert + a
            
        return convert
        
a=Solution()
print(a.romanToInt("MCVIXMCXIVVVIIIMMM"))           
                   