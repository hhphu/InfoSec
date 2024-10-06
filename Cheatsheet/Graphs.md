# GRAPHS
With three classes, Edge, Vertex, and Graph, we can implement a variety of graphs that satisfy the requirements of many algorithms. Remember that a Graph consists of vertices and their corresponding edges.
With this in mind, we will create our Graph with the following requirements:
- A Vertex can store any data.
- A Vertex maintains a list of connections to other vertices, represented by a list of Edge instances.
- A Vertex can add and remove edges going to another Vertex.
- A Graph stores all of its vertices, represented by a list of Vertex instances.
- A Graph knows if it is directed or undirected.
- A Graph knows if it is weighted or unweighted.
- A Graph can add and remove its own vertices.
- A Graph can add and remove edges between stored vertices.

## Vertex class
```javascript
  constructor(data) {
    this.data = data
    this.edges = []
  }
```
### Adding edges
```javascript
 addEdge(vertex) {
    if (vertex instanceof Vertex) {
      this.edges.push(new Edge(this, vertex))
    }
    else{
      throw new Error('Error. The edge must connect to a vertex')
    }
  }
```
### Remove edges
```javascript
 removeEdge(toRemoveVertex) {
    this.edges = this.edges.filter(edge => edge.end !== toRemoveVertex)
  }
```

## Graph Class
```javascript
  constructor(){
    this.vertices = []
  }
```

### Adding vertices
```javascript
 addVertex(data){
    const newVertex = new Vertex(data)
    this.vertices.push(newVertex)
    return newVertex
  }
```

### Remove vertices
```javascript
  removeVertex(vertex) {
    this.vertices = this.vertices.filter(v => v !== vertex);
  }
```

### Adding edges
```javascript
addEdge(vertexOne, vertexTwo) {
    if (vertexOne instanceof Vertex && vertexTwo instanceof Vertex){
      vertexOne.addEdge(vertexTwo)
      vertexTwo.addEdge(vertexOne)
    } 
    else {
      throw new Error('The two arguments must be vertices/')
    } 
  }
```

### Removing edges
```javascript
  removeEdge(vertexOne, vertexTwo){
    if (vertexOne instanceof Vertex && vertexTwo instanceof Vertex) {
      vertexOne.removeEdge(vertexTwo);
      vertexTwo.removeEdge(vertexOne);
    } else {
      throw new Error('Expected Vertex arguments.');
    }
  }
```

## Weighted Graph
- In the constructor of `Graph` class, add a boolean `isWeighted` which is default to `false`
- In the `Vertex` class, add a second parameter `weight` to `.addEdge()` funcntion & add the parameter to the new `Edge` instance created within.
- In the Graph class, add a third parameter for weight in the .addEdge() method. Create a variable edgeWeight, and set it to the weight argument if the graph is weighted, otherwise set it to null. Pass edgeWeight to the calls that create edges between the given vertices. Remember to do this for both calls

## Directed Graph
- In the `Graph` class, add `isDirected` boolean whose default falue is `false`
- In the `Graph` class, only create an edge from `vertexTwo` to `vertexOne` only if `isDirected = false`

## Complete Graph class
```javascript
const Edge = require('./Edge.js');
const Vertex = require('./Vertex.js');

class Graph {
  constructor(isWeighted = false, isDirected = false) {
    this.vertices = [];
    this.isWeighted = isWeighted;
    this.isDirected = isDirected;
  }

  addVertex(data) {
    const newVertex = new Vertex(data);
    this.vertices.push(newVertex);

    return newVertex;
  }

  removeVertex(vertex) {
    this.vertices = this.vertices.filter(v => v !== vertex);
  }

  addEdge(vertexOne, vertexTwo, weight) {
    const edgeWeight = this.isWeighted ? weight : null;

    if (vertexOne instanceof Vertex && vertexTwo instanceof Vertex) {
      vertexOne.addEdge(vertexTwo, edgeWeight);

      if (!this.isDirected) {
        vertexTwo.addEdge(vertexOne, edgeWeight);
      }
    } else {
      throw new Error('Expected Vertex arguments.');
    }
  }

  removeEdge(vertexOne, vertexTwo) {
    if (vertexOne instanceof Vertex && vertexTwo instanceof Vertex) {
      vertexOne.removeEdge(vertexTwo);

      if (!this.isDirected) {
        vertexTwo.removeEdge(vertexOne);
      }
    } else {
      throw new Error('Expected Vertex arguments.');
    }
  }

  print() {
    this.vertices.forEach(vertex => vertex.print());
  }
}

module.exports = Graph;
```

## Complete Vertex class
```javascript
const Edge = require('./Edge.js');

class Vertex {
  constructor(data) {
    this.data = data;
    this.edges = [];
  }

  addEdge(vertex, weight) {
    if (vertex instanceof Vertex) {
      this.edges.push(new Edge(this, vertex, weight));
    } else {
      throw new Error('Edge start and end must both be Vertex');
    }
  }

  removeEdge(vertex) {
    this.edges = this.edges.filter(edge => edge.end !== vertex);
  }

  print() {
    const edgeList = this.edges.map(edge =>
        edge.weight !== null ? `${edge.end.data} (${edge.weight})` : edge.end.data);

    const output = `${this.data} --> ${edgeList.join(', ')}`;
    console.log(output);
  }
}

module.exports = Vertex;
```

## Complete Edge class
```javascript
  class Edge {
  constructor(start, end, weight = null) {
    this.start = start;
    this.end = end;
    this.weight = weight;
  }
}

module.exports = Edge;
```
