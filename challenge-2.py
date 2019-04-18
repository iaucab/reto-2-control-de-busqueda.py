from functions.printers import printTable
from functions.creators import getDefaultTable, createTable, insertAtPosition
from functions.searchers import bfs, dfs, getNextCells, drawReturnPath

# OPTIONS
SHOW_TABLE = 1
RESTORE_TABLE = 2
CREATE_TABLE = 3
BFS = 4
DFS = 5

matrix = getDefaultTable()

print("Challenge 2 |AI UCAB|", end="\n\n")

userOption = -1
while userOption:
  print("1.- Show table")
  print("2.- Restore default table")
  print("3.- Create table")
  print("4.- BFS")
  print("5.- DFS")
  print("0.- Exit")

  userOption = int(input("Select one option: "))

  # Show table
  if userOption == SHOW_TABLE:
    printTable(matrix)

  # Restore table
  elif userOption == RESTORE_TABLE:
    matrix = getDefaultTable()

  # Create table
  elif userOption == CREATE_TABLE:
    dimension = int(input("Matrix dimension: "))
    matrix = createTable(dimension)
    
    printTable(matrix)
    if not insertAtPosition(matrix, -2, "Start: "):
      matrix = getDefaultTable()
      continue

    printTable(matrix)
    if not insertAtPosition(matrix, -3, "End: "):
      matrix = getDefaultTable()
      continue

    printTable(matrix)
    while insertAtPosition(matrix, -1, "Block: "):
      printTable(matrix)
      print("Press Enter to finish")
  
  # BFS
  elif userOption == BFS:
    wasFound = False
    deep = 0

    # Start with cell == -2
    cells = getNextCells(matrix, -2)
    
    while not wasFound:
      deep += 1
      
      for cell in cells:
        wasFound = bfs(matrix, cell[0], cell[1], deep)
        if wasFound:
          break
      
      if not wasFound:
        cells = getNextCells(matrix, deep)

      # No more cells to search
      if len(cells) == 0:
        break

    print() # space

    if wasFound:
      print("Congratulations!!!")
      print("Deep: {:d}".format(deep))

      # End with cell == -3      
      finalCells = getNextCells(matrix, -3)
      for cell in finalCells:
        drawReturnPath(matrix, cell[0], cell[1], deep-1)
    else:
      print("Can not solve :(")

  # DFS
  elif userOption == DFS:
    # Start with cell == -2
    cells = getNextCells(matrix, -2)

    print() # space

    if len(cells) > 0:
      for start in cells:
        deep = dfs(matrix, start[0], start[1], 0)
        if deep > 0:
          print("Congratulations!!!")
          print("Deep: {:d}".format(deep))
          
          finalCells = getNextCells(matrix, -3)
          for cell in finalCells:
            drawReturnPath(matrix, cell[0], cell[1], deep-1)
          
          break
        else:
          print("Can not solve :(")

  if userOption == BFS or userOption == DFS:
    print("Select option 1 to see the table", end="\n\n")
  