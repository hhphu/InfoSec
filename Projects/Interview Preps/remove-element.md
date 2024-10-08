# REMOVE ELEMNT

**URL:** https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

```javascript
var removeElement = function(nums, val) {
    let count = 0
    for (let i = nums.length -1; i >=0; i --) {
        if (nums[i] === val) {
            nums.splice(i,1)
            count++
            console.log(`The new nums is ${nums}`)
        }
    }
    console.log(`The total count is ${count}`)
    

};
```
