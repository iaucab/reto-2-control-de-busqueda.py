# Colors
RED = "0;31;40"
GREEN = "0;32;40"
YELLOW = "0;33;40"
BLUE = "0;34;40"

def getStringWithColor(string, color):
  return '\x1b[{c}m{s}\x1b[0m'.format(s=string, c=color)

def printValues(matrix):
  for row in matrix:
    for cell in row:
      print(cell, end=" ")
    print()

def printTable(matrix):
  # Print col index
  for i in range(len(matrix[0])):
    if i == 0:
      print(getStringWithColor('r\\c', BLUE), end="|")
    print(getStringWithColor('{:3d}'.format(i), BLUE), end="|")
  print()

  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      # Print row index
      if j == 0:
        print(getStringWithColor('{:3d}'.format(i), BLUE), end="|")

      # Print blocks
      if matrix[i][j] == -1:
        print("|||", end="|")
        continue
      
      # Print start
      if matrix[i][j] == -2:
        print(getStringWithColor(" O ", GREEN), end="|")
        continue
      
      # Print finish
      if matrix[i][j] == -3:
        print(getStringWithColor(" X ", RED), end="|")
        continue

      # Print path
      if matrix[i][j] == -4:
        print(getStringWithColor(" - ", YELLOW), end="|")
        continue
      
      # Print value with spaces
      print('{:3d}'.format(matrix[i][j]), end="|")
    print()
  print()

