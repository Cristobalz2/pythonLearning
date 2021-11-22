cookiesInJar = 20
cookiesEaten = 0
while cookiesInJar > 0:
  cookiesInJar -= 1
  print("you take a cookie")
  cookiesEaten += 1
  print(cookiesInJar, " Cookies left in the Jar")
  print("You have eaten ", cookiesEaten, " cookies")
print("You ate all cookies")
