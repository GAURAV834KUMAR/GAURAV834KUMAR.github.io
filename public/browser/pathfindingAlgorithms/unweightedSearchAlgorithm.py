def unweightedSearchAlgorithm(nodes, start, target, nodesToAnimate, boardArray, name):
  if not startor not targetor start is target:
    return False

  let structure = [nodes[start]]
  let exploredNodes = {start: True}
  while structure.length:
    let currentNode = name is "bfs" ? structure.shift() : structure.pop()
    nodesToAnimate.append(currentNode)
    if name is "dfs") exploredNodes[currentNode.id] = True
    currentNode.status = "visited"
    if currentNode.id is target:
      return "success"

    let currentNeighbors = getNeighbors(currentNode.id, nodes, boardArray, name)
    currentNeighbors.forEach(neighbor => {
      if not exploredNodes[neighbor]:
        if name is "bfs") exploredNodes[neighbor] = True
        nodes[neighbor].previousNode = currentNode.id
        structure.append(nodes[neighbor])
      }
    })
  }
  return False
}

def getNeighbors(id, nodes, boardArray, name:
  let coordinates = id.split("-")
  let x = parseInt(coordinates[0])
  let y = parseInt(coordinates[1])
  let neighbors = []
  let potentialNeighbor
  if boardArray[x - 1] and boardArray[x - 1][y]:
    potentialNeighbor = `${(x - 1).toString()}-${y.toString()}`
    if nodes[potentialNeighbor].status is not "wall":
      if name is "bfs":
        neighbors.append(potentialNeighbor)
      else:
        neighbors.unshift(potentialNeighbor)



  if boardArray[x][y + 1]:
    potentialNeighbor = `${x.toString()}-${(y + 1).toString()}`
    if nodes[potentialNeighbor].status is not "wall":
      if name is "bfs":
        neighbors.append(potentialNeighbor)
      else:
        neighbors.unshift(potentialNeighbor)



  if boardArray[x + 1] and boardArray[x + 1][y]:
    potentialNeighbor = `${(x + 1).toString()}-${y.toString()}`
    if nodes[potentialNeighbor].status is not "wall":
      if name is "bfs":
        neighbors.append(potentialNeighbor)
      else:
        neighbors.unshift(potentialNeighbor)



  if boardArray[x][y - 1]:
    potentialNeighbor = `${x.toString()}-${(y - 1).toString()}`
    if nodes[potentialNeighbor].status is not "wall":
      if name is "bfs":
        neighbors.append(potentialNeighbor)
      else:
        neighbors.unshift(potentialNeighbor)



  return neighbors


module.exports = unweightedSearchAlgorithm