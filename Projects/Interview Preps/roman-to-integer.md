# Roman to Integer

**URL:** https://leetcode.com/problems/roman-to-integer/description/

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        i=0
        while (i <len(s)):
            try:
                current_value = values.get(s[i])
                next_value = values.get(s[i+1]) if (i != len(s) -1 ) else current_value

                if (current_value < next_value):
                    result += next_value - current_value
                    i += 1
                else:
                    result += current_value 
                i+=1    
            except KeyError:
                print(f"Error: Key {s[i]} is not found.")
            
        return result
```
