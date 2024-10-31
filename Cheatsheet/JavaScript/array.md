## Check if all elements in an array is of a type
### Use `array.every`
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

## Append an element to the end of he array
```javascript
array.push(item1, item2, item3)
```

## Remove the last element of the array
```javascript
array.pop()
```

## Add to the beginning of the array
```javascript
array.unshift(item1, item2, item3)
```

## Remove the first element of the array
```javascript
array.shift()
```
