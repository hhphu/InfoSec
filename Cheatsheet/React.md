### Add an item to array
- We replace the previous array with a new array that includes the item to be added.
- we use spread syntax to copy the old array to the new one

```javascript
setCart((prev) => {
        return [item, ...prev]
})
``` 

### Remove an item from array
- We use `.filter` method in the arrays to remove an item. ## Add an item to array
- We replace the previous array with a new array that includes the item to be added.
- we use spread syntax to copy the old array to the new one

```javascript
setCart((prev) => {
        return [item, ...prev]
})
``` 

### Remove an item from array
- We use `.filter` method in the arrays to remove an item. 
- The method is called with each item and its index as its first and second arguments. 
- We want the call back function to return `true` for every item whose index does not match the `targetIndex` (also known as the index of the item to be removed)

```javascript
setCart((prev) => {
        return prev.filter((item, index) => index !== targetIndex)
})

- The method is called with each item and its index as its first and second arguments. 
- We want the call back function to return `true` for every item whose index does not match the `targetIndex` (also known as the index of the item to be removed)

```javascript
setCart((prev) => {
        return prev.filter((item, index) => index !== targetIndex)
})
                                                                                                                                                                                                                                                                                                                                                                                         
