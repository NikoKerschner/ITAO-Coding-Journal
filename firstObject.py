class Person:
  def __init__(self, name, age, gender, hair_color):
    self.name = name
    self.age = age
    self.gender = gender
    self.hair_color = hair_color

p1 = Person("Niko", 21, "Male","Brown")

print(p1.name)
print(p1.age)
print(p1.gender)
print(p1.hair_color)