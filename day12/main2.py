import sys
import numpy

def read_instr(input):
  instr = []
  with open(input, 'r') as f:
    for line in f:
      instr.append((line[0], int(line[1:-1])))

  return instr 


def main():
  DIRECTION = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0)
  }

  instr = read_instr(sys.argv[1])

  ship_coord = numpy.array((0, 0)) # (WE, NS)
  ship_dir = numpy.array((1, 0))   # (WE, NS)

  waypoint = numpy.array((10, -1))

  for ins in instr:
    if ins[0] == 'F':
      ship_coord += ins[1] * waypoint

    elif ins[0] == 'L': 
      times = int(ins[1]/90)
      for _ in range(times):
        waypoint = numpy.matmul(waypoint, numpy.array([[0, -1], [1, 0]]))

    elif ins[0] == 'R': 
      times = int(ins[1]/90)
      for _ in range(times):
        waypoint = numpy.matmul(waypoint, numpy.array([[0, 1], [-1, 0]]))
    
    else:
      waypoint += ins[1] * numpy.array(DIRECTION[ins[0]])   


  print(ship_coord, ship_dir)
  print(abs(ship_coord[0])+abs(ship_coord[1]))

main()