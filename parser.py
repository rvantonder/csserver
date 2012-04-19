import re

char_to_digit = {"l" : "1", 
                 "T" : "1", 
                 "I" : "1", 
                 "0" : "0", 
                 "1" : "1", 
                 "2" : "2", 
                 "3" : "3", 
                 "4" : "4", 
                 "5" : "5", 
                 "6" : "6", 
                 "7" : "7", 
                 "8" : "8", 
                 "9" : "9",
                 "." : "."}

def process_price(v):
  """
  In: string value such as '3T.99'
  Out: Common mistakes corrected, such as character T -> 1
  """

  s = None

  try:
    s = ''.join(map(lambda x: char_to_digit[x], v))
  except KeyError as (strerror):
    print "Don't know what to do with this:",strerror

  return s

def parse(filename):
  """
  In: filename
  Out: dictionary with parsed values (text)
  """

  f = open(filename, 'r')

  d = {}

  for line in f.readlines():
    #matches something like: "blah blah R(31.99)<ignored>"
    m = re.match(".*R(\w+\.\w+)", line) #relient on matching digits
    if m: 
      #print m.group(0) #entire line
      item = ' '.join(m.group(0).split(" ")[:-1])
      val = process_price(m.group(1)) #converts common OCR number 'mistakes'
      d[item] = val 

  return d

def sum_prices(d):
  return sum(map(lambda x: float(x), d.values()))

d = parse("out.txt") 
print d
print sum_prices(d)
