'''Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l=[]
        sub_s=""
        for i in s:
            print("i: ",i,"subs: ",sub_s)
            if i not in sub_s:
                sub_s+=i
            else:
                # print(sub_s)
                l.append(len(sub_s))
                index=sub_s.find(i)
                sub_s=sub_s[index+1:]
                sub_s+=i
        l.append(len(sub_s))

        return max(l)
    
if __name__=="__main__":
    sln=Solution()
    n=sln.lengthOfLongestSubstring("aab")
    print(n)
