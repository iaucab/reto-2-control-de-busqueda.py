import sys

def bfs(matrix, row, col, value):

  if ((row > 0 and matrix[row-1][col] == -3) or 
      (col < len(matrix[0])-1 and matrix[row][col+1] == -3) or
      (row < len(matrix)-1 and matrix[row+1][col] == -3) or 
      (col > 0 and matrix[row][col-1] == -3)):
    return True

  # Update next
  if row > 0 and matrix[row-1][col] == 0:
    matrix[row-1][col] = value
  if col < len(matrix[0])-1 and matrix[row][col+1] == 0:
    matrix[row][col+1] = value
  if row < len(matrix)-1 and matrix[row+1][col] == 0:
    matrix[row+1][col] = value
  if col > 0 and matrix[row][col-1] == 0:
    matrix[row][col-1] = value

  return False

def dfs(matrix, row, col, deep):

  if matrix[row][col] == -3:
    return deep

  elif matrix[row][col] == -2 or matrix[row][col] == 0:
    if matrix[row][col] == 0:
      matrix[row][col] = deep

    # Go deep
    if row > 0:
      result = dfs(matrix, row-1, col, deep+1)
      if result > 0:
        return result

    if col < len(matrix[0])-1:
      result = dfs(matrix, row, col+1, deep+1)
      if result > 0:
        return result

    if row < len(matrix)-1:
      result = dfs(matrix, row+1, col, deep+1)
      if result > 0:
        return result

    if col > 0:
      result = dfs(matrix, row, col-1, deep+1)
      if result > 0:
        return result

  return 0
  

def getNextCells(matrix, value):
  nextCells = []
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] == value:
        nextCells.append([i, j])
  
  # if len(nextCells) == 0:
  #  print("Error: 404. Cell not found")
  #  sys.exit()

  return nextCells

def drawReturnPath(matrix, row, col, deep):
  if deep > 0:

    if row > 0 and matrix[row-1][col] == deep:
      matrix[row-1][col] = -4
      drawReturnPath(matrix, row-1, col, deep-1)

    if col < len(matrix[0])-1 and matrix[row][col+1] == deep:
      matrix[row][col+1] = -4
      drawReturnPath(matrix, row, col+1, deep-1)
    
    if row < len(matrix)-1 and matrix[row+1][col] == deep:
      matrix[row+1][col] = -4
      drawReturnPath(matrix, row+1, col, deep-1)
    
    if col > 0 and matrix[row][col-1] == deep:
      matrix[row][col-1] = -4
      drawReturnPath(matrix, row, col-1, deep-1)