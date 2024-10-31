# Advanced Objects

## `Object.keys`
- Get all the `keys` witnin the object
```javascript
Object.keys(object1)
```

## `Object.entries`
- Get all the `entries` within the object
```javascript
Object.entries(object1)
```

## `Object.assign`
- Copy all properties from one or more`source objects` to a `target object` and returned a modified `target object`
```javascript
const target = { a: 1, b: 2 };
const source = { b: 4, c: 5 };

const returnedTarget = Object.assign(target, source));

console.log(target);
//Expected Returns: {a:1, b:4, c:5}

console.log(returnedTarget);
//Expectd Returns: {a:1, b:4, c:5}
```
