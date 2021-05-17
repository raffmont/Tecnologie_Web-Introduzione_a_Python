class Person:
  def __init__(self, f, l):
    self.first = f
    self.last = l	

  def print(self):
    print(self.first, self.last)

def swapFirstLast(p):
  p.first , p.last = p.last, p.first

person = Person("Jon", "Snow")
person.print()
swapFirstLast(person)
person.print()
