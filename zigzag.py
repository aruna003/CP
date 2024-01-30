'''not completed there are errors'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        n=(numRows-1)+(numRows-2)+1
        numRows%n
        l=len(s)
        levels=[]
        for i in range(n):
            sub_level=[]
            c=0
            while c<=l:
                sub_level.append(s[i+c])
                c+=c
            levels.append(sub_level)
        print(levels)
            
if __name__=="__main__":
    sln=Solution()
    n=sln.convert("PAYPALISHIRING",3)
    print("hello")
    # print(n)
