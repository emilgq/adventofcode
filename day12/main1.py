import sys
import numpy

def read_instr(input):
  instr = []
  with open(input, 'r') as f:
    for line in f:
      instr.append((line[0], int(line[1:-1])))

  return instr 


def main():
  instr = read_instr(sys.argv[1])

  ship_coord = numpy.array((0, 0)) # (WE, NS)
  ship_dir = numpy.array((1, 0))   # (WE, NS)

  for ins in instr:
    if ins[0] == 'F':
      ship_coord += ins[1] * ship_dir

    if ins[0] == 'B':
      ship_coord += -ins[1] * ship_dir

    if ins[0] == 'N':
      ship_coord += ins[1] * numpy.array((0, -1)) 

    if ins[0] == 'E':
      ship_coord += ins[1] * numpy.array((1, 0)) 

    if ins[0] == 'S':
      ship_coord += ins[1] * numpy.array((0, 1)) 

    if ins[0] == 'W':
      ship_coord += ins[1] * numpy.array((-1, 0)) 

    if ins[0] == 'L': 
      times = int(ins[1]/90)
      for _ in range(times):
        ship_dir = numpy.matmul(ship_dir, numpy.array([[0, -1], [1, 0]]))

    if ins[0] == 'R': 
      times = int(ins[1]/90)
      for _ in range(times):
        ship_dir = numpy.matmul(ship_dir, numpy.array([[0, 1], [-1, 0]]))


  print(ship_coord, ship_dir)
  print(abs(ship_coord[0])+abs(ship_coord[1]))

main()