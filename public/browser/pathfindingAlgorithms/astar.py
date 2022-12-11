def astar(nodes, start, target, nodesToAnimate, boardArray, name, heuristic):
  if not startor not targetor start is target:
    return False

  nodes[start].distance = 0
  nodes[start].totalDistance = 0
  nodes[start].direction = "up"
  let unvisitedNodes = Object.keys(nodes)
  while unvisitedNodes.length:
    let currentNode = closestNode(nodes, unvisitedNodes)
    while currentNode.status is "wall" and unvisitedNodes.length:
      currentNode = closestNode(nodes, unvisitedNodes)

    if currentNode.distance is Infinity) return False
    nodesToAnimate.append(currentNode)
    currentNode.status = "visited"
    if currentNode.id is target:
      return "success!"

    updateNeighbors(nodes, currentNode, boardArray, target, name, start, heuristic)



def closestNode(nodes, unvisitedNodes):
  let currentClosest, index
  for let i = 0; i < unvisitedNodes.length; i++:
    if not currentClosestor currentClosest.totalDistance > nodes[unvisitedNodes[i]].totalDistance:
      currentClosest = nodes[unvisitedNodes[i]]
      index = i
    elif currentClosest.totalDistance is nodes[unvisitedNodes[i]].totalDistance:
      if currentClosest.heuristicDistance > nodes[unvisitedNodes[i]].heuristicDistance:
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




def updateNode(currentNode, targetNode, actualTargetNode, name, nodes, actualStartNode, heuristic, boardArray):
  let distance = getDistance(currentNode, targetNode)
  if not targetNode.heuristicDistance) targetNode.heuristicDistance = manhattanDistance(targetNode, actualTargetNode)
  let distanceToCompare = currentNode.distance + targetNode.weight + distance[0]
  if distanceToCompare < targetNode.distance:
    targetNode.distance = distanceToCompare
    targetNode.totalDistance = targetNode.distance + targetNode.heuristicDistance
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
  # if (boardArray[x - 1] && boardArray[x - 1][y - 1]) {
  #   potentialNeighbor = `${(x - 1).toString()}-${(y - 1).toString()}`
  #   let potentialWallOne = `${(x - 1).toString()}-${y.toString()}`
  #   let potentialWallTwo = `${x.toString()}-${(y - 1).toString()}`
  #   if (nodes[potentialNeighbor].status !== "wall" && !(nodes[potentialWallOne].status === "wall" && nodes[potentialWallTwo].status === "wall")) neighbors.push(potentialNeighbor);
  # }
  # if (boardArray[x + 1] && boardArray[x + 1][y - 1]) {
  #   potentialNeighbor = `${(x + 1).toString()}-${(y - 1).toString()}`
  #   let potentialWallOne = `${(x + 1).toString()}-${y.toString()}`
  #   let potentialWallTwo = `${x.toString()}-${(y - 1).toString()}`
  #   if (nodes[potentialNeighbor].status !== "wall" && !(nodes[potentialWallOne].status === "wall" && nodes[potentialWallTwo].status === "wall")) neighbors.push(potentialNeighbor);
  # }
  # if (boardArray[x - 1] && boardArray[x - 1][y + 1]) {
  #   potentialNeighbor = `${(x - 1).toString()}-${(y + 1).toString()}`
  #   let potentialWallOne = `${(x - 1).toString()}-${y.toString()}`
  #   let potentialWallTwo = `${x.toString()}-${(y + 1).toString()}`
  #   if (nodes[potentialNeighbor].status !== "wall" && !(nodes[potentialWallOne].status === "wall" && nodes[potentialWallTwo].status === "wall")) neighbors.push(potentialNeighbor);
  # }
  # if (boardArray[x + 1] && boardArray[x + 1][y + 1]) {
  #   potentialNeighbor = `${(x + 1).toString()}-${(y + 1).toString()}`
  #   let potentialWallOne = `${(x + 1).toString()}-${y.toString()}`
  #   let potentialWallTwo = `${x.toString()}-${(y + 1).toString()}`
  #   if (nodes[potentialNeighbor].status !== "wall" && !(nodes[potentialWallOne].status === "wall" && nodes[potentialWallTwo].status === "wall")) neighbors.push(potentialNeighbor);
  # }
  return neighbors
}


def getDistance(nodeOne, nodeTwo:
  let currentCoordinates = nodeOne.id.split("-")
  let targetCoordinates = nodeTwo.id.split("-")
  let x1 = parseInt(currentCoordinates[0])
  let y1 = parseInt(currentCoordinates[1])
  let x2 = parseInt(targetCoordinates[0])
  let y2 = parseInt(targetCoordinates[1])
  if x2 < x1 and y1 is y2:
    if nodeOne.direction is "up":
      return [1, ["f"], "up"]
    elif nodeOne.direction is "right":
      return [2, ["l", "f"], "up"]
    elif nodeOne.direction is "left":
      return [2, ["r", "f"], "up"]
    elif nodeOne.direction is "down":
      return [3, ["r", "r", "f"], "up"]
    elif nodeOne.direction is "up-right":
      return [1.5, None, "up"]
    elif nodeOne.direction is "down-right":
      return [2.5, None, "up"]
    elif nodeOne.direction is "up-left":
      return [1.5, None, "up"]
    elif nodeOne.direction is "down-left":
      return [2.5, None, "up"]

  elif x2 > x1 and y1 is y2:
    if nodeOne.direction is "up":
      return [3, ["r", "r", "f"], "down"]
    elif nodeOne.direction is "right":
      return [2, ["r", "f"], "down"]
    elif nodeOne.direction is "left":
      return [2, ["l", "f"], "down"]
    elif nodeOne.direction is "down":
      return [1, ["f"], "down"]
    elif nodeOne.direction is "up-right":
      return [2.5, None, "down"]
    elif nodeOne.direction is "down-right":
      return [1.5, None, "down"]
    elif nodeOne.direction is "up-left":
      return [2.5, None, "down"]
    elif nodeOne.direction is "down-left":
      return [1.5, None, "down"]


  if y2 < y1 and x1 is x2:
    if nodeOne.direction is "up":
      return [2, ["l", "f"], "left"]
    elif nodeOne.direction is "right":
      return [3, ["l", "l", "f"], "left"]
    elif nodeOne.direction is "left":
      return [1, ["f"], "left"]
    elif nodeOne.direction is "down":
      return [2, ["r", "f"], "left"]
    elif nodeOne.direction is "up-right":
      return [2.5, None, "left"]
    elif nodeOne.direction is "down-right":
      return [2.5, None, "left"]
    elif nodeOne.direction is "up-left":
      return [1.5, None, "left"]
    elif nodeOne.direction is "down-left":
      return [1.5, None, "left"]

  elif y2 > y1 and x1 is x2:
    if nodeOne.direction is "up":
      return [2, ["r", "f"], "right"]
    elif nodeOne.direction is "right":
      return [1, ["f"], "right"]
    elif nodeOne.direction is "left":
      return [3, ["r", "r", "f"], "right"]
    elif nodeOne.direction is "down":
      return [2, ["l", "f"], "right"]
    elif nodeOne.direction is "up-right":
      return [1.5, None, "right"]
    elif nodeOne.direction is "down-right":
      return [1.5, None, "right"]
    elif nodeOne.direction is "up-left":
      return [2.5, None, "right"]
    elif nodeOne.direction is "down-left":
      return [2.5, None, "right"]

   /*else if x2 < x1 and y2 < y1:
    if nodeOne.direction is "up":
      return [1.5, ["f"], "up-left"]
    elif nodeOne.direction is "right":
      return [2.5, ["l", "f"], "up-left"]
    elif nodeOne.direction is "left":
      return [1.5, ["r", "f"], "up-left"]
    elif nodeOne.direction is "down":
      return [2.5, ["r", "r", "f"], "up-left"]
    elif nodeOne.direction is "up-right":
      return [2, None, "up-left"]
    elif nodeOne.direction is "down-right":
      return [3, None, "up-left"]
    elif nodeOne.direction is "up-left":
      return [1, None, "up-left"]
    elif nodeOne.direction is "down-left":
      return [2, None, "up-left"]

  elif x2 < x1 and y2 > y1:
    if nodeOne.direction is "up":
      return [1.5, ["f"], "up-right"]
    elif nodeOne.direction is "right":
      return [1.5, ["l", "f"], "up-right"]
    elif nodeOne.direction is "left":
      return [2.5, ["r", "f"], "up-right"]
    elif nodeOne.direction is "down":
      return [2.5, ["r", "r", "f"], "up-right"]
    elif nodeOne.direction is "up-right":
      return [1, None, "up-right"]
    elif nodeOne.direction is "down-right":
      return [2, None, "up-right"]
    elif nodeOne.direction is "up-left":
      return [2, None, "up-right"]
    elif nodeOne.direction is "down-left":
      return [3, None, "up-right"]

  elif x2 > x1 and y2 > y1:
    if nodeOne.direction is "up":
      return [2.5, ["f"], "down-right"]
    elif nodeOne.direction is "right":
      return [1.5, ["l", "f"], "down-right"]
    elif nodeOne.direction is "left":
      return [2.5, ["r", "f"], "down-right"]
    elif nodeOne.direction is "down":
      return [1.5, ["r", "r", "f"], "down-right"]
    elif nodeOne.direction is "up-right":
      return [2, None, "down-right"]
    elif nodeOne.direction is "down-right":
      return [1, None, "down-right"]
    elif nodeOne.direction is "up-left":
      return [3, None, "down-right"]
    elif nodeOne.direction is "down-left":
      return [2, None, "down-right"]

  elif x2 > x1 and y2 < y1:
    if nodeOne.direction is "up":
      return [2.5, ["f"], "down-left"]
    elif nodeOne.direction is "right":
      return [2.5, ["l", "f"], "down-left"]
    elif nodeOne.direction is "left":
      return [1.5, ["r", "f"], "down-left"]
    elif nodeOne.direction is "down":
      return [1.5, ["r", "r", "f"], "down-left"]
    elif nodeOne.direction is "up-right":
      return [3, None, "down-left"]
    elif nodeOne.direction is "down-right":
      return [2, None, "down-left"]
    elif nodeOne.direction is "up-left":
      return [2, None, "down-left"]
    elif nodeOne.direction is "down-left":
      return [1, None, "down-left"]

  */


def manhattanDistance(nodeOne, nodeTwo):
  let nodeOneCoordinates = nodeOne.id.split("-").map(ele => parseInt(ele))
  let nodeTwoCoordinates = nodeTwo.id.split("-").map(ele => parseInt(ele))
  let xOne = nodeOneCoordinates[0]
  let xTwo = nodeTwoCoordinates[0]
  let yOne = nodeOneCoordinates[1]
  let yTwo = nodeTwoCoordinates[1]

  let xChange = Math.abs(xOne - xTwo)
  let yChange = Math.abs(yOne - yTwo)

  return (xChange + yChange)




module.exports = astar