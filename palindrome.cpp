class Solution {
public:
    bool isPalindrome(int x) {
        long int ori_x=x;
        long int reverse=0;
        while(x>0){
            int r=x%10;
            x=x/10;
            reverse=reverse*10+r;
        }
        cout<<reverse;
        if (reverse==ori_x){
            return true;
        }
        else{
            return false;
        }
    }
};
