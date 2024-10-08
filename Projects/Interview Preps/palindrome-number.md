# PALINDROM NUMBER

**URL:** https://leetcode.com/problems/palindrome-number/

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_num = str(x)
        left = 0
        right = len(str_num) -1
        while (left != right or right != 0 or left != len(str_num) -1):
            if (str_num[left] != str_num[right]): return False
            else:
                left += 1
                right -= 1
        return True
        
            
        
```
