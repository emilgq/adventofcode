import sys
import functools, operator

def read_bus_schedule(input):
  with open(input, 'r') as f:
    timestamp = int(f.readline()[:-1])
    # Extract bus numbers in functional fashion
    # buses = list(map(int, (filter(lambda x: x != 'x', f.readline().split(",")))))

    # Imperative fashion to carry on index
    buses = []
    for i, bus in enumerate(f.readline().split(",")):
      if bus != 'x':
        buses.append((int(bus), i))
    
    return timestamp, buses

def next_departures(timestamp, buses):
  departures = []
  time = 0
  for bus in buses:

    while time < timestamp:
      time += bus
    departures.append(time)
    time = 0
  
  return dict(zip(buses, departures))

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def find_subseq_departures(buses):
  sum_of_residues = 0
  product = functools.reduce(operator.mul, [b[0] for b in buses], 1)
  for b in buses:
    M = product // b[0]
    sum_of_residues += M * (b[0]-b[1]) * modinv(M, b[0]) 
  
  # Least common multiple of primes is product sum
  print(sum_of_residues)
  t = sum_of_residues % product
  return t

def verify(buses, t):
  print("T % B+offset = ?")
  for k,v in buses:
    print("{} % ({} + {}) = {}".format(t, k, v, (t+v)%k))

def main():
  timestamp, buses = read_bus_schedule(sys.argv[1])
  print(buses)
  print("You arrive at the bus terminal at: "+ str(timestamp))
  next_deps = next_departures(timestamp, [b[0] for b in buses])
  print("The buses depart at the following times: ")
  print(next_deps)
  print("Soonest departure to the airport")
  soonest = min(next_deps, key=next_deps.get)
  print("Bus: {}\nTime to departure: {}".format(soonest, next_deps[soonest]-timestamp))
  print("Puzzle answer (bus number * time to dep): " + str((next_deps[soonest]-timestamp)*soonest))
  t = find_subseq_departures(buses)
  print("Subsequent departures occur at timestamp: {}".format(str(t)))
  
  print(verify(buses, t))


if __name__=="__main__": 
  main()