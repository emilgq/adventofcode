import sys
from collections import namedtuple

def read_docking_program(input):
  Instr = namedtuple('Instruction', 'type address value')
  instructions = []
  with open(input, 'r') as f:
    for line in f:
      if line[0:2] == 'ma':
        instructions.append(Instr('mask', None, line.split()[2]))
      else: 
        ins = line.split()
        instructions.append(Instr('write', ins[0][4:-1], ins[2]))

  return instructions

def bin(num, len=None):
  x = 0
  n = int(num)
  binary = []
  while 2**(x+1) <= n:
    x += 1
  if len is not None:
    for i in range(len-1, -1, -1):
      if i > x:
        binary.append(0)
      else:
        if n >= 2**i:
          binary.append(1)
          n -= 2**i

        else:
          binary.append(0)
  else: 
    for i in range(x, -1, -1):
      if n >= 2**i:
        binary.append(1)
        n -= 2**i

      else:
        binary.append(0)

  return binary

def bin2int(binary):
  bint = 0
  for i in range(len(binary)):
    if binary[i] == 1:
      bint += 2**(len(binary)-1-i)
  return bint

def apply_mask(val, mask):
  bin_val = bin(val, len(mask))
  for i in range(len(mask)):
    if mask[i] == 'X':
      continue
    else: 
      bin_val[i] = int(mask[i])
  return bin2int(bin_val)

def apply_mask_address(address, mask):
  """
  V: 01111
  M: 1X1X0
  O: 1X1X1 -> 10101, 10111, 11101, 11111
  OUT: Decimal values of all mask-output addresses 
  """
  x_count = 0
  x_indices = []
  bin_val = bin(address, len(mask))
  for i in range(len(mask)):
    if mask[i] == '0':
      continue
    elif mask[i] == '1': 
      bin_val[i] = 1
    else: 
      bin_val[i] = None
      x_indices.append(i)
      x_count += 1
    
  addresses = []
  # For each X, generate 2 addresses
  if x_count > 0: 
    for i in range(2**x_count):
      # One address
      x = bin(i, x_count) # e.g. [1,1]
      for idx, e in enumerate(x_indices): # e.g. [1, 3]
        bin_val[e] = x[idx]  
      addresses.append(bin2int(bin_val.copy()))
    
    return addresses
  
  else:
    return [bin_val]
    

def execute(instructions,  mac=False):
  mask = None
  memory = {}
  if not mac:
    for instr in instructions:
      if instr.type == 'mask':
        mask = instr.value

      else:
        memory[instr.address] = apply_mask(instr.value, mask)
    return memory

  else: 
    for instr in instructions:
      if instr.type == 'mask':
        mask = instr.value
      else: 
        addresses = apply_mask_address(instr.address, mask)
        for a in addresses:
          memory[a] = int(instr.value)
    return memory

def sum_memory(memory):
  return sum(memory.values())

def main():
  instructions = read_docking_program(sys.argv[1])
  memory = execute(instructions, True)
  remainder = sum_memory(memory)
  print(remainder)

if __name__=='__main__':
  main()