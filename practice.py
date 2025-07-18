import math 

def add(x,y):
  return x + y

def subtract(x,y):
  return x - y

def mulitply(x,y):
  return x * y

def divide(x,y):
  if y == 0:
    return "Error: cant divide by zero"
  else:
    return x/y

def modulo(x,y):
  return x & y

def int_divide(x,y):
   if y == 0:
    return "Error: cant divide by zero"
  else:
    return x//y

def sqrt(x):
  if x < 0:
    return "Error: cant square root a neg number"
  else math.sqrt(x)

def main():
  


