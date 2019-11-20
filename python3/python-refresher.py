# variable
age = 26
name = 'diana'
print(age)

# conditional
if age > 18:
  print("You're officially an adult!")
else:
  print("Still young.")

# function
def hello():
  print("Hello World!")

hello()

# list
names = ['Fido', 'Freddy', 'Pippa', 'Frankie']
names.insert(0, 'Jane')
del(names[2]) # mutates
len(names) # get length

# loop
for name in names:
  print(name)

for x in range(1,10):
  print(x) # prints out 1 to 9

age = 0

while age < 18:
  print(age)
  age += 1

# dictionary
dogs = {"Fido": 10, "Freddy": 1, "Pippa": 5, "Frankie": 2}
del(dogs["Pippa"]) # mutates

# class
class Dog:
  def __init__(self, name, age, color):
    # instance variables
    self.name = name 
    self.age = age
    self.color = color

  def bark(self, paramter):
    print('Bark, ' + parameter)

mydog = Dog('Fido', 2, 'brown')
mydog.bark()

class Restaurant:
  bankrupt = False
  def open_branch(self):
    if not self.bankrupt:
      print('Open branch.')

# self refers to the class object