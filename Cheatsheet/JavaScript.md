# Javascript Cheat Sheet

## Promises
- Resulting objects of asynchronous functions, which has three states:
	- Pending: initial state, where the operation is incomplete
	- Resolves: the operation is completed successfully with a given object of values
	- Rejected: the operation failed with a given error

- An example of an asynchronous function that returns promises

```javascript
const checkInventory = (order) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            let inStock = order.every(item => inventory[item[0]] >= item[1]);
            if (inStock) {
                resolve(`Thank you. Your order was successful.`);
            } else {
                reject(`We're sorry. Your order could not be completed because some items are sold out.`);
            }
        }, 1000);
    });
};
```

- Function that works on resolvedValue

```javascript
const handleSuccess = (resolvedValue) =>{
	console.log(resolvedValue)
}
```

- Function that works on rejectedValue

```JavaScript
const handleFailure = (rejcetedValue) => {
	console.log(rejectedValue)
}
```

- Try-Catch with Promises

```JavaScript
checkInventory(order).then(handleSuccess).catch(handleFailure)
```

- Chaining multiple Promises

```JavaScript
checkInventory(order)
.then((resolvedValueArray) => {
	return processPayment(resolvedValueArray)
})
.then((resolvedValueArray) => {
	return shipOrder(resolvedValueArray)
})
.catch(handleFailure)
```

- `Promise.all()`: accepts an array of Promises and group them into a Promise.
	- The Promise resolves when all the Promises in the array resolve.
	- The Promise rejects when one or more of the Promises in the array rejects.

```JavaScript

```


