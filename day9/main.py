import sys

data = []

def find_two_sum(preamble, goal):
  left = 0
  right = len(preamble)-1
  while right > left:
    two_sum = preamble[left] + preamble[right]
    if two_sum == goal:
      return True
    if two_sum > goal: 
      right -= 1
    else:
      left += 1
  return False


with open(sys.argv[1], 'r') as file:
  for line in file:
    data.append(int(line[:-1]))

no_sum_idx = 0
target = 0

# Find encryption error
for i in range(25, len(data)):
  preamble = data[i-25:i]
  preamble.sort()
  if not find_two_sum(preamble, data[i]):
    no_sum_idx = i
    target = data[i]
    break

print("INDEX & DATA: {}, {}".format(no_sum_idx, target))

# Find contiguous set that sum up to target
for i in range(0, no_sum_idx):
  sublist = [data[i]]
  weakness_sum = data[i]
  j = i+1
  while weakness_sum < target:
    sublist.append(data[j])
    weakness_sum += data[j]
    if weakness_sum == target:
      print(sublist)
      sublist.sort()
      print(sublist)
      print("Encryption weakness: {} & {}".format(sublist[0], sublist[-1]))
      print("Encryption weakness sum: " + str(sublist[0]+sublist[-1]))
      break

    j = j+1
  
