import sys
from collections import namedtuple

Cube = namedtuple('Cube', 'x y z w')

def read_initial_state(input):
  active_set = set()
  with open(input, 'r') as f:
    for i, line in enumerate(f):
      for j, c in enumerate(line[:-1]):
        if c == '#':
          active_set.add(Cube(i,j,0,0))
  return active_set

def neighbour_set(cube):
  neighbours = set()
  for i in range(cube.x-1, cube.x+2):
    for j in range(cube.y-1, cube.y+2):
      for k in range(cube.z-1, cube.z+2):
        for m in range(cube.w-1, cube.w+2):
          # print(Cube(i,j,k,m))
          if Cube(i,j,k,m) == cube:
            continue
          else: 
            neighbours.add(Cube(i,j,k,m))
  return neighbours

def next_state(active_set):
  next_state = set()
  visited = set()
  for a in active_set:
    # Define the neighbour set
    neighbours = neighbour_set(a)
    # Determine which neighbours are active
    active_neighbours = neighbours.intersection(active_set)
    
    # If there are 2 or 3 active neighbours, cube remains active
    if 2 <= len(active_neighbours) <= 3:
      next_state.add(a)
    visited.add(a)

    # For each neighbour that is not already active and has not yet been visited, count the number of active neighbours
    for n in neighbours - (active_set | visited):
      n_active_neighbours = neighbour_set(n).intersection(active_set)
      if len(n_active_neighbours) == 3:
        #print("{} will be activated. It has the follwing three active neighbours: ".format(n))
        #[print(nn) for nn in neighbour_set(n).intersection(active_set)]
        next_state.add(n) 
      visited.add(n)

  return next_state

    


if __name__=='__main__':

  active_set = (read_initial_state(sys.argv[1]))
  # For each cube within distance 1 from active set, determine active/inactive in next state

  for _ in range(6):
    active_set = next_state(active_set)

  print(len(active_set))

  """
  active_set = next_state(active_set)
  active_set = next_state(active_set)
  [print(c) for c in active_set if c.z == 0]
  
  with open('out.txt', 'w') as f:
    for zs in range(min(space.keys()), max(space.keys())+1):
      f.write("Layer: "+ str(zs) + "\n")
      [f.write("".join(z)+"\n") for z in space[zs]]
  """