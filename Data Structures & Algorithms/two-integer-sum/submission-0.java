class Solution {
    public int[] twoSum(int[] nums, int target) {
        //map of differences between num and target
        HashMap<Integer,Integer> diffMap = new HashMap<>();
        for(int i = 0; i<nums.length; i++){
            int diff = target - nums[i];
            //if the difference is already mapped we return (there is only one valid combo, wont appear twice)
            if(diffMap.containsKey(diff)){
                return new int[] {diffMap.get(diff), i};
            }else{
                //else, map it
                diffMap.put(nums[i],i);
            }
        }
        //invalid case, empty array
        return new int[]{};
    }
}
