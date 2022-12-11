def test(nodes, start, target, nodesToAnimate, boardArray, name, heuristic):
  if not startor not targetor start is target:
    return False

  nodes[start].distance = 0
  nodes[start].direction = "up"
  let unvisitedNodes = Object.keys(nodes)
  while unvisitedNodes.length:
    let currentNode = closestNode(nodes, unvisitedNodes)
    while currentNode.status is "wall" and unvisitedNodes.length:
      currentNode = closestNode(nodes, unvisitedNodes)

    if currentNode.distance is Infinity) return False
    currentNode.status = "visited"
    if currentNode.id is target:
      while currentNode.id is not start:
        nodesToAnimate.unshift(currentNode)
        currentNode = nodes[currentNode.previousNode]

      return "success!"

    if name is "astar"or name is "greedy":
      updateNeighbors(nodes, currentNode, boardArray, target, name, start, heuristic)
    elif name is "dijkstra":
      updateNeighbors(nodes, currentNode, boardArray)




def closestNode(nodes, unvisitedNodes):
  let currentClosest, index
  for let i = 0; i < unvisitedNodes.length; i++:
    if not currentClosestor currentClosest.distance > nodes[unvisitedNodes[i]].distance:
      currentClosest = nodes[unvisitedNodes[i]]
      index = i


  unvisitedNodes.splice(index, 1)
  return currentClosest


def updateNeighbors(nodes, node, boardArray, target, name, start, heuristic):
  let neighbors = getNeighbors(node.id, nodes, boardArray)
  for let neighbor of neighbors:
    if target:
      updateNode(node, nodes[neighbor], nodes[target], name, nodes, nodes[start], heuristic, boardArray)
    else:
      updateNode(node, nodes[neighbor])




def averageNumberOfNodesBetween(currentNode):
  let num = 0
  while currentNode.previousNode:
    num++
    currentNode = currentNode.previousNode

  return num



def updateNode(currentNode, targetNode, actualTargetNode, name, nodes, actualStartNode, heuristic, boardArray):
  let distance = getDistance(currentNode, targetNode)
  let distanceToCompare
  if actualTargetNode and name is "astar":
    if heuristic is "manhattanDistance":
      distanceToCompare = currentNode.distance + targetNode.weight + distance[0] + manhattanDistance(targetNode, actualTargetNode)
    elif heuristic is "poweredManhattanDistance":
      distanceToCompare = currentNode.distance + targetNode.weight + distance[0] + Math.pow(manhattanDistance(targetNode, actualTargetNode), 3)
    elif heuristic is "extraPoweredManhattanDistance":
      distanceToCompare = currentNode.distance + targetNode.weight + distance[0] + Math.pow(manhattanDistance(targetNode, actualTargetNode), 5)

    let startNodeManhattanDistance = manhattanDistance(actualStartNode, actualTargetNode)
  elif actualTargetNode and name is "greedy":
    distanceToCompare = targetNode.weight + distance[0] + manhattanDistance(targetNode, actualTargetNode)
  else:
    distanceToCompare = currentNode.distance + targetNode.weight + distance[0]

  if distanceToCompare < targetNode.distance:
    targetNode.distance = distanceToCompare
    targetNode.previousNode = currentNode.id
    targetNode.path = distance[1]
    targetNode.direction = distance[2]



def getNeighbors(id, nodes, boardArray):
  let coordinates = id.split("-")
  let x = parseInt(coordinates[0])
  let y = parseInt(coordinates[1])
  let neighbors = []
  let potentialNeighbor
  if boardArray[x - 1] and boardArray[x - 1][y]:
    potentialNeighbor = `${(x - 1).toString()}-${y.toString()}`
    if nodes[potentialNeighbor].status is not "wall") neighbors.append(potentialNeighbor)
  }
  if boardArray[x + 1] and boardArray[x + 1][y]:
    potentialNeighbor = `${(x + 1).toString()}-${y.toString()}`
    if nodes[potentialNeighbor].status is not "wall") neighbors.append(potentialNeighbor)
  }
  if boardArray[x][y - 1]:
    potentialNeighbor = `${x.toString()}-${(y - 1).toString()}`
    if nodes[potentialNeighbor].status is not "wall") neighbors.append(potentialNeighbor)
  }
  if boardArray[x][y + 1]:
    potentialNeighbor = `${x.toString()}-${(y + 1).toString()}`
    if nodes[potentialNeighbor].status is not "wall") neighbors.append(potentialNeighbor)
  }
  return neighbors
}


def getDistance(nodeOne, nodeTwo:
  let currentCoordinates = nodeOne.id.split("-")
  let targetCoordinates = nodeTwo.id.split("-")
  let x1 = parseInt(currentCoordinates[0])
  let y1 = parseInt(currentCoordinates[1])
  let x2 = parseInt(targetCoordinates[0])
  let y2 = parseInt(targetCoordinates[1])
  if x2 < x1:
    if nodeOne.direction is "up":
      return [1, ["f"], "up"]
    elif nodeOne.direction is "right":
      return [2, ["l", "f"], "up"]
    elif nodeOne.direction is "left":
      return [2, ["r", "f"], "up"]
    elif nodeOne.direction is "down":
      return [3, ["r", "r", "f"], "up"]

  elif x2 > x1:
    if nodeOne.direction is "up":
      return [3, ["r", "r", "f"], "down"]
    elif nodeOne.direction is "right":
      return [2, ["r", "f"], "down"]
    elif nodeOne.direction is "left":
      return [2, ["l", "f"], "down"]
    elif nodeOne.direction is "down":
      return [1, ["f"], "down"]


  if y2 < y1:
    if nodeOne.direction is "up":
      return [2, ["l", "f"], "left"]
    elif nodeOne.direction is "right":
      return [3, ["l", "l", "f"], "left"]
    elif nodeOne.direction is "left":
      return [1, ["f"], "left"]
    elif nodeOne.direction is "down":
      return [2, ["r", "f"], "left"]

  elif y2 > y1:
    if nodeOne.direction is "up":
      return [2, ["r", "f"], "right"]
    elif nodeOne.direction is "right":
      return [1, ["f"], "right"]
    elif nodeOne.direction is "left":
      return [3, ["r", "r", "f"], "right"]
    elif nodeOne.direction is "down":
      return [2, ["l", "f"], "right"]




def manhattanDistance(nodeOne, nodeTwo):
  let nodeOneCoordinates = nodeOne.id.split("-").map(ele => parseInt(ele))
  let nodeTwoCoordinates = nodeTwo.id.split("-").map(ele => parseInt(ele))
  let xChange = Math.abs(nodeOneCoordinates[0] - nodeTwoCoordinates[0])
  let yChange = Math.abs(nodeOneCoordinates[1] - nodeTwoCoordinates[1])
  return (xChange + yChange)


module.exports = test