# Class 1

class India():
  def capital(self):

    print("New Delhi is the capital of India.")

def language(self):
  print("Hindi is the most widely spoken language of India")

def type(self):

 print("India is a developing country.")

# class 2
class USA():
 def capital(self):

  print("Washington, D.C. is the capital of USA.")

def language(self):
  print("English is the primary language of USA.")
  # Object Creation
obj_ind = India()

obj_usa = USA()

# Common Interface
for country in (obj_ind, obj_usa):
 country.capital()
 country.language()
 country.type()
 