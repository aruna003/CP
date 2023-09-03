// Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside 
// the signed 32-bit integer range [-231, 231 - 1], then return 0

class Solution {
public:
    int reverse(int x) {
        int revs=0;
        int max = INT_MAX;
        int min = INT_MIN;
        while (x!=0){
          // before multiplying check for limit since a 64 bit cant be stored 
            if ((revs>max/10) or (revs<min/10)){
                return 0;
            }
            int r = x%10;
            x = x/10;
            revs=revs*10+r;

        }
        return revs;
    }
};
