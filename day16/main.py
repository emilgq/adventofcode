import linecache

valid_nums = [False]*1000
found_nums = []
ticket_ranges = []

input = "input.txt"

for i in range(1,21):
  low = [int(n) for n in linecache.getline(input, i)[:-1].split()[-3].split("-")]
  high = [int(n) for n in linecache.getline(input, i)[:-1].split()[-1].split("-")]
  print(low, high)
  for i in range(low[0],low[1]+1):
    valid_nums[i] = True
  for i in range(high[0],high[1]+1):
    valid_nums[i] = True
  ticket_ranges.append((low, high))

my_ticket = [int(n) for n in linecache.getline(input, 23)[:-1].split(',')]
print(my_ticket)

error_rate = 0
error_lines = 0

for i in range(26, 264):
  nums = [int(n) for n in linecache.getline(input, i)[:-1].split(',')]
  valid_ticket = True

  #print(nums)

  for j, n in enumerate(nums):
    if not valid_nums[n]:
      #print("Not valid: {} \t valid_nums[{}] = {}".format(str(n), str(n), valid_nums[n]))
      error_rate += n
      valid_ticket = False
    
  if valid_ticket:
    for j, n in enumerate(nums):
      if j > len(found_nums)-1:
        found_nums.append([n])
      else:
        found_nums[j].append(n)

  else: 
    error_lines += 1

list(map(lambda x: print(x), found_nums))
print(ticket_ranges)

def numbers_match_range(tkt_range, nums):
  for n in nums:
    #print(f"Evaluating if {tkt_range[0][0]} <= {n} <= {tkt_range[0][1]} or {tkt_range[1][0]} <= {n} <= {tkt_range[1][1]}")
    #print(not(tkt_range[0][0] <= n <= tkt_range[0][1] or tkt_range[1][0] <= n <= tkt_range[1][1]))
    if not(tkt_range[0][0] <= n <= tkt_range[0][1] or tkt_range[1][0] <= n <= tkt_range[1][1]):
      return False
  
  return True

unset_ticket_positions = 20
set_ticket_positions = [None]*20



while unset_ticket_positions > 1:
  for i, tr in enumerate(ticket_ranges):
    if tr == None:
      continue
    candidate_position = None
    multiple_candidates = False
    for j, ns in enumerate(found_nums):
      print(tr, ns)
      if ns == None:
        continue
      if numbers_match_range(tr, ns):
        # print("Numbers match range!")
        if candidate_position != None:
          multiple_candidates = True 
          # print("Too many candidates")
          break
        else: 
          candidate_position = j

    # Candidate found
    if not multiple_candidates and candidate_position != None:
      print("Determined ticket number {} maps to rule {}".format(candidate_position, i))
      set_ticket_positions[candidate_position] = i  # set_ticket_positions[0] = 5 means first ticket number maps to 5th rule
      unset_ticket_positions -= 1
      #remove ticket range
      ticket_ranges[i] = None
      found_nums[candidate_position] = None

print(ticket_ranges)
print(set_ticket_positions)

out = 1
for i, n in enumerate(set_ticket_positions):
  if n == None:
    continue 
  if n < 6:
    out *= my_ticket[i]

print(out)