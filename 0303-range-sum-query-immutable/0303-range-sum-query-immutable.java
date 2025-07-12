class NumArray {
    private int[] prefix;
    public NumArray(int[] nums) {
        int n = nums.length;
        prefix = new int[n];
        prefix[0] = nums[0];
        for(int i = 1 ;i<n;i++){
            prefix[i] = prefix[i-1]+nums[i];
        }
    }
    
    public int sumRange(int left, int right) {
        int sum = prefix[right] - (left>0 ? prefix[left-1] : 0);
        return sum;
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */