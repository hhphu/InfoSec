# GRAPHS

## Depth-First Search

```js
const depthFirstSearch =  (start, visitedVertices = [start) => {
  if (start.edges.length) {
    start.edges.forEacth( edge => {
      const neighbor = start.edges[0].end
      if (!visitedVertices.includes(neighbor)) {
        visitedVertices.push(neighbor)
        depthFirstSearch(neighbor, visitedVertices)
      }
    })
  }
}
```
- Using callback fucntion

```js
const depthFirstSearch =  (start, cb, visitedVertices = [start) => {
  if (start.edges.length) {
    start.edges.forEacth( edge => {
      const neighbor = start.edges[0].end
      if (!visitedVertices.includes(neighbor)) {
        visitedVertices.push(neighbor)
        depthFirstSearch(neighbor, visitedVertices)
      }
    })
  }
}

depthFirstSearch(vertices[0], (vertex) => {console.log(vertex.data})
```

## Breadth-First Search
Use a queue for the operations

```js
const breadthFirstTraversal = (start) => {
  const visitedVertices = [start]
  const visitQueue = new Queue()
  visitQueue.enqueue(start)

  while (!visitQueue.isEmpty()){
    const current = visiQueue.dequeue()
    console.log(current.data)
    current.edges.forEach( edge => {
      const neighbor = edge.end
      if (!visitedVertices.includes(neighbor)) {
        visitedVertices.push(neighbor)
        visitQueue.enqueue(neighbor)
    })
  }
}
```
