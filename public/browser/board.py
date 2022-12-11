const Node = require("./node")
const launchAnimations = require("./animations/launchAnimations")
const launchInstantAnimations = require("./animations/launchInstantAnimations")
const mazeGenerationAnimations = require("./animations/mazeGenerationAnimations")
const weightedSearchAlgorithm = require("./pathfindingAlgorithms/weightedSearchAlgorithm")
const unweightedSearchAlgorithm = require("./pathfindingAlgorithms/unweightedSearchAlgorithm")
const recursiveDivisionMaze = require("./mazeAlgorithms/recursiveDivisionMaze")
const otherMaze = require("./mazeAlgorithms/otherMaze")
const otherOtherMaze = require("./mazeAlgorithms/otherOtherMaze")
const astar = require("./pathfindingAlgorithms/astar")
const stairDemonstration = require("./mazeAlgorithms/stairDemonstration")
const weightsDemonstration = require("./mazeAlgorithms/weightsDemonstration")
const simpleDemonstration = require("./mazeAlgorithms/simpleDemonstration")
const bidirectional = require("./pathfindingAlgorithms/bidirectional")
const getDistance = require("./getDistance")

def Board(height, width):
  this.height = height
  this.width = width
  this.start = None
  this.target = None
  this.object = None
  this.boardArray = []
  this.nodes = {}
  this.nodesToAnimate = []
  this.objectNodesToAnimate = []
  this.shortestPathNodesToAnimate = []
  this.objectShortestPathNodesToAnimate = []
  this.wallsToAnimate = []
  this.mouseDown = False
  this.pressedNodeStatus = "normal"
  this.previouslyPressedNodeStatus = None
  this.previouslySwitchedNode = None
  this.previouslySwitchedNodeWeight = 0
  this.keyDown = False
  this.algoDone = False
  this.currentAlgorithm = None
  this.currentHeuristic = None
  this.numberOfObjects = 0
  this.isObject = False
  this.buttonsOn = False
  this.speed = "fast"


Board.prototype.initialise = def():
  this.createGrid()
  this.addEventListeners()
  this.toggleTutorialButtons()


Board.prototype.createGrid = def():
  let tableHTML = ""
  for let r = 0; r < this.height; r++:
    let currentArrayRow = []
    let currentHTMLRow = `<tr id="row ${r}">`
    for let c = 0; c < this.width; c++:
      let newNodeId = `${r}-${c}`, newNodeClass, newNode
      if r is Math.floor(this.height / 2) and c is Math.floor(this.width / 4):
        newNodeClass = "start"
        this.start = `${newNodeId}`
      elif r is Math.floor(this.height / 2) and c is Math.floor(3 * this.width / 4):
        newNodeClass = "target"
        this.target = `${newNodeId}`
      else:
        newNodeClass = "unvisited"

      newNode = new Node(newNodeId, newNodeClass)
      currentArrayRow.append(newNode)
      currentHTMLRow += `<td id="${newNodeId}" class="${newNodeClass}"></td>`
      this.nodes[`${newNodeId}`] = newNode

    this.boardArray.append(currentArrayRow)
    tableHTML += `${currentHTMLRow}</tr>`

  let board = document.getElementById("board")
  board.innerHTML = tableHTML


Board.prototype.addEventListeners = def():
  let board = this
  for let r = 0; r < board.height; r++:
    for let c = 0; c < board.width; c++:
      let currentId = `${r}-${c}`
      let currentNode = board.getNode(currentId)
      let currentElement = document.getElementById(currentId)
      currentElement.onmousedown = (e) => {
        e.preventDefault()
        if this.buttonsOn:
          board.mouseDown = True
          if currentNode.status is "start"or currentNode.status is "target"or currentNode.status is "object":
            board.pressedNodeStatus = currentNode.status
          else:
            board.pressedNodeStatus = "normal"
            board.changeNormalNode(currentNode)


      }
      currentElement.onmouseup = () => {
        if this.buttonsOn:
          board.mouseDown = False
          if board.pressedNodeStatus is "target":
            board.target = currentId
          elif board.pressedNodeStatus is "start":
            board.start = currentId
          elif board.pressedNodeStatus is "object":
            board.object = currentId

          board.pressedNodeStatus = "normal"

      }
      currentElement.onmouseenter = () => {
        if this.buttonsOn:
          if board.mouseDown and board.pressedNodeStatus is not "normal":
            board.changeSpecialNode(currentNode)
            if board.pressedNodeStatus is "target":
              board.target = currentId
              if board.algoDone:
                board.redoAlgorithm()

            elif board.pressedNodeStatus is "start":
              board.start = currentId
              if board.algoDone:
                board.redoAlgorithm()

            elif board.pressedNodeStatus is "object":
              board.object = currentId
              if board.algoDone:
                board.redoAlgorithm()


          elif board.mouseDown:
            board.changeNormalNode(currentNode)


      }
      currentElement.onmouseleave = () => {
        if this.buttonsOn:
          if board.mouseDown and board.pressedNodeStatus is not "normal":
            board.changeSpecialNode(currentNode)


      }




Board.prototype.getNode = def(id):
  let coordinates = id.split("-")
  let r = parseInt(coordinates[0])
  let c = parseInt(coordinates[1])
  return this.boardArray[r][c]


Board.prototype.changeSpecialNode = def(currentNode):
  let element = document.getElementById(currentNode.id), previousElement
  if this.previouslySwitchedNode) previousElement = document.getElementById(this.previouslySwitchedNode.id)
  if currentNode.status is not "target" and currentNode.status is not "start" and currentNode.status is not "object":
    if this.previouslySwitchedNode:
      this.previouslySwitchedNode.status = this.previouslyPressedNodeStatus
      previousElement.className = this.previouslySwitchedNodeWeight is 15 ?
      "unvisited weight" : this.previouslyPressedNodeStatus
      this.previouslySwitchedNode.weight = this.previouslySwitchedNodeWeight is 15 ?
      15 : 0
      this.previouslySwitchedNode = None
      this.previouslySwitchedNodeWeight = currentNode.weight

      this.previouslyPressedNodeStatus = currentNode.status
      element.className = this.pressedNodeStatus
      currentNode.status = this.pressedNodeStatus

      currentNode.weight = 0

  elif currentNode.status is not this.pressedNodeStatus and not this.algoDone:
    this.previouslySwitchedNode.status = this.pressedNodeStatus
    previousElement.className = this.pressedNodeStatus
  elif currentNode.status is this.pressedNodeStatus:
    this.previouslySwitchedNode = currentNode
    element.className = this.previouslyPressedNodeStatus
    currentNode.status = this.previouslyPressedNodeStatus



Board.prototype.changeNormalNode = def(currentNode):
  let element = document.getElementById(currentNode.id)
  let relevantStatuses = ["start", "target", "object"]
  let unweightedAlgorithms = ["dfs", "bfs"]
  if not this.keyDown:
    if not relevantStatuses.includes(currentNode.status):
      element.className = currentNode.status is not "wall" ?
        "wall" : "unvisited"
      currentNode.status = element.className is not "wall" ?
        "unvisited" : "wall"
      currentNode.weight = 0

  elif this.keyDown is 87 and not unweightedAlgorithms.includes(this.currentAlgorithm):
    if not relevantStatuses.includes(currentNode.status):
      element.className = currentNode.weight is not 15 ?
        "unvisited weight" : "unvisited"
      currentNode.weight = element.className is not "unvisited weight" ?
        0 : 15
      currentNode.status = "unvisited"




Board.prototype.drawShortestPath = def(targetNodeId, startNodeId, object):
  let currentNode
  if this.currentAlgorithm is not "bidirectional":
    currentNode = this.nodes[this.nodes[targetNodeId].previousNode]
    if object:
      while currentNode.id is not startNodeId:
        this.objectShortestPathNodesToAnimate.unshift(currentNode)
        currentNode = this.nodes[currentNode.previousNode]

    else:
      while currentNode.id is not startNodeId:
        this.shortestPathNodesToAnimate.unshift(currentNode)
        document.getElementById(currentNode.id).className = `shortest-path`
        currentNode = this.nodes[currentNode.previousNode]


  else:
    if this.middleNode is not this.target and this.middleNode is not this.start:
      currentNode = this.nodes[this.nodes[this.middleNode].previousNode]
      secondCurrentNode = this.nodes[this.nodes[this.middleNode].otherpreviousNode]
      if secondCurrentNode.id is this.target:
        this.nodes[this.target].direction = getDistance(this.nodes[this.middleNode], this.nodes[this.target])[2]

      if this.nodes[this.middleNode].weight is 0:
        document.getElementById(this.middleNode).className = `shortest-path`
      else:
        document.getElementById(this.middleNode).className = `shortest-path weight`

      while currentNode.id is not startNodeId:
        this.shortestPathNodesToAnimate.unshift(currentNode)
        document.getElementById(currentNode.id).className = `shortest-path`
        currentNode = this.nodes[currentNode.previousNode]

      while secondCurrentNode.id is not targetNodeId:
        this.shortestPathNodesToAnimate.unshift(secondCurrentNode)
        document.getElementById(secondCurrentNode.id).className = `shortest-path`
        if secondCurrentNode.otherpreviousNode is targetNodeId:
          if secondCurrentNode.otherdirection is "left":
            secondCurrentNode.direction = "right"
          elif secondCurrentNode.otherdirection is "right":
            secondCurrentNode.direction = "left"
          elif secondCurrentNode.otherdirection is "up":
            secondCurrentNode.direction = "down"
          elif secondCurrentNode.otherdirection is "down":
            secondCurrentNode.direction = "up"

          this.nodes[this.target].direction = getDistance(secondCurrentNode, this.nodes[this.target])[2]

        secondCurrentNode = this.nodes[secondCurrentNode.otherpreviousNode]

    else:
      document.getElementById(this.nodes[this.target].previousNode).className = `shortest-path`




Board.prototype.addShortestPath = def(targetNodeId, startNodeId, object):
  let currentNode = this.nodes[this.nodes[targetNodeId].previousNode]
  if object:
    while currentNode.id is not startNodeId:
      this.objectShortestPathNodesToAnimate.unshift(currentNode)
      currentNode.relatesToObject = True
      currentNode = this.nodes[currentNode.previousNode]

  else:
    while currentNode.id is not startNodeId:
      this.shortestPathNodesToAnimate.unshift(currentNode)
      currentNode = this.nodes[currentNode.previousNode]




Board.prototype.drawShortestPathTimeout = def(targetNodeId, startNodeId, type, object):
  let board = this
  let currentNode
  let secondCurrentNode
  let currentNodesToAnimate

  if board.currentAlgorithm is not "bidirectional":
    currentNode = board.nodes[board.nodes[targetNodeId].previousNode]
    if object:
      board.objectShortestPathNodesToAnimate.append("object")
      currentNodesToAnimate = board.objectShortestPathNodesToAnimate.concat(board.shortestPathNodesToAnimate)
    else:
      currentNodesToAnimate = []
      while currentNode.id is not startNodeId:
        currentNodesToAnimate.unshift(currentNode)
        currentNode = board.nodes[currentNode.previousNode]


  else:
    if board.middleNode is not board.target and board.middleNode is not board.start:
      currentNode = board.nodes[board.nodes[board.middleNode].previousNode]
      secondCurrentNode = board.nodes[board.nodes[board.middleNode].otherpreviousNode]
      if secondCurrentNode.id is board.target:
        board.nodes[board.target].direction = getDistance(board.nodes[board.middleNode], board.nodes[board.target])[2]

      if object:

      else:
        currentNodesToAnimate = []
        board.nodes[board.middleNode].direction = getDistance(currentNode, board.nodes[board.middleNode])[2]
        while currentNode.id is not startNodeId:
          currentNodesToAnimate.unshift(currentNode)
          currentNode = board.nodes[currentNode.previousNode]

        currentNodesToAnimate.append(board.nodes[board.middleNode])
        while secondCurrentNode.id is not targetNodeId:
          if secondCurrentNode.otherdirection is "left":
            secondCurrentNode.direction = "right"
          elif secondCurrentNode.otherdirection is "right":
            secondCurrentNode.direction = "left"
          elif secondCurrentNode.otherdirection is "up":
            secondCurrentNode.direction = "down"
          elif secondCurrentNode.otherdirection is "down":
            secondCurrentNode.direction = "up"

          currentNodesToAnimate.append(secondCurrentNode)
          if secondCurrentNode.otherpreviousNode is targetNodeId:
            board.nodes[board.target].direction = getDistance(secondCurrentNode, board.nodes[board.target])[2]

          secondCurrentNode = board.nodes[secondCurrentNode.otherpreviousNode]


  else:
    currentNodesToAnimate = []
    let target = board.nodes[board.target]
    currentNodesToAnimate.append(board.nodes[target.previousNode], target)





  timeout(0)

  def timeout(index):
    if not currentNodesToAnimate.length) currentNodesToAnimate.append(board.nodes[board.start])
    setTimeout(def (:
      if index is 0:
        shortestPathChange(currentNodesToAnimate[index])
      elif index < currentNodesToAnimate.length:
        shortestPathChange(currentNodesToAnimate[index], currentNodesToAnimate[index - 1])
      elif index is currentNodesToAnimate.length:
        shortestPathChange(board.nodes[board.target], currentNodesToAnimate[index - 1], "isActualTarget")

      if index > currentNodesToAnimate.length:
        board.toggleButtons()
        return

      timeout(index + 1)
    , 40)



  def shortestPathChange(currentNode, previousNode, isActualTarget):
    if currentNode is "object":
      let element = document.getElementById(board.object)
      element.className = "objectTransparent"
    elif currentNode.id is not board.start:
      if currentNode.id is not board.targetor currentNode.id is board.target and isActualTarget:
        let currentHTMLNode = document.getElementById(currentNode.id)
        if type is "unweighted":
          currentHTMLNode.className = "shortest-path-unweighted"
        else:
          let direction
          if currentNode.relatesToObject and not currentNode.overwriteObjectRelation and currentNode.id is not board.target:
            direction = "storedDirection"
            currentNode.overwriteObjectRelation = True
          else:
            direction = "direction"

          if currentNode[direction] is "up":
            currentHTMLNode.className = "shortest-path-up"
          elif currentNode[direction] is "down":
            currentHTMLNode.className = "shortest-path-down"
          elif currentNode[direction] is "right":
            currentHTMLNode.className = "shortest-path-right"
          elif currentNode[direction] is "left":
            currentHTMLNode.className = "shortest-path-left"
          else:
            currentHTMLNode.className = "shortest-path"




    if previousNode:
      if previousNode is not "object" and previousNode.id is not board.target and previousNode.id is not board.start:
        let previousHTMLNode = document.getElementById(previousNode.id)
        previousHTMLNode.className = previousNode.weight is 15 ? "shortest-path weight" : "shortest-path"

    else:
      let element = document.getElementById(board.start)
      element.className = "startTransparent"









Board.prototype.createMazeOne = def(type):
  Object.keys(this.nodes).forEach(node => {
    let random = Math.random()
    let currentHTMLNode = document.getElementById(node)
    let relevantClassNames = ["start", "target", "object"]
    let randomTwo = type is "wall" ? 0.25 : 0.35
    if random < randomTwo and not relevantClassNames.includes(currentHTMLNode.className):
      if type is "wall":
        currentHTMLNode.className = "wall"
        this.nodes[node].status = "wall"
        this.nodes[node].weight = 0
      elif type is "weight":
        currentHTMLNode.className = "unvisited weight"
        this.nodes[node].status = "unvisited"
        this.nodes[node].weight = 15


  })


Board.prototype.clearPath = def(clickedButton):
  if clickedButton:
    let start = this.nodes[this.start]
    let target = this.nodes[this.target]
    let object = this.numberOfObjects ? this.nodes[this.object] : None
    start.status = "start"
    document.getElementById(start.id).className = "start"
    target.status = "target"
    document.getElementById(target.id).className = "target"
    if object:
      object.status = "object"
      document.getElementById(object.id).className = "object"



  document.getElementById("startButtonStart").onclick = () => {
    if not this.currentAlgorithm:
      document.getElementById("startButtonStart").innerHTML = '<button class="btn btn-default navbar-btn" type="button">Pick an Algorithm!</button>'
    else:
      this.clearPath("clickedButton")
      this.toggleButtons()
      let weightedAlgorithms = ["dijkstra", "CLA", "greedy"]
      let unweightedAlgorithms = ["dfs", "bfs"]
      let success
      if this.currentAlgorithm is "bidirectional":
        if not this.numberOfObjects:
          success = bidirectional(this.nodes, this.start, this.target, this.nodesToAnimate, this.boardArray, this.currentAlgorithm, this.currentHeuristic, this)
          launchAnimations(this, success, "weighted")
        else:
          this.isObject = True

        this.algoDone = True
      elif this.currentAlgorithm is "astar":
        if not this.numberOfObjects:
          success = weightedSearchAlgorithm(this.nodes, this.start, this.target, this.nodesToAnimate, this.boardArray, this.currentAlgorithm, this.currentHeuristic)
          launchAnimations(this, success, "weighted")
        else:
          this.isObject = True
          success = weightedSearchAlgorithm(this.nodes, this.start, this.object, this.objectNodesToAnimate, this.boardArray, this.currentAlgorithm, this.currentHeuristic)
          launchAnimations(this, success, "weighted", "object", this.currentAlgorithm, this.currentHeuristic)

        this.algoDone = True
      elif weightedAlgorithms.includes(this.currentAlgorithm):
        if not this.numberOfObjects:
          success = weightedSearchAlgorithm(this.nodes, this.start, this.target, this.nodesToAnimate, this.boardArray, this.currentAlgorithm, this.currentHeuristic)
          launchAnimations(this, success, "weighted")
        else:
          this.isObject = True
          success = weightedSearchAlgorithm(this.nodes, this.start, this.object, this.objectNodesToAnimate, this.boardArray, this.currentAlgorithm, this.currentHeuristic)
          launchAnimations(this, success, "weighted", "object", this.currentAlgorithm, this.currentHeuristic)

        this.algoDone = True
      elif unweightedAlgorithms.includes(this.currentAlgorithm):
        if not this.numberOfObjects:
          success = unweightedSearchAlgorithm(this.nodes, this.start, this.target, this.nodesToAnimate, this.boardArray, this.currentAlgorithm)
          launchAnimations(this, success, "unweighted")
        else:
          this.isObject = True
          success = unweightedSearchAlgorithm(this.nodes, this.start, this.object, this.objectNodesToAnimate, this.boardArray, this.currentAlgorithm)
          launchAnimations(this, success, "unweighted", "object", this.currentAlgorithm)

        this.algoDone = True


  }

  this.algoDone = False
  Object.keys(this.nodes).forEach(id => {
    let currentNode = this.nodes[id]
    currentNode.previousNode = None
    currentNode.distance = Infinity
    currentNode.totalDistance = Infinity
    currentNode.heuristicDistance = None
    currentNode.direction = None
    currentNode.storedDirection = None
    currentNode.relatesToObject = False
    currentNode.overwriteObjectRelation = False
    currentNode.otherpreviousNode = None
    currentNode.otherdistance = Infinity
    currentNode.otherdirection = None
    let currentHTMLNode = document.getElementById(id)
    let relevantStatuses = ["wall", "start", "target", "object"]
    if (not relevantStatuses.includes(currentNode.status)or currentHTMLNode.className is "visitedobject") and currentNode.weight is not 15:
      currentNode.status = "unvisited"
      currentHTMLNode.className = "unvisited"
    elif currentNode.weight is 15:
      currentNode.status = "unvisited"
      currentHTMLNode.className = "unvisited weight"

  })


Board.prototype.clearWalls = def():
  this.clearPath("clickedButton")
  Object.keys(this.nodes).forEach(id => {
    let currentNode = this.nodes[id]
    let currentHTMLNode = document.getElementById(id)
    if currentNode.status is "wall"or currentNode.weight is 15:
      currentNode.status = "unvisited"
      currentNode.weight = 0
      currentHTMLNode.className = "unvisited"

  })


Board.prototype.clearWeights = def():
  Object.keys(this.nodes).forEach(id => {
    let currentNode = this.nodes[id]
    let currentHTMLNode = document.getElementById(id)
    if currentNode.weight is 15:
      currentNode.status = "unvisited"
      currentNode.weight = 0
      currentHTMLNode.className = "unvisited"

  })


Board.prototype.clearNodeStatuses = def():
  Object.keys(this.nodes).forEach(id => {
    let currentNode = this.nodes[id]
    currentNode.previousNode = None
    currentNode.distance = Infinity
    currentNode.totalDistance = Infinity
    currentNode.heuristicDistance = None
    currentNode.storedDirection = currentNode.direction
    currentNode.direction = None
    let relevantStatuses = ["wall", "start", "target", "object"]
    if not relevantStatuses.includes(currentNode.status):
      currentNode.status = "unvisited"

  })


Board.prototype.instantAlgorithm = def():
  let weightedAlgorithms = ["dijkstra", "CLA", "greedy"]
  let unweightedAlgorithms = ["dfs", "bfs"]
  let success
  if this.currentAlgorithm is "bidirectional":
    if not this.numberOfObjects:
      success = bidirectional(this.nodes, this.start, this.target, this.nodesToAnimate, this.boardArray, this.currentAlgorithm, this.currentHeuristic, this)
      launchInstantAnimations(this, success, "weighted")
    else:
      this.isObject = True

    this.algoDone = True
  elif this.currentAlgorithm is "astar":
    if not this.numberOfObjects:
      success = weightedSearchAlgorithm(this.nodes, this.start, this.target, this.nodesToAnimate, this.boardArray, this.currentAlgorithm, this.currentHeuristic)
      launchInstantAnimations(this, success, "weighted")
    else:
      this.isObject = True
      success = weightedSearchAlgorithm(this.nodes, this.start, this.object, this.objectNodesToAnimate, this.boardArray, this.currentAlgorithm, this.currentHeuristic)
      launchInstantAnimations(this, success, "weighted", "object", this.currentAlgorithm)

    this.algoDone = True

  if weightedAlgorithms.includes(this.currentAlgorithm):
    if not this.numberOfObjects:
      success = weightedSearchAlgorithm(this.nodes, this.start, this.target, this.nodesToAnimate, this.boardArray, this.currentAlgorithm, this.currentHeuristic)
      launchInstantAnimations(this, success, "weighted")
    else:
      this.isObject = True
      success = weightedSearchAlgorithm(this.nodes, this.start, this.object, this.objectNodesToAnimate, this.boardArray, this.currentAlgorithm, this.currentHeuristic)
      launchInstantAnimations(this, success, "weighted", "object", this.currentAlgorithm, this.currentHeuristic)

    this.algoDone = True
  elif unweightedAlgorithms.includes(this.currentAlgorithm):
    if not this.numberOfObjects:
      success = unweightedSearchAlgorithm(this.nodes, this.start, this.target, this.nodesToAnimate, this.boardArray, this.currentAlgorithm)
      launchInstantAnimations(this, success, "unweighted")
    else:
      this.isObject = True
      success = unweightedSearchAlgorithm(this.nodes, this.start, this.object, this.objectNodesToAnimate, this.boardArray, this.currentAlgorithm)
      launchInstantAnimations(this, success, "unweighted", "object", this.currentAlgorithm)

    this.algoDone = True



Board.prototype.redoAlgorithm = def():
  this.clearPath()
  this.instantAlgorithm()


Board.prototype.reset = def(objectNotTransparent):
  this.nodes[this.start].status = "start"
  document.getElementById(this.start).className = "startTransparent"
  this.nodes[this.target].status = "target"
  if this.object:
    this.nodes[this.object].status = "object"
    if objectNotTransparent:
      document.getElementById(this.object).className = "visitedObjectNode"
    else:
      document.getElementById(this.object).className = "objectTransparent"




Board.prototype.resetHTMLNodes = def():
  let start = document.getElementById(this.start)
  let target = document.getElementById(this.target)
  start.className = "start"
  target.className = "target"


Board.prototype.changeStartNodeImages = def():
  let unweighted = ["bfs", "dfs"]
  let strikethrough = ["bfs", "dfs"]
  let guaranteed = ["dijkstra", "astar"]
  let name = ""
  if this.currentAlgorithm is "bfs":
    name = "Breath-first Search"
  elif this.currentAlgorithm is "dfs":
    name = "Depth-first Search"
  elif this.currentAlgorithm is "dijkstra":
    name = "Dijkstra's Algorithm"
  elif this.currentAlgorithm is "astar":
    name = "A* Search"
  elif this.currentAlgorithm is "greedy":
    name = "Greedy Best-first Search"
  elif this.currentAlgorithm is "CLA" and this.currentHeuristic is not "extraPoweredManhattanDistance":
    name = "Swarm Algorithm"
  elif this.currentAlgorithm is "CLA" and this.currentHeuristic is "extraPoweredManhattanDistance":
    name = "Convergent Swarm Algorithm"
  elif this.currentAlgorithm is "bidirectional":
    name = "Bidirectional Swarm Algorithm"

  if unweighted.includes(this.currentAlgorithm):
    if this.currentAlgorithm is "dfs":
      document.getElementById("algorithmDescriptor").innerHTML = `${name} is <i><b>unweighted</b></i> and <i><b>does not guarantee</b></i> the shortest pathnot `
    else:
      document.getElementById("algorithmDescriptor").innerHTML = `${name} is <i><b>unweighted</b></i> and <i><b>guarantees</b></i> the shortest pathnot `

    document.getElementById("weightLegend").className = "strikethrough"
    for let i = 0; i < 14; i++:
      let j = i.toString()
      let backgroundImage = document.styleSheets["1"].rules[j].style.backgroundImage
      document.styleSheets["1"].rules[j].style.backgroundImage = backgroundImage.replace("triangle", "spaceship")

  else:
    if this.currentAlgorithm is "greedy"or this.currentAlgorithm is "CLA":
      document.getElementById("algorithmDescriptor").innerHTML = `${name} is <i><b>weighted</b></i> and <i><b>does not guarantee</b></i> the shortest pathnot `

    document.getElementById("weightLegend").className = ""
    for let i = 0; i < 14; i++:
      let j = i.toString()
      let backgroundImage = document.styleSheets["1"].rules[j].style.backgroundImage
      document.styleSheets["1"].rules[j].style.backgroundImage = backgroundImage.replace("spaceship", "triangle")


  if this.currentAlgorithm is "bidirectional":

    document.getElementById("algorithmDescriptor").innerHTML = `${name} is <i><b>weighted</b></i> and <i><b>does not guarantee</b></i> the shortest pathnot `
    document.getElementById("bombLegend").className = "strikethrough"
    document.getElementById("startButtonAddObject").className = "navbar-inverse navbar-nav disabledA"
  else:
    document.getElementById("bombLegend").className = ""
    document.getElementById("startButtonAddObject").className = "navbar-inverse navbar-nav"

  if guaranteed.includes(this.currentAlgorithm):
    document.getElementById("algorithmDescriptor").innerHTML = `${name} is <i><b>weighted</b></i> and <i><b>guarantees</b></i> the shortest pathnot `



let counter = 1
Board.prototype.toggleTutorialButtons = def():

  document.getElementById("skipButton").onclick = () => {
    document.getElementById("tutorial").style.display = "none"
    this.toggleButtons()
  }

  if document.getElementById("nextButton"):
    document.getElementById("nextButton").onclick = () => {
      if counter < 9) counter++
      nextPreviousClick()
      this.toggleTutorialButtons()
    }
  }

  document.getElementById("previousButton").onclick = () => {
    if counter > 1) counter--
    nextPreviousClick()
    this.toggleTutorialButtons()
  }

  let board = this
  def nextPreviousClick(:
    if counter is 1:
      document.getElementById("tutorial").innerHTML = `<h3>Welcome to Pathfinding Visualizernot </h3><h6>This short tutorial will walk you through all of the features of this application.</h6><p>If you want to dive right in, feel free to press the "Skip Tutorial" button below. Otherwise, press "Next"not </p><div id="tutorialCounter">1/9</div><img id="mainTutorialImage" src="public/styling/c_icon.png"><button id="nextButton" class="btn btn-default navbar-btn" type="button">Next</button><button id="previousButton" class="btn btn-default navbar-btn" type="button">Previous</button><button id="skipButton" class="btn btn-default navbar-btn" type="button">Skip Tutorial</button>`
    elif counter is 2:
      document.getElementById("tutorial").innerHTML = `<h3>What is a pathfinding algorithm?</h3><h6>At its core, a pathfinding algorithm seeks to find the shortest path between two points. This application visualizes various pathfinding algorithms in action, and morenot </h6><p>All of the algorithms on this application are adapted for a 2D grid, where 90 degree turns have a "cost" of 1 and movements from a node to another have a "cost" of 1.</p><div id="tutorialCounter">${counter}/9</div><img id="mainTutorialImage" src="public/styling/path.png"><button id="nextButton" class="btn btn-default navbar-btn" type="button">Next</button><button id="previousButton" class="btn btn-default navbar-btn" type="button">Previous</button><button id="skipButton" class="btn btn-default navbar-btn" type="button">Skip Tutorial</button>`
    elif counter is 3:
      document.getElementById("tutorial").innerHTML = `<h3>Picking an algorithm</h3><h6>Choose an algorithm from the "Algorithms" drop-down menu.</h6><p>Note that some algorithms are <i><b>unweighted</b></i>, while others are <i><b>weighted</b></i>. Unweighted algorithms do not take turnsor weight nodes into account, whereas weighted ones do. Additionally, not all algorithms guarantee the shortest path. </p><img id="secondTutorialImage" src="public/styling/algorithms.png"><div id="tutorialCounter">${counter}/9</div><button id="nextButton" class="btn btn-default navbar-btn" type="button">Next</button><button id="previousButton" class="btn btn-default navbar-btn" type="button">Previous</button><button id="skipButton" class="btn btn-default navbar-btn" type="button">Skip Tutorial</button>`
    elif counter is 4:
      document.getElementById("tutorial").innerHTML = `<h3>Meet the algorithms</h3><h6>Not all algorithms are created equal.</h6><ul><li><b>Dijkstra's Algorithm</b> (weighted): the father of pathfinding algorithms; guarantees the shortest path</li><li><b>A* Search</b> (weighted): arguably the best pathfinding algorithm; uses heuristics to guarantee the shortest path much faster than Dijkstra's Algorithm</li><li><b>Greedy Best-first Search</b> (weighted): a faster, more heuristic-heavy version of A*; does not guarantee the shortest path</li><li><b>Swarm Algorithm</b> (weighted): a mixture of Dijkstra's Algorithm and A*; does not guarantee the shortest-path</li><li><b>Convergent Swarm Algorithm</b> (weighted): the faster, more heuristic-heavy version of Swarm; does not guarantee the shortest path</li><li><b>Bidirectional Swarm Algorithm</b> (weighted): Swarm from both sides; does not guarantee the shortest path</li><li><b>Breath-first Search</b> (unweighted): a great algorithm; guarantees the shortest path</li><li><b>Depth-first Search</b> (unweighted): a very bad algorithm for pathfinding; does not guarantee the shortest path</li></ul><div id="tutorialCounter">${counter}/9</div><button id="nextButton" class="btn btn-default navbar-btn" type="button">Next</button><button id="previousButton" class="btn btn-default navbar-btn" type="button">Previous</button><button id="skipButton" class="btn btn-default navbar-btn" type="button">Skip Tutorial</button>`
    } else if (counter === 5) {
      document.getElementById("tutorial").innerHTML = `<h3>Adding walls and weights</h3><h6>Click on the grid to add a wall. Click on the grid while pressing W to add a weight. Generate mazes and patterns from the "Mazes & Patterns" drop-down menu.</h6><p>Walls are impenetrable, meaning that a path cannot cross through them. Weights, however, are not impassable. They are simply more "costly" to move through. In this application, moving through a weight node has a "cost" of 15.</p><img id="secondTutorialImage" src="public/styling/walls.gif"><div id="tutorialCounter">${counter}/9</div><button id="nextButton" class="btn btn-default navbar-btn" type="button">Next</button><button id="previousButton" class="btn btn-default navbar-btn" type="button">Previous</button><button id="skipButton" class="btn btn-default navbar-btn" type="button">Skip Tutorial</button>`
    } else if (counter === 6) {
      document.getElementById("tutorial").innerHTML = `<h3>Adding a bomb</h3><h6>Click the "Add Bomb" button.</h6><p>Adding a bomb will change the course of the chosen algorithm. In other words, the algorithm will first look for the bomb (in an effort to diffuse it) and will then look for the target node. Note that the Bidirectional Swarm Algorithm does not support adding a bomb.</p><img id="secondTutorialImage" src="public/styling/bomb.png"><div id="tutorialCounter">${counter}/9</div><button id="nextButton" class="btn btn-default navbar-btn" type="button">Next</button><button id="previousButton" class="btn btn-default navbar-btn" type="button">Previous</button><button id="skipButton" class="btn btn-default navbar-btn" type="button">Skip Tutorial</button>`
    } else if (counter === 7) {
      document.getElementById("tutorial").innerHTML = `<h3>Dragging nodes</h3><h6>Click and drag the start, bomb, and target nodes to move them.</h6><p>Note that you can drag nodes even after an algorithm has finished running. This will allow you to instantly see different paths.</p><img src="public/styling/dragging.gif"><div id="tutorialCounter">${counter}/9</div><button id="nextButton" class="btn btn-default navbar-btn" type="button">Next</button><button id="previousButton" class="btn btn-default navbar-btn" type="button">Previous</button><button id="skipButton" class="btn btn-default navbar-btn" type="button">Skip Tutorial</button>`
    } else if (counter === 8) {
      document.getElementById("tutorial").innerHTML = `<h3>Visualizing and more</h3><h6>Use the navbar buttons to visualize algorithms and to do other stuff!</h6><p>You can clear the current path, clear walls and weights, clear the entire board, and adjust the visualization speed, all from the navbar. If you want to access this tutorial again, click on "Pathfinding Visualizer" in the top left corner of your screen.</p><img id="secondTutorialImage" src="public/styling/navbar.png"><div id="tutorialCounter">${counter}/9</div><button id="nextButton" class="btn btn-default navbar-btn" type="button">Next</button><button id="previousButton" class="btn btn-default navbar-btn" type="button">Previous</button><button id="skipButton" class="btn btn-default navbar-btn" type="button">Skip Tutorial</button>`
    } else if (counter === 9) {
      document.getElementById("tutorial").innerHTML = `<h3>Enjoy!</h3><h6>I hope you have just as much fun playing around with this visualization tool as I had building it!</h6><p>If you want to see the source code for this application, check out my <a href="https://github.com/clementmihailescu/Pathfinding-Visualizer">github</a>.</p><div id="tutorialCounter">${counter}/9</div><button id="finishButton" class="btn btn-default navbar-btn" type="button">Finish</button><button id="previousButton" class="btn btn-default navbar-btn" type="button">Previous</button><button id="skipButton" class="btn btn-default navbar-btn" type="button">Skip Tutorial</button>`
      document.getElementById("finishButton").onclick = () => {
        document.getElementById("tutorial").style.display = "none";
        board.toggleButtons();
      }
    }
  }

};

Board.prototype.toggleButtons = function() {
  document.getElementById("refreshButton").onclick = () => {
    window.location.reload(true);
  }

  if (!this.buttonsOn) {
    this.buttonsOn = true;

    document.getElementById("startButtonStart").onclick = () => {
      if (!this.currentAlgorithm) {
        document.getElementById("startButtonStart").innerHTML = '<button class="btn btn-default navbar-btn" type="button">Pick an Algorithmnot </button>'
      } else {
        this.clearPath("clickedButton");
        this.toggleButtons();
        let weightedAlgorithms = ["dijkstra", "CLA", "CLA", "greedy"];
        let unweightedAlgorithms = ["dfs", "bfs"];
        let success;
        if (this.currentAlgorithm === "bidirectional") {
          if (!this.numberOfObjects) {
            success = bidirectional(this.nodes, this.start, this.target, this.nodesToAnimate, this.boardArray, this.currentAlgorithm, this.currentHeuristic, this);
            launchAnimations(this, success, "weighted");
          } else {
            this.isObject = true;
            success = bidirectional(this.nodes, this.start, this.object, this.nodesToAnimate, this.boardArray, this.currentAlgorithm, this.currentHeuristic, this);
            launchAnimations(this, success, "weighted");
          }
          this.algoDone = true;
        } else if (this.currentAlgorithm === "astar") {
          if (!this.numberOfObjects) {
            success = weightedSearchAlgorithm(this.nodes, this.start, this.target, this.nodesToAnimate, this.boardArray, this.currentAlgorithm, this.currentHeuristic);
            launchAnimations(this, success, "weighted");
          } else {
            this.isObject = true;
            success = weightedSearchAlgorithm(this.nodes, this.start, this.object, this.objectNodesToAnimate, this.boardArray, this.currentAlgorithm, this.currentHeuristic);
            launchAnimations(this, success, "weighted", "object", this.currentAlgorithm);
          }
          this.algoDone = true;
        } else if (weightedAlgorithms.includes(this.currentAlgorithm)) {
          if (!this.numberOfObjects) {
            success = weightedSearchAlgorithm(this.nodes, this.start, this.target, this.nodesToAnimate, this.boardArray, this.currentAlgorithm, this.currentHeuristic);
            launchAnimations(this, success, "weighted");
          } else {
            this.isObject = true;
            success = weightedSearchAlgorithm(this.nodes, this.start, this.object, this.objectNodesToAnimate, this.boardArray, this.currentAlgorithm, this.currentHeuristic);
            launchAnimations(this, success, "weighted", "object", this.currentAlgorithm, this.currentHeuristic);
          }
          this.algoDone = true;
        } else if (unweightedAlgorithms.includes(this.currentAlgorithm)) {
          if (!this.numberOfObjects) {
            success = unweightedSearchAlgorithm(this.nodes, this.start, this.target, this.nodesToAnimate, this.boardArray, this.currentAlgorithm);
            launchAnimations(this, success, "unweighted");
          } else {
            this.isObject = true;
            success = unweightedSearchAlgorithm(this.nodes, this.start, this.object, this.objectNodesToAnimate, this.boardArray, this.currentAlgorithm);
            launchAnimations(this, success, "unweighted", "object", this.currentAlgorithm);
          }
          this.algoDone = true;
        }
      }
    }

    document.getElementById("adjustFast").onclick = () => {
      this.speed = "fast";
      document.getElementById("adjustSpeed").innerHTML = 'Speed: Fast<span class="caret"></span>';
    }

    document.getElementById("adjustAverage").onclick = () => {
      this.speed = "average";
      document.getElementById("adjustSpeed").innerHTML = 'Speed: Average<span class="caret"></span>';
    }

    document.getElementById("adjustSlow").onclick = () => {
      this.speed = "slow";
      document.getElementById("adjustSpeed").innerHTML = 'Speed: Slow<span class="caret"></span>';
    }

    document.getElementById("startStairDemonstration").onclick = () => {
      this.clearWalls();
      this.clearPath("clickedButton");
      this.toggleButtons();
      stairDemonstration(this);
      mazeGenerationAnimations(this);
    }


    document.getElementById("startButtonBidirectional").onclick = () => {
      document.getElementById("startButtonStart").innerHTML = '<button id="actualStartButton" class="btn btn-default navbar-btn" type="button">Visualize Bidirectional Swarmnot </button>'
      this.currentAlgorithm = "bidirectional";
      this.currentHeuristic = "manhattanDistance";
      if (this.numberOfObjects) {
        let objectNodeId = this.object;
        document.getElementById("startButtonAddObject").innerHTML = '<a href="#">Add a Bomb</a></li>';
        document.getElementById(objectNodeId).className = "unvisited";
        this.object = null;
        this.numberOfObjects = 0;
        this.nodes[objectNodeId].status = "unvisited";
        this.isObject = false;
      }
      this.clearPath("clickedButton");
      this.changeStartNodeImages();
    }

    document.getElementById("startButtonDijkstra").onclick = () => {
      document.getElementById("startButtonStart").innerHTML = '<button id="actualStartButton" class="btn btn-default navbar-btn" type="button">Visualize Dijkstra\'snot </button>'
      this.currentAlgorithm = "dijkstra";
      this.changeStartNodeImages();
    }

    document.getElementById("startButtonAStar").onclick = () => {
      document.getElementById("startButtonStart").innerHTML = '<button id="actualStartButton" class="btn btn-default navbar-btn" type="button">Visualize Swarmnot </button>'
      this.currentAlgorithm = "CLA";
      this.currentHeuristic = "manhattanDistance"
      this.changeStartNodeImages();
    }

    document.getElementById("startButtonAStar2").onclick = () => {
      document.getElementById("startButtonStart").innerHTML = '<button id="actualStartButton" class="btn btn-default navbar-btn" type="button">Visualize A*not </button>'
      this.currentAlgorithm = "astar";
      this.currentHeuristic = "poweredManhattanDistance"
      this.changeStartNodeImages();
    }

    document.getElementById("startButtonAStar3").onclick = () => {
      document.getElementById("startButtonStart").innerHTML = '<button id="actualStartButton" class="btn btn-default navbar-btn" type="button">Visualize Convergent Swarmnot </button>'
      this.currentAlgorithm = "CLA";
      this.currentHeuristic = "extraPoweredManhattanDistance"
      this.changeStartNodeImages();
    }

    document.getElementById("startButtonGreedy").onclick = () => {
      document.getElementById("startButtonStart").innerHTML = '<button id="actualStartButton" class="btn btn-default navbar-btn" type="button">Visualize Greedynot </button>'
      this.currentAlgorithm = "greedy";
      this.changeStartNodeImages();
    }

    document.getElementById("startButtonBFS").onclick = () => {
      document.getElementById("startButtonStart").innerHTML = '<button id="actualStartButton" class="btn btn-default navbar-btn" type="button">Visualize BFSnot </button>'
      this.currentAlgorithm = "bfs";
      this.clearWeights();
      this.changeStartNodeImages();
    }

    document.getElementById("startButtonDFS").onclick = () => {
      document.getElementById("startButtonStart").innerHTML = '<button id="actualStartButton" class="btn btn-default navbar-btn" type="button">Visualize DFSnot </button>'
      this.currentAlgorithm = "dfs";
      this.clearWeights();
      this.changeStartNodeImages();
    }

    document.getElementById("startButtonCreateMazeOne").onclick = () => {
      this.clearWalls();
      this.clearPath("clickedButton");
      this.createMazeOne("wall");
    }

    document.getElementById("startButtonCreateMazeTwo").onclick = () => {
      this.clearWalls();
      this.clearPath("clickedButton");
      this.toggleButtons();
      recursiveDivisionMaze(this, 2, this.height - 3, 2, this.width - 3, "horizontal", false, "wall");
      mazeGenerationAnimations(this);
    }

    document.getElementById("startButtonCreateMazeWeights").onclick = () => {
      this.clearWalls();
      this.clearPath("clickedButton");
      this.createMazeOne("weight");
    }

    document.getElementById("startButtonClearBoard").onclick = () => {
      document.getElementById("startButtonAddObject").innerHTML = '<a href="#">Add Bomb</a></li>';



      let navbarHeight = document.getElementById("navbarDiv").clientHeight;
      let textHeight = document.getElementById("mainText").clientHeight + document.getElementById("algorithmDescriptor").clientHeight;
      let height = Math.floor((document.documentElement.clientHeight - navbarHeight - textHeight) / 28);
      let width = Math.floor(document.documentElement.clientWidth / 25);
      let start = Math.floor(height / 2).toString() + "-" + Math.floor(width / 4).toString();
      let target = Math.floor(height / 2).toString() + "-" + Math.floor(3 * width / 4).toString();

        Object.keys(this.nodes).forEach(id => {
          let currentNode = this.nodes[id];
          let currentHTMLNode = document.getElementById(id);
          if (id === start) {
            currentHTMLNode.className = "start";
            currentNode.status = "start";
          } else if (id === target) {
            currentHTMLNode.className = "target";
            currentNode.status = "target"
          } else {
            currentHTMLNode.className = "unvisited";
            currentNode.status = "unvisited";
          }
          currentNode.previousNode = null;
          currentNode.path = null;
          currentNode.direction = null;
          currentNode.storedDirection = null;
          currentNode.distance = Infinity;
          currentNode.totalDistance = Infinity;
          currentNode.heuristicDistance = null;
          currentNode.weight = 0;
          currentNode.relatesToObject = false;
          currentNode.overwriteObjectRelation = false;

        });
      this.start = start;
      this.target = target;
      this.object = null;
      this.nodesToAnimate = [];
      this.objectNodesToAnimate = [];
      this.shortestPathNodesToAnimate = [];
      this.objectShortestPathNodesToAnimate = [];
      this.wallsToAnimate = [];
      this.mouseDown = false;
      this.pressedNodeStatus = "normal";
      this.previouslyPressedNodeStatus = null;
      this.previouslySwitchedNode = null;
      this.previouslySwitchedNodeWeight = 0;
      this.keyDown = false;
      this.algoDone = false;
      this.numberOfObjects = 0;
      this.isObject = false;
    }

    document.getElementById("startButtonClearWalls").onclick = () => {
      this.clearWalls();
    }

    document.getElementById("startButtonClearPath").onclick = () => {
      this.clearPath("clickedButton");
    }

    document.getElementById("startButtonCreateMazeThree").onclick = () => {
      this.clearWalls();
      this.clearPath("clickedButton");
      this.toggleButtons();
      otherMaze(this, 2, this.height - 3, 2, this.width - 3, "vertical", false);
      mazeGenerationAnimations(this);
    }

    document.getElementById("startButtonCreateMazeFour").onclick = () => {
      this.clearWalls();
      this.clearPath("clickedButton");
      this.toggleButtons();
      otherOtherMaze(this, 2, this.height - 3, 2, this.width - 3, "horizontal", false);
      mazeGenerationAnimations(this);
    }

    document.getElementById("startButtonAddObject").onclick = () => {
      let innerHTML = document.getElementById("startButtonAddObject").innerHTML;
      if (this.currentAlgorithm !== "bidirectional") {
        if (innerHTML.includes("Add")) {
          let r = Math.floor(this.height / 2);
          let c = Math.floor(2 * this.width / 4);
          let objectNodeId = `${r}-${c}`;
          if (this.target === objectNodeId || this.start === objectNodeId || this.numberOfObjects === 1) {
            console.log("Failure to place object.");
          } else {
            document.getElementById("startButtonAddObject").innerHTML = '<a href="#">Remove Bomb</a></li>';
            this.clearPath("clickedButton");
            this.object = objectNodeId;
            this.numberOfObjects = 1;
            this.nodes[objectNodeId].status = "object";
            document.getElementById(objectNodeId).className = "object";
          }
        } else {
          let objectNodeId = this.object;
          document.getElementById("startButtonAddObject").innerHTML = '<a href="#">Add Bomb</a></li>';
          document.getElementById(objectNodeId).className = "unvisited";
          this.object = null;
          this.numberOfObjects = 0;
          this.nodes[objectNodeId].status = "unvisited";
          this.isObject = false;
          this.clearPath("clickedButton");
        }
      }

    }

    document.getElementById("startButtonClearPath").className = "navbar-inverse navbar-nav";
    document.getElementById("startButtonClearWalls").className = "navbar-inverse navbar-nav";
    document.getElementById("startButtonClearBoard").className = "navbar-inverse navbar-nav";
    if (this.currentAlgorithm !== "bidirectional") {
      document.getElementById("startButtonAddObject").className = "navbar-inverse navbar-nav";
    }
    document.getElementById("startButtonCreateMazeOne").className = "navbar-inverse navbar-nav";
    document.getElementById("startButtonCreateMazeTwo").className = "navbar-inverse navbar-nav";
    document.getElementById("startButtonCreateMazeThree").className = "navbar-inverse navbar-nav";
    document.getElementById("startButtonCreateMazeFour").className = "navbar-inverse navbar-nav";
    document.getElementById("startButtonCreateMazeWeights").className = "navbar-inverse navbar-nav";
    document.getElementById("startStairDemonstration").className = "navbar-inverse navbar-nav";
    document.getElementById("startButtonDFS").className = "navbar-inverse navbar-nav";
    document.getElementById("startButtonBFS").className = "navbar-inverse navbar-nav";
    document.getElementById("startButtonDijkstra").className = "navbar-inverse navbar-nav";
    document.getElementById("startButtonAStar").className = "navbar-inverse navbar-nav";
    document.getElementById("startButtonAStar2").className = "navbar-inverse navbar-nav";
    document.getElementById("startButtonAStar3").className = "navbar-inverse navbar-nav";
    document.getElementById("adjustFast").className = "navbar-inverse navbar-nav";
    document.getElementById("adjustAverage").className = "navbar-inverse navbar-nav";
    document.getElementById("adjustSlow").className = "navbar-inverse navbar-nav";
    document.getElementById("startButtonBidirectional").className = "navbar-inverse navbar-nav";
    document.getElementById("startButtonGreedy").className = "navbar-inverse navbar-nav";
    document.getElementById("actualStartButton").style.backgroundColor = "";

  } else {
    this.buttonsOn = false;
    document.getElementById("startButtonDFS").onclick = null;
    document.getElementById("startButtonBFS").onclick = null;
    document.getElementById("startButtonDijkstra").onclick = null;
    document.getElementById("startButtonAStar").onclick = null;
    document.getElementById("startButtonGreedy").onclick = null;
    document.getElementById("startButtonAddObject").onclick = null;
    document.getElementById("startButtonAStar2").onclick = null;
    document.getElementById("startButtonAStar3").onclick = null;
    document.getElementById("startButtonBidirectional").onclick = null;
    document.getElementById("startButtonCreateMazeOne").onclick = null;
    document.getElementById("startButtonCreateMazeTwo").onclick = null;
    document.getElementById("startButtonCreateMazeThree").onclick = null;
    document.getElementById("startButtonCreateMazeFour").onclick = null;
    document.getElementById("startButtonCreateMazeWeights").onclick = null;
    document.getElementById("startStairDemonstration").onclick = null;
    document.getElementById("startButtonClearPath").onclick = null;
    document.getElementById("startButtonClearWalls").onclick = null;
    document.getElementById("startButtonClearBoard").onclick = null;
    document.getElementById("startButtonStart").onclick = null;
    document.getElementById("adjustFast").onclick = null;
    document.getElementById("adjustAverage").onclick = null;
    document.getElementById("adjustSlow").onclick = null;

    document.getElementById("adjustFast").className = "navbar-inverse navbar-nav disabledA";
    document.getElementById("adjustAverage").className = "navbar-inverse navbar-nav disabledA";
    document.getElementById("adjustSlow").className = "navbar-inverse navbar-nav disabledA";
    document.getElementById("startButtonClearPath").className = "navbar-inverse navbar-nav disabledA";
    document.getElementById("startButtonClearWalls").className = "navbar-inverse navbar-nav disabledA";
    document.getElementById("startButtonClearBoard").className = "navbar-inverse navbar-nav disabledA";
    document.getElementById("startButtonAddObject").className = "navbar-inverse navbar-nav disabledA";
    document.getElementById("startButtonCreateMazeOne").className = "navbar-inverse navbar-nav disabledA";
    document.getElementById("startButtonCreateMazeTwo").className = "navbar-inverse navbar-nav disabledA";
    document.getElementById("startButtonCreateMazeThree").className = "navbar-inverse navbar-nav disabledA";
    document.getElementById("startButtonCreateMazeFour").className = "navbar-inverse navbar-nav disabledA";
    document.getElementById("startButtonCreateMazeWeights").className = "navbar-inverse navbar-nav disabledA";
    document.getElementById("startStairDemonstration").className = "navbar-inverse navbar-nav disabledA";
    document.getElementById("startButtonDFS").className = "navbar-inverse navbar-nav disabledA";
    document.getElementById("startButtonBFS").className = "navbar-inverse navbar-nav disabledA";
    document.getElementById("startButtonDijkstra").className = "navbar-inverse navbar-nav disabledA";
    document.getElementById("startButtonAStar").className = "navbar-inverse navbar-nav disabledA";
    document.getElementById("startButtonGreedy").className = "navbar-inverse navbar-nav disabledA";
    document.getElementById("startButtonAStar2").className = "navbar-inverse navbar-nav disabledA";
    document.getElementById("startButtonAStar3").className = "navbar-inverse navbar-nav disabledA";
    document.getElementById("startButtonBidirectional").className = "navbar-inverse navbar-nav disabledA";

    document.getElementById("actualStartButton").style.backgroundColor = "rgb(185, 15, 15)";
  }


}

let navbarHeight = $("#navbarDiv").height();
let textHeight = $("#mainText").height() + $("#algorithmDescriptor").height();
let height = Math.floor(($(document).height() - navbarHeight - textHeight) / 28);
let width = Math.floor($(document).width() / 25);
let newBoard = new Board(height, width)
newBoard.initialise();

window.onkeydown = (e) => {
  newBoard.keyDown = e.keyCode;
}

window.onkeyup = (e) => {
  newBoard.keyDown = false;
}

}