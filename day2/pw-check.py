def main():
  valid_pass_count = 0
  try: 
    line = input()
    while line != None:
      counter = 0
      rule_count, rule_char, password = line.split(" ")
      lower_bound, upper_bound = rule_count.split("-")
      rule_char = rule_char[0]
      password = list(password)
      

      if bool(password[int(lower_bound)-1] ==rule_char) ^ bool(password[int(upper_bound)-1] == rule_char):
       valid_pass_count += 1

      line = input()
  except EOFError:
    print(valid_pass_count)
main()