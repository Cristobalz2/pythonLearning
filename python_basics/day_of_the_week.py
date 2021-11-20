dotw = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
number = input("write a number between 1 and 7: ")
x = int(number)
if x <= 7 and x > 0:
  print(dotw[x-1])
else:
  print("number out of range")