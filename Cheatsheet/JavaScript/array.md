## Check if all elements in an array is of a type
###Use `array.every`
```javascript
const array = [1,2,3,4,5];
const checkNumbers = array.every(e => typeof e === 'number');
console.log(checkNumbers);  // this will return true if all elements are numbers
```

### Manual implementation
```javascript
const array = [1,2,3,4,5];
let allNumbers = true; // assume the array has all number elements

for (int i = 0; i<array.length(); i++) {
	if (typeof array[i] !== 'number') {
		allNumbers = false;
		break;
	}
}

console.log(allNumbers) 
```
