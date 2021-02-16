import linecache,sys

def read_instructions():
  instr = []
  with open(sys.argv[1], 'r') as file:
    for line in file:
      temp = line[:-1].split(" ")
      instr.append([temp[0], temp[1]])
  return instr

def run_program(instructions, ):
  acc = 0
  pc = 0
  visited = set()
  while pc < len(instructions):
    if pc in visited:
      print("Loop started on line " + str(pc+1))
      return acc, False

    x = instructions[pc]

    if x[0] == 'acc':
      acc += int(x[1])

    if x[0] == 'jmp':
      pc += int(x[1])-1
     
    visited.add(pc)
    pc += 1

  print("Program terminated")
  return acc, True

instr = read_instructions()

for i in range(len(instr)):
  if instr[i][0] == 'nop':
    instr[i][0] = 'jmp'
    acc, succeeded = run_program(instr)
    if succeeded:
      print("Program repaired, line {} was changed nop->jmp".format(i+1))
      print("Accumulator: " + str(acc))
      break
    else:
      instr[i][0] = 'nop'

  if instr[i][0] == 'jmp':
    instr[i][0] = 'nop'
    acc, succeeded = run_program(instr)
    if succeeded:
      print("Program repaired, line {} was changed jmp->nop".format(i+1))
      print("Accumulator: " + str(acc))
      break
    else:
      instr[i][0] = 'jmp'

print(acc)