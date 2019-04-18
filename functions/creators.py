def createTable(n):
  return [[0] * n for i in range(n)]
  
def insertAtPosition(matrix, blockType, str):
  uInput = input(str)

  # Exit
  if uInput == '':
    return False
  
  position = uInput.split(' ')
  
  # Validations
  if len(position) != 2:
    print("Error, you should enter 2 numbers. Ex: '26 18'")
    return insertAtPosition(matrix, blockType, 'Try again:')

  position[0] = int(position[0])
  position[1] = int(position[1])
  
  if (position[0] < 0 or position[0] > len(matrix)-1 or
      position[1] < 0 or position[1] > len(matrix[0])-1):
    print("Error, position out of range")
    return insertAtPosition(matrix, blockType, 'Try again:')

  if matrix[position[0]][position[1]] != 0:
    print("Error, this cell is not empty")
    return insertAtPosition(matrix, blockType, 'Try again:')

  # Insert new cell
  matrix[position[0]][position[1]] = blockType

  return True


def getDefaultTable():
  return [
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-2,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1],
    [-1,0,0,-1,0,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,0,-1,0,-1],
    [-1,0,-1,-1,0,-1,0,0,0,-1,0,0,0,0,0,-1,0,0,0,-1],
    [-1,0,-1,0,0,-1,0,0,0,-1,0,-1,-1,-1,-1,-1,0,-1,0,-1],
    [-1,0,-1,0,-1,-1,0,0,0,-1,0,0,0,0,0,0,0,0,0,-1],
    [-1,0,-1,-3,-1,0,0,0,-1,-1,0,-1,-1,-1,-1,-1,0,-1,0,-1],
    [-1,0,-1,-1,-1,0,0,0,-1,0,0,-1,0,0,0,-1,0,0,0,-1],
    [-1,0,0,0,0,0,0,0,-1,-1,-1,-1,0,0,0,-1,0,-1,0,-1],
    [-1,0,0,0,0,0,0,0,0,0,-1,-1,0,0,-1,-1,0,0,0,-1],
    [-1,0,-1,-1,-1,-1,-1,0,0,0,-1,-1,0,0,-1,0,0,-1,0,-1],
    [-1,0,-1,0,0,0,-1,0,0,0,-1,-1,0,0,0,0,0,0,0,-1],
    [-1,0,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,0,0,0,-1,0,-1,0,-1],
    [-1,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,0,0,0,-1],
    [-1,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,-1,0,-1],
    [-1,0,-1,-1,0,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,0,0,0,0,-1],
    [-1,0,-1,-1,0,-1,-1,0,0,0,0,-1,-1,-1,-1,0,0,-1,0,-1],
    [-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,0,0,0,-1],
    [-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,-1,0,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
  ]