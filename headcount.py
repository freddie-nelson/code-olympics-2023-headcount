def find_neighbours(layout, row, col):
  neighbours = []

  for i in range(row-1, row+2):
    for j in range(col-1, col+2):
      if i < 0 or j < 0:
        continue

      if i >= len(layout) or j >= len(layout[i]):
        continue

      if i == row and j == col:
        continue

      # don't include diagonals
      if i == row-1 and j == col-1:
        continue
      if i == row-1 and j == col+1:
        continue
      if i == row+1 and j == col-1:
        continue
      if i == row+1 and j == col+1:
        continue

      neighbours.append((i, j))
  
  return neighbours

def find_team(layout, row, col, counted):
  counted[(row, col)] = 1
  neighbours = find_neighbours(layout, row, col)
  # print(neighbours, row, col)

  size = 1

  for neighbour in neighbours:
    if neighbour in counted:
      continue

    if layout[neighbour[0]][neighbour[1]] == 1:
      counted[neighbour] = True
      size += find_team(layout, neighbour[0], neighbour[1], counted)

  return size

def headcount(layout):
  counted = {}
  teams = []

  for row in range(len(layout)):
    for col in range(len(layout[row])):
      if (row, col) in counted:
        continue

      if layout[row][col] == 1:
        team = find_team(layout, row, col, counted)
        teams.append(team)
  
  num_of_teams = len(teams)
  headcount = sum(teams)

  return teams, num_of_teams, headcount
      

layout = [
  [1,1,0,0,0,0,1,1],
  [1,1,0,1,1,0,1,1],
  [0,0,0,1,1,0,0,0],
  [1,1,0,1,1,0,1,1],
  [1,1,0,0,0,0,1,1]
]

teams, num_of_teams, headcount = headcount(layout)
print(f"{num_of_teams} teams of {teams} totaling {headcount}")