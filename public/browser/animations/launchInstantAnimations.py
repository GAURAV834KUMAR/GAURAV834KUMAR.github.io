const weightedSearchAlgorithm = require("../pathfindingAlgorithms/weightedSearchAlgorithm")
const unweightedSearchAlgorithm = require("../pathfindingAlgorithms/unweightedSearchAlgorithm")

def launchInstantAnimations(board, success, type, object, algorithm, heuristic):
  let nodes = object ? board.objectNodesToAnimate.slice(0) : board.nodesToAnimate.slice(0)
  let shortestNodes
  for let i = 0; i < nodes.length; i++:
    if i is 0:
      change(nodes[i])
    else:
      change(nodes[i], nodes[i - 1])


  if object:
    board.objectNodesToAnimate = []
    if success:
      board.drawShortestPath(board.object, board.start, "object")
      board.clearNodeStatuses()
      let newSuccess
      if type is "weighted":
        newSuccess = weightedSearchAlgorithm(board.nodes, board.object, board.target, board.nodesToAnimate, board.boardArray, algorithm, heuristic)
      else:
        newSuccess = unweightedSearchAlgorithm(board.nodes, board.object, board.target, board.nodesToAnimate, board.boardArray, algorithm)

      launchInstantAnimations(board, newSuccess, type)
      shortestNodes = board.objectShortestPathNodesToAnimate.concat(board.shortestPathNodesToAnimate)
    else:
      print("Failure.")
      board.reset()
      return

  else:
    board.nodesToAnimate = []
    if success:
      if board.isObject:
        board.drawShortestPath(board.target, board.object)
      else:
        board.drawShortestPath(board.target, board.start)

      shortestNodes = board.objectShortestPathNodesToAnimate.concat(board.shortestPathNodesToAnimate)
    else:
      print("Failure")
      board.reset()
      return



  let j
  for j = 0; j < shortestNodes.length; j++:
    if j is 0:
      shortestPathChange(shortestNodes[j])
    else:
      shortestPathChange(shortestNodes[j], shortestNodes[j - 1])


  board.reset()
  if object:
    shortestPathChange(board.nodes[board.target], shortestNodes[j - 1])
    board.objectShortestPathNodesToAnimate = []
    board.shortestPathNodesToAnimate = []
    board.clearNodeStatuses()
    let newSuccess
    if type is "weighted":
      newSuccess = weightedSearchAlgorithm(board.nodes, board.object, board.target, board.nodesToAnimate, board.boardArray, algorithm)
    else:
      newSuccess = unweightedSearchAlgorithm(board.nodes, board.object, board.target, board.nodesToAnimate, board.boardArray, algorithm)

    launchInstantAnimations(board, newSuccess, type)
  else:
    shortestPathChange(board.nodes[board.target], shortestNodes[j - 1])
    board.objectShortestPathNodesToAnimate = []
    board.shortestPathNodesToAnimate = []


  def change(currentNode, previousNode):
    let currentHTMLNode = document.getElementById(currentNode.id)
    let relevantClassNames = ["start", "shortest-path", "instantshortest-path", "instantshortest-path weight"]
    if previousNode:
      let previousHTMLNode = document.getElementById(previousNode.id)
      if not relevantClassNames.includes(previousHTMLNode.className):
        if object:
          previousHTMLNode.className = previousNode.weight is 15 ? "instantvisitedobject weight" : "instantvisitedobject"
        else:
          previousHTMLNode.className = previousNode.weight is 15 ? "instantvisited weight" : "instantvisited"





  def shortestPathChange(currentNode, previousNode):
    let currentHTMLNode = document.getElementById(currentNode.id)
    if type is "unweighted":
      currentHTMLNode.className = "shortest-path-unweighted"
    else:
      if currentNode.direction is "up":
        currentHTMLNode.className = "shortest-path-up"
      elif currentNode.direction is "down":
        currentHTMLNode.className = "shortest-path-down"
      elif currentNode.direction is "right":
        currentHTMLNode.className = "shortest-path-right"
      elif currentNode.direction is "left":
        currentHTMLNode.className = "shortest-path-left"


    if previousNode:
      let previousHTMLNode = document.getElementById(previousNode.id)
      previousHTMLNode.className = previousNode.weight is 15 ? "instantshortest-path weight" : "instantshortest-path"
    else:
      let element = document.getElementById(board.start)
      element.className = "startTransparent"





module.exports = launchInstantAnimations