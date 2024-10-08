# Two Sum

**URL:** https://leetcode.com/problems/two-sum/description/

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

/**
 [2,7,11,15]
    0:2
    1:7
    2:11
    3:15
 */     

var twoSum = function(nums, target) {
    let numsMap = new Map()
    nums.forEach((element, index) => {
        numsMap.set(element, index)
    })
    
    for (let i =0; i < nums.length -1; i++) {
        let sub = target - nums[i]
        if (numsMap.has(sub) && numsMap.get(sub) !== i ) {
            return [i, numsMap.get(sub)]
        }
    }


};
```
