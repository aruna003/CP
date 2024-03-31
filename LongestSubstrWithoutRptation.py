class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxi=-float("inf")
        sub_s=""
        for i in s:
            if i not in sub_s:
                sub_s+=i
            else:
                # l.append(len(sub_s))
                l=len(sub_s)
                if l>maxi:
                    maxi=l
                index=sub_s.find(i)
                sub_s=sub_s[index+1:]
                sub_s+=i
        l=len(sub_s)
        if l>maxi:
            maxi=l

        return maxi
