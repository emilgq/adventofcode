import sys

questions_answered = set()
sum_of_counts = 0
new_group = True

with open(sys.argv[1], 'r') as file:
  for index, line in enumerate(file):
    if line == "\n":
      # Update sum of counts by adding size of current group
      # Clear group and indicate next line will be start of a new group
      # print(index, questions_answered, len(questions_answered))
      sum_of_counts += len(questions_answered)
      questions_answered.clear()
      new_group = True

    elif new_group == True:
      # New group means we start by adding first set of question answered
      questions_answered = set(line[:-1])
      new_group = False

    else: 
      # For the remainder of the group we update the set to be the intersection of all lines
      # print(questions_answered, set(line[:-1]))
      questions_answered.intersection_update(set(line[:-1]))

print(sum_of_counts)