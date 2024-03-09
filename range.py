
#before debugging
for number in range (1,10):
  if number%3==0 or number%5==0:
        print("fizzbuzz")
  if number%3==0:
        print("fizz")
  if number%5==0:
        print("buzz")
  else:
        print(number)


# after debugging
for number in range (1,10):
  if number%3==0 and number%5==0:
        print("fizzbuzz")
  if number%3==0:
        print("fizz")
  if number%5==0:
        print("buzz")
  else:
        print(number)