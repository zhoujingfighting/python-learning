def add(a,b):
      answer = a + b
      print(str(a) + "+" + str(b) + "=", answer)

def sub(a,b):
      answer = a - b
      print(str(a) + "-" + str(b) + "=", answer)

def mul(a,b):
      answer = a * b
      print(str(a) + "*" + str(b) + "=", answer)

def divide(a,b):
      answer = a / b
      print(str(a) + "/" + str(b) + "=", answer)


print("*****Simple calculator*****")
print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")
print("E. Exit")

while True:
  choice = input("Please input your choice: ")
  if str(choice).lower() == 'a':
      print("Addition")
      a = int(input("Input first operand: "))
      b = int(input("Input second operand: "))
      add(a,b)
  elif str(choice).lower() == 'b':
      print("Subtraction")
      a = int(input("Input first operand: "))
      b = int(input("Input second operand: "))
      sub(a,b)
  elif str(choice).lower() == 'c':
      print("Multiplication")
      a = int(input("Input first operand: "))
      b = int(input("Input second operand: "))
      mul(a,b)
  elif str(choice).lower() == 'd':
      print("Division")
      a = int(input("Input first operand: "))
      b = int(input("Input second operand: "))
      divide(a,b)
  elif str(choice).lower() == 'e':
      print("Exit")
      quit()
  else:
     quit()