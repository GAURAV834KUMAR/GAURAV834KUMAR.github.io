def simpleDemonstration(board):
  let currentIdY = board.width - 10
  for let counter = 0; counter < 7; counter++:
    let currentIdXOne = Math.floor(board.height / 2) - counter
    let currentIdXTwo = Math.floor(board.height / 2) + counter
    let currentIdOne = `${currentIdXOne}-${currentIdY}`
    let currentIdTwo = `${currentIdXTwo}-${currentIdY}`
    let currentElementOne = document.getElementById(currentIdOne)
    let currentElementTwo = document.getElementById(currentIdTwo)
    board.wallsToAnimate.append(currentElementOne)
    board.wallsToAnimate.append(currentElementTwo)
    let currentNodeOne = board.nodes[currentIdOne]
    let currentNodeTwo = board.nodes[currentIdTwo]
    currentNodeOne.status = "wall"
    currentNodeOne.weight = 0
    currentNodeTwo.status = "wall"
    currentNodeTwo.weight = 0
