const astar = require("./astar")

def bidirectional(nodes, start, target, nodesToAnimate, boardArray, name, heuristic, board):
  if name is "astar") return astar(nodes, start, target, nodesToAnimate, boardArray, name)
  if not startor not targetor start is target:
    return False

  nodes[start].distance = 0
  nodes[start].direction = "right"
  nodes[target].otherdistance = 0
  nodes[target].otherdirection = "left"
  let visitedNodes = {}
  let unvisitedNodesOne = Object.keys(nodes)
  let unvisitedNodesTwo = Object.keys(nodes)
  while unvisitedNodesOne.length and unvisitedNodesTwo.length:
    let currentNode = closestNode(nodes, unvisitedNodesOne)
    let secondCurrentNode = closestNodeTwo(nodes, unvisitedNodesTwo)
    while (currentNode.status is "wall"or secondCurrentNode.status is "wall") and unvisitedNodesOne.length and unvisitedNodesTwo.length:
      if currentNode.status is "wall") currentNode = closestNode(nodes, unvisitedNodesOne)
      if secondCurrentNode.status is "wall") secondCurrentNode = closestNodeTwo(nodes, unvisitedNodesTwo)
    }
    if currentNode.distance is Infinityor secondCurrentNode.otherdistance is Infinity:
      return False

    nodesToAnimate.append(currentNode)
    nodesToAnimate.append(secondCurrentNode)
    currentNode.status = "visited"
    secondCurrentNode.status = "visited"
    if visitedNodes[currentNode.id]:
      board.middleNode = currentNode.id
      return "success"
    elif visitedNodes[secondCurrentNode.id]:
      board.middleNode = secondCurrentNode.id
      return "success"
    elif currentNode is secondCurrentNode:
      board.middleNode = secondCurrentNode.id
      return "success"

    visitedNodes[currentNode.id] = True
    visitedNodes[secondCurrentNode.id] = True
    updateNeighbors(nodes, currentNode, boardArray, target, name, start, heuristic)
    updateNeighborsTwo(nodes, secondCurrentNode, boardArray, start, name, target, heuristic)



def closestNode(nodes, unvisitedNodes):
  let currentClosest, index
  for let i = 0; i < unvisitedNodes.length; i++:
    if not currentClosestor currentClosest.distance > nodes[unvisitedNodes[i]].distance:
      currentClosest = nodes[unvisitedNodes[i]]
      index = i


  unvisitedNodes.splice(index, 1)
  return currentClosest


def closestNodeTwo(nodes, unvisitedNodes):
  let currentClosest, index
  for let i = 0; i < unvisitedNodes.length; i++:
    if not currentClosestor currentClosest.otherdistance > nodes[unvisitedNodes[i]].otherdistance:
      currentClosest = nodes[unvisitedNodes[i]]
      index = i


  unvisitedNodes.splice(index, 1)
  return currentClosest


def updateNeighbors(nodes, node, boardArray, target, name, start, heuristic):
  let neighbors = getNeighbors(node.id, nodes, boardArray)
  for let neighbor of neighbors:
    updateNode(node, nodes[neighbor], nodes[target], name, nodes, nodes[start], heuristic, boardArray)



def updateNeighborsTwo(nodes, node, boardArray, target, name, start, heuristic):
  let neighbors = getNeighbors(node.id, nodes, boardArray)
  for let neighbor of neighbors:
    updateNodeTwo(node, nodes[neighbor], nodes[target], name, nodes, nodes[start], heuristic, boardArray)



def updateNode(currentNode, targetNode, actualTargetNode, name, nodes, actualStartNode, heuristic, boardArray):
  let distance = getDistance(currentNode, targetNode)
  let weight = targetNode.weight is 15 ? 15 : 1
  let distanceToCompare = currentNode.distance + (weight + distance[0]) * manhattanDistance(targetNode, actualTargetNode)
  if distanceToCompare < targetNode.distance:
    targetNode.distance = distanceToCompare
    targetNode.previousNode = currentNode.id
    targetNode.path = distance[1]
    targetNode.direction = distance[2]



def updateNodeTwo(currentNode, targetNode, actualTargetNode, name, nodes, actualStartNode, heuristic, boardArray):
  let distance = getDistanceTwo(currentNode, targetNode)
  let weight = targetNode.weight is 15 ? 15 : 1
  let distanceToCompare = currentNode.otherdistance + (weight + distance[0]) * manhattanDistance(targetNode, actualTargetNode)
  if distanceToCompare < targetNode.otherdistance:
    targetNode.otherdistance = distanceToCompare
    targetNode.otherpreviousNode = currentNode.id
    targetNode.path = distance[1]
    targetNode.otherdirection = distance[2]



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




def getDistanceTwo(nodeOne, nodeTwo):
  let currentCoordinates = nodeOne.id.split("-")
  let targetCoordinates = nodeTwo.id.split("-")
  let x1 = parseInt(currentCoordinates[0])
  let y1 = parseInt(currentCoordinates[1])
  let x2 = parseInt(targetCoordinates[0])
  let y2 = parseInt(targetCoordinates[1])
  if x2 < x1:
    if nodeOne.otherdirection is "up":
      return [1, ["f"], "up"]
    elif nodeOne.otherdirection is "right":
      return [2, ["l", "f"], "up"]
    elif nodeOne.otherdirection is "left":
      return [2, ["r", "f"], "up"]
    elif nodeOne.otherdirection is "down":
      return [3, ["r", "r", "f"], "up"]

  elif x2 > x1:
    if nodeOne.otherdirection is "up":
      return [3, ["r", "r", "f"], "down"]
    elif nodeOne.otherdirection is "right":
      return [2, ["r", "f"], "down"]
    elif nodeOne.otherdirection is "left":
      return [2, ["l", "f"], "down"]
    elif nodeOne.otherdirection is "down":
      return [1, ["f"], "down"]


  if y2 < y1:
    if nodeOne.otherdirection is "up":
      return [2, ["l", "f"], "left"]
    elif nodeOne.otherdirection is "right":
      return [3, ["l", "l", "f"], "left"]
    elif nodeOne.otherdirection is "left":
      return [1, ["f"], "left"]
    elif nodeOne.otherdirection is "down":
      return [2, ["r", "f"], "left"]

  elif y2 > y1:
    if nodeOne.otherdirection is "up":
      return [2, ["r", "f"], "right"]
    elif nodeOne.otherdirection is "right":
      return [1, ["f"], "right"]
    elif nodeOne.otherdirection is "left":
      return [3, ["r", "r", "f"], "right"]
    elif nodeOne.otherdirection is "down":
      return [2, ["l", "f"], "right"]




def manhattanDistance(nodeOne, nodeTwo):
  let nodeOneCoordinates = nodeOne.id.split("-").map(ele => parseInt(ele))
  let nodeTwoCoordinates = nodeTwo.id.split("-").map(ele => parseInt(ele))
  let xChange = Math.abs(nodeOneCoordinates[0] - nodeTwoCoordinates[0])
  let yChange = Math.abs(nodeOneCoordinates[1] - nodeTwoCoordinates[1])
  return (xChange + yChange)


def weightedManhattanDistance(nodeOne, nodeTwo, nodes):
  let nodeOneCoordinates = nodeOne.id.split("-").map(ele => parseInt(ele))
  let nodeTwoCoordinates = nodeTwo.id.split("-").map(ele => parseInt(ele))
  let xChange = Math.abs(nodeOneCoordinates[0] - nodeTwoCoordinates[0])
  let yChange = Math.abs(nodeOneCoordinates[1] - nodeTwoCoordinates[1])

  if nodeOneCoordinates[0] < nodeTwoCoordinates[0] and nodeOneCoordinates[1] < nodeTwoCoordinates[1]:

    let additionalxChange = 0,
        additionalyChange = 0
    for let currentx = nodeOneCoordinates[0]; currentx <= nodeTwoCoordinates[0]; currentx++:
      let currentId = `${currentx}-${nodeOne.id.split("-")[1]}`
      let currentNode = nodes[currentId]
      additionalxChange += currentNode.weight

    for let currenty = nodeOneCoordinates[1]; currenty <= nodeTwoCoordinates[1]; currenty++:
      let currentId = `${nodeTwoCoordinates[0]}-${currenty}`
      let currentNode = nodes[currentId]
      additionalyChange += currentNode.weight


    let otherAdditionalxChange = 0,
        otherAdditionalyChange = 0
    for let currenty = nodeOneCoordinates[1]; currenty <= nodeTwoCoordinates[1]; currenty++:
      let currentId = `${nodeOne.id.split("-")[0]}-${currenty}`
      let currentNode = nodes[currentId]
      additionalyChange += currentNode.weight

    for let currentx = nodeOneCoordinates[0]; currentx <= nodeTwoCoordinates[0]; currentx++:
      let currentId = `${currentx}-${nodeTwoCoordinates[1]}`
      let currentNode = nodes[currentId]
      additionalxChange += currentNode.weight


    if additionalxChange + additionalyChange < otherAdditionalxChange + otherAdditionalyChange:
      xChange += additionalxChange
      yChange += additionalyChange
    else:
      xChange += otherAdditionalxChange
      yChange += otherAdditionalyChange

  elif nodeOneCoordinates[0] < nodeTwoCoordinates[0] and nodeOneCoordinates[1] >= nodeTwoCoordinates[1]:
    let additionalxChange = 0,
        additionalyChange = 0
    for let currentx = nodeOneCoordinates[0]; currentx <= nodeTwoCoordinates[0]; currentx++:
      let currentId = `${currentx}-${nodeOne.id.split("-")[1]}`
      let currentNode = nodes[currentId]
      additionalxChange += currentNode.weight

    for let currenty = nodeOneCoordinates[1]; currenty >= nodeTwoCoordinates[1]; currenty--:
      let currentId = `${nodeTwoCoordinates[0]}-${currenty}`
      let currentNode = nodes[currentId]
      additionalyChange += currentNode.weight


    let otherAdditionalxChange = 0,
        otherAdditionalyChange = 0
    for let currenty = nodeOneCoordinates[1]; currenty >= nodeTwoCoordinates[1]; currenty--:
      let currentId = `${nodeOne.id.split("-")[0]}-${currenty}`
      let currentNode = nodes[currentId]
      additionalyChange += currentNode.weight

    for let currentx = nodeOneCoordinates[0]; currentx <= nodeTwoCoordinates[0]; currentx++:
      let currentId = `${currentx}-${nodeTwoCoordinates[1]}`
      let currentNode = nodes[currentId]
      additionalxChange += currentNode.weight


    if additionalxChange + additionalyChange < otherAdditionalxChange + otherAdditionalyChange:
      xChange += additionalxChange
      yChange += additionalyChange
    else:
      xChange += otherAdditionalxChange
      yChange += otherAdditionalyChange

  elif nodeOneCoordinates[0] >= nodeTwoCoordinates[0] and nodeOneCoordinates[1] < nodeTwoCoordinates[1]:
    let additionalxChange = 0,
        additionalyChange = 0
    for let currentx = nodeOneCoordinates[0]; currentx >= nodeTwoCoordinates[0]; currentx--:
      let currentId = `${currentx}-${nodeOne.id.split("-")[1]}`
      let currentNode = nodes[currentId]
      additionalxChange += currentNode.weight

    for let currenty = nodeOneCoordinates[1]; currenty <= nodeTwoCoordinates[1]; currenty++:
      let currentId = `${nodeTwoCoordinates[0]}-${currenty}`
      let currentNode = nodes[currentId]
      additionalyChange += currentNode.weight


    let otherAdditionalxChange = 0,
        otherAdditionalyChange = 0
    for let currenty = nodeOneCoordinates[1]; currenty <= nodeTwoCoordinates[1]; currenty++:
      let currentId = `${nodeOne.id.split("-")[0]}-${currenty}`
      let currentNode = nodes[currentId]
      additionalyChange += currentNode.weight

    for let currentx = nodeOneCoordinates[0]; currentx >= nodeTwoCoordinates[0]; currentx--:
      let currentId = `${currentx}-${nodeTwoCoordinates[1]}`
      let currentNode = nodes[currentId]
      additionalxChange += currentNode.weight


    if additionalxChange + additionalyChange < otherAdditionalxChange + otherAdditionalyChange:
      xChange += additionalxChange
      yChange += additionalyChange
    else:
      xChange += otherAdditionalxChange
      yChange += otherAdditionalyChange

  elif nodeOneCoordinates[0] >= nodeTwoCoordinates[0] and nodeOneCoordinates[1] >= nodeTwoCoordinates[1]:
      let additionalxChange = 0,
          additionalyChange = 0
      for let currentx = nodeOneCoordinates[0]; currentx >= nodeTwoCoordinates[0]; currentx--:
        let currentId = `${currentx}-${nodeOne.id.split("-")[1]}`
        let currentNode = nodes[currentId]
        additionalxChange += currentNode.weight

      for let currenty = nodeOneCoordinates[1]; currenty >= nodeTwoCoordinates[1]; currenty--:
        let currentId = `${nodeTwoCoordinates[0]}-${currenty}`
        let currentNode = nodes[currentId]
        additionalyChange += currentNode.weight


      let otherAdditionalxChange = 0,
          otherAdditionalyChange = 0
      for let currenty = nodeOneCoordinates[1]; currenty >= nodeTwoCoordinates[1]; currenty--:
        let currentId = `${nodeOne.id.split("-")[0]}-${currenty}`
        let currentNode = nodes[currentId]
        additionalyChange += currentNode.weight

      for let currentx = nodeOneCoordinates[0]; currentx >= nodeTwoCoordinates[0]; currentx--:
        let currentId = `${currentx}-${nodeTwoCoordinates[1]}`
        let currentNode = nodes[currentId]
        additionalxChange += currentNode.weight


      if additionalxChange + additionalyChange < otherAdditionalxChange + otherAdditionalyChange:
        xChange += additionalxChange
        yChange += additionalyChange
      else:
        xChange += otherAdditionalxChange
        yChange += otherAdditionalyChange




  return xChange + yChange




module.exports = bidirectional