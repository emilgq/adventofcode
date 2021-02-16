import sys

CONTAINERS = {}
CONTAINS = {}


with open(sys.argv[1], 'r') as file:
  for line in file:
    if line == "\n":
      continue

    info = line.split()
    print(info)
    container = "{} {}".format(info[0], info[1])   
    if container not in CONTAINERS.keys():
      CONTAINERS[container] = set()

    if container not in CONTAINS.keys():
      CONTAINS[container] = {}
    
    for i in range(5, len(info)-1):
      if info[i-1] == 'no': 
        break

      if i % 4 == 1:
        contained = "{} {}".format(info[i], info[i+1])
        if contained not in CONTAINERS.keys():
          CONTAINERS[contained] = set()

        CONTAINERS[contained].add(container)
        CONTAINS[container][contained] = info[i-1]

BAGS_USED = set()

def find_containers(bag):

  for bg in CONTAINERS[bag]:
    if bg not in BAGS_USED:
      BAGS_USED.add(bg)
      find_containers(bg)

  return

def count_sub_bags(bag):
  count = 0
  print("Counting sub-bags for: " + bag)
  print("Contains: " + str(CONTAINS[bag]))
  if not bool(CONTAINS[bag]): 
    return 0

  for k,v in CONTAINS[bag].items():
    count += int(v) + int(v) * count_sub_bags(k) # Count the bag plus its recursive sub-bags

  return count

print(CONTAINERS['shiny gold'])
find_containers('shiny gold')
print(BAGS_USED)
print(len(BAGS_USED))

print(CONTAINS['shiny gold'])
print(count_sub_bags('shiny gold'))