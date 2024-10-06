# Heaps
- Binary trees with sorted values:
    - Min-Heap: the root element (top most) must be the minimum value & every child element must be greater than or equal to its parent
    - Max-Heap: the root element (top most) must be the maximum value & every child element must be less than or equal to its parent
- To determine the indices of for parent and child elements:
    - Parent: `(index/2)`, round donw
    - Left Child: `index*2`
    - Right Child: `(index*2) + 1`
      
## Implementing MinHeap
### MinHeap Class
Our MinHeap class will store two pieces of information:
  - An array of elements within the heap.
  - A count of the elements within the heap.
To make our lives easier, we’ll always keep one element at the beginning of the array with the value null. By doing this, we can simplify our coding by always referencing our minimum element at index
 1 instead of 0 and our last element at index `this.size` instead of `this.size - 1`.

```javascript
class MinHeap {
  constructor(){
    this.heap = [null]
    this.size=0
  }
}
module.exports = MinHeap;
```
### Bubble up
- USed to preserve the properties of the MinHeap, i.e when adding a new element, we need to make sure the root element has the minimum values.
- Helper functions: these will help us to perform `**bubbleUp()**` function

```javascript
const getParent = current => Math.floor((current / 2));
const getLeft = current => current * 2;
const getRight = current => current * 2 + 1;
 swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }
```

- To ensure every child element has greater value than its parents, we continuosly swapping it with its parents until the conditions are met.

```javascript
bubbleUp() {
    let current = this.size;
    while (current > 1 && this.heap[current] < this.heap[getParent(current)]) {
      console.log('..', this.heap);
      console.log(`.. swap index ${current} with ${getParent(current)}`);
      this.swap(current, getParent(current));
      current = getParent(current);
    }
  }
```

### Remove the Min
- To remove the Min in the MinHeap:
  1. Swap the last indext with the first index
  2. Delete the min
  3. Restore the heap properities through Heapify()
 
```javascript
  popMin() {
    if (this.size === 0) {
      return null;
    }
    
    console.log(`\n.. Swap ${this.heap[1]} with last element ${this.heap[this.size]}`);
    this.swap(1, this.size);
    const min = this.heap.pop();
    this.size--;
    console.log(`.. Removed ${min} from heap`);
    console.log('..',this.heap);
    return min;
    
  }
```

### Heapify
- Like `BubbleUp`, `Heapify` is used to maintain the properties of a hash. The only difference is it's moving down instead of moving up
- Helper functions:
  - `canSwap()`:
    - The parent value has to be less than both of its child values.
    - return `true` if swapping can occur for either child. return `false` otherwise

```javascript
canSwap(current, leftChild, rightChild) {
  // Check that one of the possible swap conditions exists
  return (this.exists(leftChild) && this.heap[current] > this.heap[leftChild] 
  || this.exists(rightChild) && this.heap[current] > this.heap[rightChild]
    );
  }

exists(index) {
    return index <= this.size;
  }
```
- `**Heapify()**` function
  - We need to swap with the child whose value is smaller. This way, we can maintain the properties of the MinHeap
  - If an element has both two children, check to see which child element has smaller value. If `leftChild` is smaller, swap with the `leftChild`. Otherwise, Swap with the `rightChild`
  - If an elenment only has one child, we swap with the `leftChild`

```javascript
heapify() {
    console.log('Heapify');
    let current = 1;
    let leftChild = getLeft(current);
    let rightChild = getRight(current);

    while (this.canSwap(current, leftChild, rightChild)) {
      if (this.exists(leftChild) && this.exists(rightChild)){
        if( this.heap[leftChild] > this.heap[rightChild] ){
           this.swap(current, leftChild)
           current = leftChild
        }
        else {
          this.swap(current, rightChild)
          current = rightChild
        } 
      }
      else {
        this.swap(current, leftChild)
        current = leftChild
      }
      leftChild = getLeft(current);
      rightChild = getRight(current);
    }
  }
```

- in `.popMin()` function, add the `.heapify()` before returning the `min` value.

- Complete `MinHeap()` Class

```javascript
class MinHeap {
  constructor() {
    this.heap = [ null ];
    this.size = 0;
  }

  popMin() {
    if (this.size === 0) {
      return null
    }
    console.log(`\n.. Swap ${this.heap[1]} with last element ${this.heap[this.size]}`);
    this.swap(1, this.size);
    const min = this.heap.pop();
    this.size--;
    console.log(`.. Removed ${min} from heap`);
    console.log('..',this.heap);
    this.heapify()
    return min;
  }

  add(value) {
    console.log(`.. adding ${value}`);
    this.heap.push(value);
    this.size++;
    this.bubbleUp();
    console.log(`added ${value} to heap`, this.heap);
  }

  bubbleUp() {
    let current = this.size;
    while (current > 1 && this.heap[getParent(current)] > this.heap[current]) {
      console.log(`.. swap ${this.heap[current]} with parent ${this.heap[getParent(current)]}`);
      this.swap(current, getParent(current));
      console.log('..', this.heap);
      current = getParent(current);
    }
  }

  heapify() {
    console.log('Heapify');
    let current = 1;
    let leftChild = getLeft(current);
    let rightChild = getRight(current);

    while (this.canSwap(current, leftChild, rightChild)) {
      if (this.exists(leftChild) && this.exists(rightChild)){
        if( this.heap[leftChild] > this.heap[rightChild] ){
           this.swap(current, leftChild)
           current = leftChild
        }
        else {
          this.swap(current, rightChild)
          current = rightChild
        } 
      }
      else {
        this.swap(current, leftChild)
        current = leftChild
      }
      leftChild = getLeft(current);
      rightChild = getRight(current);
    }
  }

  exists(index) {
    return index <= this.size;
  }

  canSwap(current, leftChild, rightChild) {
    // Check that one of the possible swap conditions exists
    return (
      this.exists(leftChild) && this.heap[current] > this.heap[leftChild]
      || this.exists(rightChild) && this.heap[current] > this.heap[rightChild]
    );
  }

  swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }

}

const getParent = current => Math.floor((current / 2));
const getLeft = current => current * 2;
const getRight = current => current * 2 + 1;

module.exports = MinHeap;

```

### What's the maximum swaps for a given set of data?
- Let `N` be the number of the element & `h` be the height of the binary tree (heap)
- Following the formula, we get the maximum swaps: `N = 2**(h+1) -1`
- Since 10000 is between 8191 (h=13) & 16383 (h=14), the maximum swaps can be at most 13

