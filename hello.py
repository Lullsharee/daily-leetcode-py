import math

ans = (math.sqrt(5) + 1 ) / 2
print(ans)

def bmi(height, weight):
  return weight / (height / 100.0) ** 2


print(bmi(188.0,104.0))

def ft_to_cm(f,i):
  return ((12*f+i)/12)*30.48

assert round(ft_to_cm(5, 2) - 157.48, 6) == 0
assert round(ft_to_cm(6, 5) - 195.58, 6) == 0

def quadratic(a,b,c,x):
  return a*x*x+b*x+c


n = 5

while n > 0:
  print(n)
  n -= 1
  

n = 10
while n > 0:
  print(n)
  n -= 1
  if n == 5:
    break
  if n % 2 ==0:
    continue
  print(n)


for i in range(5):
  print(i)

for i in range(5,10):
  print(i)

for i in reversed(range(5)):
  print(i)


for i in range(5):
  print(i)
else:
  print("done")

for i in range(5):
  if i == 3:
    break
  print(i)
else:
  print("done")


print(5/2)
print(5//2)