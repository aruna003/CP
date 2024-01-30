'''Input: strs = ["flower","flow","flight"]
Output: "fl"'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        stop=False
        for i in range(len(strs[0])):
            letter = strs[0][i]
            # print(letter)
            for word in strs:
                if i>=len(word) or word[i]!=letter:
                    stop=True
                    break
            if stop:
                break
            else:
                prefix+=letter
        return prefix

def efficient(strs):
        temps=strs[0]
        for k in range(1,len(strs)):
            a=temps
            b=strs[k]
            maxl=0
            i=0
            while i<min(len(a),len(b)) and a[i]==b[i]:
                maxl+=1
                i+=1
            temps=a[i-maxl:i]
        return temps
