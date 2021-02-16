import sys, re

FIELD_REQ = {
  'byr': r"^19[2-9]\d|200[0-2]$",
  'iyr': r"^201\d|2020$",
  'eyr': r"^202\d|2030$",
  'hgt': r"^(1[5-8]\d|19[0-3])cm|(59|6\d|7[0-6])in$",
  'hcl': r"^#[0-9a-f]{6}$",
  'ecl': r"^amb|blu|brn|gry|grn|hzl|oth$",
  'pid': r"^[0-9]{9}$",
  'cid': r"^.*$"
}

def read_passports(input_file):
  passports = [[]]
  pp_index = 0
  with open(input_file, 'r') as file:
    for line in file:
      if line == "\n":
        passports.append([])
        pp_index += 1
        continue
      else: 
        for kvs in line.split(" "):
          field = kvs.split(":")
          if not valid_field(field):
            continue
          else:
            passports[pp_index].append(field[0])

  print(passports)
  return passports

def valid_field(field):
  return bool(re.match(FIELD_REQ[field[0]], field[1]))

def count_valid_fields(passports, required_fields):
  valid_counter = 0
  for pp in passports:
    if not required_fields.difference(set(pp)):
      valid_counter += 1

  return valid_counter

def main():
  passports = read_passports(sys.argv[1])

  required_fields = {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'}
  valid_passport_count = count_valid_fields(passports, required_fields)
  print(valid_passport_count)

main()