from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=set()
        pos,neg,zer = [],[],[]
        for i in nums:
            if i<0:
                neg.append(i)
            elif i>0:
                pos.append(i)
            else:
                zer.append(i)
        # Create a seperate set for neg and pos for O(1)
        Neg, Pos = set(neg), set(pos)

        # if 0 present
        if zer:
            if len(zer)>=3:
                result.add((0,0,0))
            for i in Neg:
                if -1*i in Pos:
                    result.add((i,0,-1*i))
        
        # 2 negatives and 1 pos

        for x,y in combinations(neg,2):
            need = -1 * (x+y)
            if need in Pos:
                result.add(tuple(sorted((x,y,need))))
        # 2 positives 1 neg

        for x,y in combinations(pos,2):
            need = -1 * (x+y)
            if need in Neg:
                result.add(tuple(sorted((x,y,need))))
    
        return [ list(x) for x in result]
       
