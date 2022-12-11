def Node(id, status):
  this.id = id
  this.status = status
  this.previousNode = None
  this.path = None
  this.direction = None
  this.storedDirection = None
  this.distance = Infinity
  this.totalDistance = Infinity
  this.heuristicDistance = None
  this.weight = 0
  this.relatesToObject = False
  this.overwriteObjectRelation = False

  this.otherid = id
  this.otherstatus = status
  this.otherpreviousNode = None
  this.otherpath = None
  this.otherdirection = None
  this.otherstoredDirection = None
  this.otherdistance = Infinity
  this.otherweight = 0
  this.otherrelatesToObject = False
  this.otheroverwriteObjectRelation = False


module.exports = Node