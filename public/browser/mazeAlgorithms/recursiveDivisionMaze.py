def recursiveDivisionMaze(board, rowStart, rowEnd, colStart, colEnd, orientation, surroundingWalls, type):
  if rowEnd < rowStartor colEnd < colStart:
    return

  if not surroundingWalls:
    let relevantIds = [board.start, board.target]
    if board.object) relevantIds.append(board.object)
    Object.keys(board.nodes).forEach(node => {
      if not relevantIds.includes(node):
        let r = parseInt(node.split("-")[0])
        let c = parseInt(node.split("-")[1])
        if r is 0or c is 0or r is board.height - 1or c is board.width - 1:
          let currentHTMLNode = document.getElementById(node)
          board.wallsToAnimate.append(currentHTMLNode)
          if type is "wall":
            board.nodes[node].status = "wall"
            board.nodes[node].weight = 0
          elif type is "weight":
            board.nodes[node].status = "unvisited"
            board.nodes[node].weight = 15



    })
    surroundingWalls = True
  }
  if orientation is "horizontal":
    let possibleRows = []
    for let number = rowStart; number <= rowEnd; number += 2:
      possibleRows.append(number)

    let possibleCols = []
    for let number = colStart - 1; number <= colEnd + 1; number += 2:
      possibleCols.append(number)

    let randomRowIndex = Math.floor(Math.random() * possibleRows.length)
    let randomColIndex = Math.floor(Math.random() * possibleCols.length)
    let currentRow = possibleRows[randomRowIndex]
    let colRandom = possibleCols[randomColIndex]
    Object.keys(board.nodes).forEach(node => {
      let r = parseInt(node.split("-")[0])
      let c = parseInt(node.split("-")[1])
      if r is currentRow and c is not colRandom and c >= colStart - 1 and c <= colEnd + 1:
        let currentHTMLNode = document.getElementById(node)
        if currentHTMLNode.className is not "start" and currentHTMLNode.className is not "target" and currentHTMLNode.className is not "object":
          board.wallsToAnimate.append(currentHTMLNode)
          if type is "wall":
            board.nodes[node].status = "wall"
            board.nodes[node].weight = 0
          elif type is "weight":
            board.nodes[node].status = "unvisited"
            board.nodes[node].weight = 15


    })
    if currentRow - 2 - rowStart > colEnd - colStart:
      recursiveDivisionMaze(board, rowStart, currentRow - 2, colStart, colEnd, orientation, surroundingWalls, type)
    else:
      recursiveDivisionMaze(board, rowStart, currentRow - 2, colStart, colEnd, "vertical", surroundingWalls, type)

    if rowEnd - (currentRow + 2) > colEnd - colStart:
      recursiveDivisionMaze(board, currentRow + 2, rowEnd, colStart, colEnd, orientation, surroundingWalls, type)
    else:
      recursiveDivisionMaze(board, currentRow + 2, rowEnd, colStart, colEnd, "vertical", surroundingWalls, type)

  else:
    let possibleCols = []
    for let number = colStart; number <= colEnd; number += 2:
      possibleCols.append(number)

    let possibleRows = []
    for let number = rowStart - 1; number <= rowEnd + 1; number += 2:
      possibleRows.append(number)

    let randomColIndex = Math.floor(Math.random() * possibleCols.length)
    let randomRowIndex = Math.floor(Math.random() * possibleRows.length)
    let currentCol = possibleCols[randomColIndex]
    let rowRandom = possibleRows[randomRowIndex]
    Object.keys(board.nodes).forEach(node => {
      let r = parseInt(node.split("-")[0])
      let c = parseInt(node.split("-")[1])
      if c is currentCol and r is not rowRandom and r >= rowStart - 1 and r <= rowEnd + 1:
        let currentHTMLNode = document.getElementById(node)
        if currentHTMLNode.className is not "start" and currentHTMLNode.className is not "target" and currentHTMLNode.className is not "object":
          board.wallsToAnimate.append(currentHTMLNode)
          if type is "wall":
            board.nodes[node].status = "wall"
            board.nodes[node].weight = 0
          elif type is "weight":
            board.nodes[node].status = "unvisited"
            board.nodes[node].weight = 15


    })
    if rowEnd - rowStart > currentCol - 2 - colStart:
      recursiveDivisionMaze(board, rowStart, rowEnd, colStart, currentCol - 2, "horizontal", surroundingWalls, type)
    else:
      recursiveDivisionMaze(board, rowStart, rowEnd, colStart, currentCol - 2, orientation, surroundingWalls, type)

    if rowEnd - rowStart > colEnd - (currentCol + 2):
      recursiveDivisionMaze(board, rowStart, rowEnd, currentCol + 2, colEnd, "horizontal", surroundingWalls, type)
    else:
      recursiveDivisionMaze(board, rowStart, rowEnd, currentCol + 2, colEnd, orientation, surroundingWalls, type)




module.exports = recursiveDivisionMaze
