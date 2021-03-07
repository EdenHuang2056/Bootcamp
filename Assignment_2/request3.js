
function maxProduct(nums){

    var eachSet = 0;
    var sum = [];
    for(i=0; i<nums.length; i++){
        for(j=i+1; j<nums.length; j++){
            eachSet = nums[i]*nums[j];
            sum.push(eachSet)
        }
    }
    console.log(Math.max.apply(null, sum))
}


maxProduct([5, 20, 2, 6]); 
maxProduct([10, -20, 0, 3]);