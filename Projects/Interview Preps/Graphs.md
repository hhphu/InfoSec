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
