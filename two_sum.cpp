class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> v;
        for (int i=0; i<nums.size(); i++){
            int a=nums[i];
            int comple = target-a;
            int index = find(nums,i,comple);

            if (index!= -1){
                v.push_back(i);
                v.push_back(index);
                return v;
            }
        }
        return v;
    }

    int find(vector<int> nums, int index,int comple){
        for (int i=0; i<nums.size(); i++){
            if (i==index){
                continue;
            }
            if (nums[i]==comple){
                return i;
            }
        } 
        return -1 ;    
    }
};
