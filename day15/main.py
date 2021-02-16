INPUT = [13,16,0,12,15,1]

def main():
  nums = {}
  for i, n in enumerate(INPUT):
    nums[n] = i

  print(nums)

  round = len(INPUT)
  last_num = INPUT[-1]
  while round < 30000000:
    # print("Starting round " + str(round))
    # First occurence of last number was last round
    # print("LAST_NUM: {} \t LAST_OCC: {} \t ROUND {}".format(last_num, nums[last_num], round-1))
    try:
      diff = round - (1 + nums[last_num]) # difference between last numbers two most recent occurences
      # print("{} was called {} rounds ago.".format(last_num, diff))
      nums[last_num] = round-1            # record last numbers latest occurence
      last_num = diff                     # Update last number to current difference
    except KeyError:                      # New numbers will raise exceptions since number is not in dict
      # print("{} was called for the first time.".format(last_num))
      nums[last_num] = round -1
      last_num = 0

    round += 1
    
  print(last_num)

main()