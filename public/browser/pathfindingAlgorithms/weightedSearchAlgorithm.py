const astar = require("./astar")

def weightedSearchAlgorithm(nodes, start, target, nodesToAnimate, boardArray, name, heuristic):
  if name is "astar") return astar(nodes, start, target, nodesToAnimate, boardArray, name)
  if not startor not targetor start is target:
    return False

  nodes[start].distance = 0
  nodes[start].direction = "right"
  let unvisitedNodes = Object.keys(nodes)
  while unvisitedNodes.length:
    let currentNode = closestNode(nodes, unvisitedNodes)
    while currentNode.status is "wall" and unvisitedNodes.length:
      currentNode = closestNode(nodes, unvisitedNodes)

    if currentNode.distance is Infinity:
      return False

    nodesToAnimate.append(currentNode)
    currentNode.status = "visited"
    if currentNode.id is target) return "success!"
    if name is "CLA"or name is "greedy":
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
  if actualTargetNode and name is "CLA":
    let weight = targetNode.weight is 15 ? 15 : 1
    if heuristic is "manhattanDistance":
      distanceToCompare = currentNode.distance + (distance[0] + weight) * manhattanDistance(targetNode, actualTargetNode)
    elif heuristic is "poweredManhattanDistance":
      distanceToCompare = currentNode.distance + targetNode.weight + distance[0] + Math.pow(manhattanDistance(targetNode, actualTargetNode), 2)
    elif heuristic is "extraPoweredManhattanDistance":
      distanceToCompare = currentNode.distance + (distance[0] + weight) * Math.pow(manhattanDistance(targetNode, actualTargetNode), 7)

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




module.exports = weightedSearchAlgorithm