def getDistance(nodeOne, nodeTwo):
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




module.exports = getDistance