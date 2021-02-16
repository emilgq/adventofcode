import sys, functools, operator, math, itertools, collections

def parse_input(input):
  with open(input, 'r') as f:
    data = list(map(str.rstrip,f))
    tiles = {str.rstrip(data[x].split()[1], ':'): data[x+1:x+11] for x in range(0, len(data), 12)} 
    # dimension_size = int(math.sqrt(len(tiles_data)))
    print(len(tiles))
    return tiles

def get_side(tiles, tile_number, side):
  tile = tiles[tile_number]
  if side == 'u':
    return tile[0]
  elif side == 'd':
    return tile[-1]
  elif side == 'l':
    return ''.join([t[0] for t in tile])
  elif side == 'r':
    return ''.join([t[-1] for t in tile])
  else:
    raise Exception

def find_adjacencies(tiles):
  # {tile_number: [<borders with no match>]}
  adjacencies = collections.defaultdict(list)
  print(tiles.keys())
  for (t1, t2) in itertools.combinations(tiles.keys(), 2):
    for t1_side in 'udlr':
      for t2_side in 'udlr':
        this_side = get_side(tiles, t1, t1_side)
        other_side = get_side(tiles, t2, t2_side)

        if this_side == other_side:
          adjacencies[t1].append((t2, t1_side, False))
          adjacencies[t2].append((t1, t2_side, False))
        elif this_side == other_side[::-1]:
          adjacencies[t1].append((t2, t1_side, True))
          adjacencies[t2].append((t1, t2_side, True))

  return adjacencies

def assemble_image(tiles, adjacencies, start):
  dimension = int(len(tiles) ** 0.5)
  image = [[None] * dimension for _ in range(dimension)]
  i,j = 0,0
  remaining_tiles = set(tiles.keys()) - {start}
  image[i][j] = (start, False)
  queue = []
  curr = start
  for adj in adjacencies[start]:
    f
    queue.append(adj)


     
   
  

# def find_frame(border_tiles, start, size):
#   frame = [[None] * size for _ in range(size)]
#   frame[0][0] = start
#   unused = set(border_tiles - [start])

#   print(border_tiles)
#   print(unused)

#   # Fill top border of frame
#   for i in range(1, len(frame[0])):
#     for k,v in 
#   print(frame)
            

tiles = parse_input(sys.argv[1])

# In order to begin image assembly, I need to identify the border tiles. 
# These can be found by identifying tiles for which at least 1 edge has
# no other matching tile. 4 tiles will have two non-matching edges. 

# First I'll identify all adjacencies
adjacencies = find_adjacencies(tiles)
print(adjacencies)
print(functools.reduce(lambda x, y: x * y, [int(k) for k,v in adjacencies.items() if len(v) == 2]))

for c, adj in [(k, v) for k, v in adjacencies.items() if len(v) == 2]:
  adj_sides = ''.join([a[1] for a in adj])
  if adj_sides in ['dr', 'rd']:
    top_left = c

assemble_image(tiles, adjacencies, top_left)

# Now I'm ready to identify the corners and multiply the 4 corner tile numbers together
# corners = [t for (t,v) in border_tiles.items() if len(v) == 2]
# answer1 = functools.reduce(operator.mul, [int(c) for c in corners], 1)
# print(answer1)

# Next up I'll need to identify the positions of each border tile. 
# I'll do this by chaining together border tiles, with start in a corner
# And add matching border pieces until I've exhausted all borders pieces, 
# I should end up with a frame
# image_frame = find_frame(border_tiles.keys(), corners[0], dimension_size)