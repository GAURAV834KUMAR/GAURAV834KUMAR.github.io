def mazeGenerationAnimations(board):
  let nodes = board.wallsToAnimate.slice(0)
  let speed = board.speed is "fast" ?
    5 : board.speed is "average" ?
      25 : 75
  def timeout(index):
    setTimeout(def ():
        if index is nodes.length){
          board.wallsToAnimate = []
          board.toggleButtons()
          return
        }
        nodes[index].className = board.nodes[nodes[index].id].weight is 15 ? "unvisited weight" : "wall"
        timeout(index + 1)
    }, speed)
  }

  timeout(0)
}

module.exports = mazeGenerationAnimations
ns