def process_price(v):
  s = None

  try:
    s = ''.join(map(lambda x: char_to_digit[x], v))
  except KeyError as (strerror):
    print "Don't know what to do with this:",strerror

  return s

def parse(filename):

  f = open(filename, 'r')

  d = {}

  #pattern = re.compile("R*\.)")

  for line in f.readlines():
    m = re.match(".*R(\w+\.\w+)", line) #relient on matching digits
    if m: 
      print m.group(0)
      item = ' '.join(m.group(0).split(" ")[:-1])
      val = process_price(m.group(1))
      d[item] = val 

  return d

def sum_prices(d):
  return sum(map(lambda x: float(x), d.values()))

d = parse("out.txt") 
print d
print sum_prices(d)
