class Person:
  def __init__(self, first, last):
    self.first = first
    self.last = last

  def __str__(self):
    return f"{self.first} {self.last}"

def create_person(first=None, last=None,
                  person_base=Person("Gina", "Jones")):
  if first: person_base.first = first
  if last: person_base.last = last
  return person_base

person_default = create_person()
print(person_default)
person_A = create_person("Ada")
print(person_A)
person_B = create_person("Beda")
print(person_B)
print(person_A)
print(person_default)
