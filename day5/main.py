import sys

def find_max_seat_id(input_stream):
  max = 0
  seats = []
  with open(input_stream, 'r') as file:
    for bsp in file:
      curr = get_seat_id(bsp)
      seats.append(curr)
      if get_seat_id(bsp) > max:
        max = curr

  return max, seats

def get_seat_id(bsp):
  row = 0
  col = 0
  chars = list(bsp)
  
  for i in range(0,7):
    if chars[i] == 'B':
      row += 2**(6-i)

  for i in range(7,10):
    if chars[i] == 'R':
      col += 2**(2-(i-7))
  return (8 * row) + col

def find_free_seat(seats):
  for i in range(len(seats)):
    if seats[i+1] - seats[i] == 2:
      return seats[i]+1
    
  return -1

def main():
  max_seat_id, seats = find_max_seat_id(sys.argv[1])
  print(seats)
  seats.sort()
  print(seats)
  
  my_seat = find_free_seat(seats)
  print(my_seat)

main()