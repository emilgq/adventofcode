import sys
from functools import lru_cache 

ADAPTERS = []

with open(sys.argv[1], 'r') as file:
  for line in file:
    ADAPTERS.append(int(line[:-1]))

print(ADAPTERS)
ADAPTERS.append(0)
ADAPTERS.sort()
print(ADAPTERS)
ADAPTERS.append(ADAPTERS[-1]+3)
print(ADAPTERS)


diffByOne = 0
diffByThree = 0

for i in range(len(ADAPTERS)-1):
  diff = ADAPTERS[i+1] - ADAPTERS[i]
  if diff == 1:
    diffByOne += 1
  elif diff == 3:
    diffByThree += 1
  elif diff == 2:
    continue
  else: 
    print("No fitting adapter found")

print("1-jolt differences: " + str(diffByOne))
print("3-jolt differences: " + str(diffByThree))
print("Product: " + str(diffByOne*diffByThree))

# LRU Cache allows me to memoize function calls and thus reuse the result as opposed to have to recalculate 
# the function call when subproblems overlap. 
@lru_cache()
def count_conf(idx):
  if idx == len(ADAPTERS)-1:
    return 1

  confs = 0 
  # For each list element, I will have to evalute up to 3 consecutive elements, depending on where I am in the list
  # For the consecutive elements, I must evaluate whether I can connect to it with ADAPTER[idx] by checking the difference
  # If that is the case, I must then recursively calculate how many configurations follow that connection 
  for i in range(idx+1, min(idx+4, len(ADAPTERS))):
    if ADAPTERS[i] - ADAPTERS[idx] <= 3:
      confs += count_conf(i)
    else: 
      break
  
  return confs

print("Total number of possible configurations: " + str(count_conf(0)))