class Solution {
public:
    int romanToInt(string s) {
        map<char,int> r;
        r['I'] = 1;
        r['V'] = 5;
        r['X'] = 10;
        r['L'] = 50;
        r['C'] = 100;
        r['D'] = 500;
        r['M'] = 1000;
        int num=0;
         
        for(int i=0; i!=s.length(); i++){
            char n = s[i];
            if (r[n]<r[s[i+1]]) {
                num=num-r[n];
            }
            else{
                num=num+r[n];
            }
        cout<<num<<endl;
        }
        return num;
    }
};
