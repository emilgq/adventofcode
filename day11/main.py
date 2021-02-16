import sys

def run_one_round(room):
  next_room = [list('.'*100)]
  changes = 0

  for i in range(1, len(room)-1):
    next_room.append(['.'])
    for j in range(1, len(room[i])-1):
      if room[i][j] == 'L' and will_be_taken(room, i,j):
        next_room[i].append('#')
        changes += 1

      elif room[i][j] == '#' and will_be_vacated(room, i,j):
        next_room[i].append('L')
        changes += 1
      
      else:
        next_room[i].append(room[i][j])
    next_room[i].append('.')
  
  next_room.append(list('.'*100))

  return next_room, changes
      
def will_be_taken(room, i,j):
  if room[i][j] in ['#', '.']:
    raise ValueError(message="invalid slots to evaluate")

  for diry in range(-1, 2):
    for dirx in range(-1, 2):
      if (diry,dirx) == (0,0):
        continue
      if is_occupied(room, i, j, diry, dirx) == 1: 
        return False
        
  return True

"""
.#.LL
#L.LL i=1, j=4, [1]
..L.L
#.LL# i=3, j=4, [3, 2, 1]
L#.#L
"""

def is_occupied(room, i,j, diry, dirx):
  while True:
    i = i + diry
    j = j + dirx
    try:
      if room[i][j] == '#':
        return 1
      if room[i][j] == 'L':
        return 0
    except IndexError:
      return 0

def will_be_vacated(room, i,j):
  if room[i][j] in ['.', 'L']:
    raise ValueError(message="invalid slots to evaluate")
  
  count_vis_adj = 0
  for diry in range(-1, 2):
    for dirx in range(-1, 2):
      if (diry,dirx) == (0,0):
        continue
      count_vis_adj += is_occupied(room, i, j, diry, dirx)

  return count_vis_adj >= 5

def write_room(room, target):
  with open(target, 'w') as out:
    for row in room[1:-1]:
      out.write("".join(row[1:-1])+'\n')

    out.close()

def main():
  WAITING_ROOM = []
  NEXT_ROOM = []
  CHANGES = 1
  ROUNDS = 0

  WAITING_ROOM.append(list('.'*100))
  with open(sys.argv[1], 'r') as file:
    for line in file:
      WAITING_ROOM.append(list("." + line[:-1] + "."))
  WAITING_ROOM.append(list('.'*100))
  """
  write_room(WAITING_ROOM, "o0.txt")
  WAITING_ROOM, CHANGES = run_one_round(WAITING_ROOM)
  write_room(WAITING_ROOM, "o1.txt")
  WAITING_ROOM, CHANGES = run_one_round(WAITING_ROOM)
  write_room(WAITING_ROOM, "o2.txt")
  WAITING_ROOM, CHANGES = run_one_round(WAITING_ROOM)
  write_room(WAITING_ROOM, "o3.txt")
  """
  while CHANGES > 0:
    WAITING_ROOM, CHANGES = run_one_round(WAITING_ROOM)
    ROUNDS += 1
    print("ROUND {}, CHANGES {}".format(ROUNDS, CHANGES))
  
  seats_taken = 0
  for row in WAITING_ROOM:
    for col in row:
      if col == '#':
        seats_taken += 1
  
  write_room(WAITING_ROOM, 'output.txt')
  print(seats_taken)
main()