
function twoSum(nums, target){
    for(i=0; i<nums.length; i++){
        for(j=i+1; j<nums.length; j++){
            if(nums[i] + nums[j] == target){
                if(i != j){
                    return('['+i+', '+j+']')
                }
            }
        }
    }
}

result=twoSum([2, 11, 7, 15], 9)
console.log(result)


