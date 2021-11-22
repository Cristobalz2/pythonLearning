# print("var=10\nif var > 10:\vprint('la casa esta vacia')\nfin del programa" )
def mix_up(a, b):
  # +++your code here+++\
  # a[0] = b[0]

  strA = a.replace(a[:2],b[:2]) 
  strB = b.replace(b[:2],a[:2])
  return strA + " " + strB
a= 'mix'
b= 'pod'
print(mix_up(a,b))
def fix_start(s):
  
  # +++your code here+++
  
  return s[0] + s[1:].replace(s[0], '*')

# print(fix_start('babble'))