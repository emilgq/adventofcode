import sys, os
import itertools

def count_trees(slopex, slopey):
  tree_count = 0
  right_shift = 0
  skip_step = 0

  with open(sys.argv[1], 'r') as file:

    l = file.readline()
    lim = len(l)-1  # Discount newline char
    file.seek(0, os.SEEK_SET)

    for line in file:
      if skip_step > 0: 
        skip_step -= 1
        continue 

      else:
        if right_shift >= lim:
          right_shift = right_shift % lim 

        if list(line)[right_shift] == '#':
          tree_count += 1

        right_shift += slopex
        skip_step = slopey -1

  return tree_count

def acc_tree_count(x, y):
  return x * count_trees(y[0],y[1])

def main():
  slopes = [1, (1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
  prod = itertools.accumulate(slopes, acc_tree_count)
  print(list(prod))
  

main()