import sys

class Expr:
  def __init__(self, line):
    self.expression = self.parse(line) 

  def parse(self, line):
    expression = []
    i = 0
    while i < len(line):
      if line[i] == '(':
        # finding the sub-expression jumps to closing parenthesis
        s, i = self.subexpr(i, line)
        expression.append(s)
      else: 
        expression.append(line[i])
        i += 1
      
    for i, e in enumerate(expression):
      if type(e) != Expr and e not in ('*', '+'):
        expression[i] = int(e)

    return expression

  def subexpr(self, start, line):
    count_left_pars = 0
    for i in range(start+1, len(line)):
      if line[i] == ')':
        if count_left_pars == 0:
          return Expr(line[start+1:i]), i+1
        else: 
          count_left_pars -= 1

      elif line[i] == '(':
        count_left_pars += 1
      
  def eval1(self):
    result = self.expression[0].eval1() if type(self.expression[0])==Expr else int(self.expression[0])
    i = 1
    while i < len(self.expression):
      if self.expression[i] == '+':
        result += self.expression[i+1].eval1() if type(self.expression[i+1])==Expr else int(self.expression[i+1])
      else: 
        result *= self.expression[i+1].eval1() if type(self.expression[i+1])==Expr else int(self.expression[i+1])
      i += 2
    return result

  def eval2(self):
    i = 1
    while i < len(self.expression):      
      if self.expression[i] == '+':
        if type(self.expression[i-1]) == Expr:
          if type(self.expression[i+1]) == Expr:
            self.expression[i-1] = self.expression[i-1].eval2() + self.expression[i+1].eval2()
          else: 
            self.expression[i-1] = self.expression[i-1].eval2() + self.expression[i+1]

        elif type(self.expression[i+1]) == Expr:
          self.expression[i-1] = self.expression[i-1] + self.expression[i+1].eval2()
        
        else: 
          self.expression[i-1] = self.expression[i-1] + self.expression[i+1]

        self.expression.pop(i+1)
        self.expression.pop(i)

      else: 
        if type(self.expression[i]) == Expr:
          self.expression[i] = self.expression[i].eval2()
        i += 2

    i = 1
    result = self.expression[0].eval2() if type(self.expression[0])==Expr else self.expression[0]
    print(self.expression)
    while i < len(self.expression):
      result *= self.expression[i+1].eval2() if type(self.expression[i+1])==Expr else self.expression[i+1]
      i += 2
    
    return result

def read_homework(input):
  expressions = []
  with open(input, 'r') as f:
    for l in f:
      tokens = [char for char in l[:-1] if char != ' ']
      expressions.append(Expr(tokens))

  return expressions


def main():
  sum = 0
  expressions = read_homework(sys.argv[1])
  for e in expressions:
    evaluated = e.eval2()
    print(evaluated)
    sum += evaluated

  print(sum)

  print(expressions[-1].expression, expressions[-1].expression[2].expression)
main()