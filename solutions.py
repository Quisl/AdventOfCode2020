numbers = open("numbers.txt","r").read().split("\n")

def day1():
  for i in numbers:
    for j in numbers[numbers.index(i):]:
      if int(i)+int(j) == 2020:
        return (int(i)*int(j))

def day2():
  for i in numbers:
    for j in numbers[numbers.index(i):]:
      for x in numbers[numbers.index(j):]:
        if int(i)+int(j)+int(x)==2020:
          return (int(i)*int(j)*int(x))


print(str(day1()))
print(str(day2()))
